# Django
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Current Folder
from .adapters.repository import LoanRepository
from .serializers import LoanSerializer
from ..customers.adapters.repository import CustomerRepository
from ..utils.mixins import ExceptionHandlerMixin
from ...domain.loans.models import LoanData
from ...domain.loans.services.services import LoanService


class LoanCreateView(ExceptionHandlerMixin, APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            loan_data = LoanData(**validated_data)
            service = LoanService(LoanRepository(), CustomerRepository())
            try:
                loan = service.create(loan_data)
                return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoansByCustomerView(ExceptionHandlerMixin, APIView):

    def get(self, request, customer_external_id: str):
        service = LoanService(LoanRepository(), CustomerRepository())
        loans = service.get_loans_by_customer(customer_external_id)
        return Response(LoanSerializer(loans, many=True).data)
