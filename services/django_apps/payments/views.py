# Django
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Current Folder
from .adapters.repository import PaymentDetailRepository, PaymentRepository
from .serializers import PaymentDetailSerializer, PaymentSerializer
from ..customers.adapters.repository import CustomerRepository
from ..loans.adapters.repository import LoanRepository
from ..utils.mixins import ExceptionHandlerMixin
from ...domain.payments.models import PaymentData
from ...domain.payments.services.services import PaymentService


class PaymentCreateView(ExceptionHandlerMixin, APIView):
    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment_service = PaymentService(
                payment_repository=PaymentRepository(),
                payment_detail_repository=PaymentDetailRepository(),
                loan_repository=LoanRepository(),
                customer_repository=CustomerRepository(),
            )

            try:
                payment_data = PaymentData(**serializer.validated_data)
                payment = payment_service.create_payment(payment_data)
                return Response(
                    PaymentSerializer(payment).data,
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentsByCustomerView(ExceptionHandlerMixin, APIView):
    def get(self, request, customer_external_id: str):
        payment_service = PaymentService(
            payment_repository=PaymentRepository(),
            payment_detail_repository=PaymentDetailRepository(),
            loan_repository=LoanRepository(),
            customer_repository=CustomerRepository(),
        )
        payments = payment_service.get_payment_details_by_customer(customer_external_id)
        return Response(PaymentDetailSerializer(payments, many=True).data)
