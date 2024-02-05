# Django
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal
from services.django_apps.customers.adapters.repository import (
    CustomerRepository,
)
from services.django_apps.customers.models import Customer
from services.django_apps.customers.serializers import (
    CustomerBalanceSerializer,
    CustomerSerializer,
)
from services.django_apps.utils.mixins import ExceptionHandlerMixin
from services.domain.customers.models import CustomerData
from services.domain.customers.services.services import CustomerService
from services.domain.utils.authenticators.api_key import ApiKeyAuthenticator


class CustomerCreateView(ExceptionHandlerMixin, APIView):
    """
    API view for creating a new customer.

    Attributes:
        authentication_classes (tuple): Tuple containing the ApiKeyAuthenticator.
    """

    authentication_classes = (ApiKeyAuthenticator,)

    def post(self, request):
        """
        Handles POST requests to create a new customer.

        Args:
            request: The request object containing customer data.

        Returns:
            Response: The HTTP response with the created customer data or error messages.
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            if "score" in validated_data:
                validated_data["score"] = float(validated_data["score"])

            customer_data = CustomerData(**validated_data)
            service = CustomerService(CustomerRepository())
            try:
                customer = service.create(customer_data)
                return Response(CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerBalanceView(ExceptionHandlerMixin, APIView):
    """
    API view for retrieving the balance information of a customer.
    """

    def get(self, request, external_id):
        """
        Handles GET requests to retrieve customer balance information.

        Args:
            request: The request object.
            external_id (str): The external ID of the customer.

        Returns:
            Response: The HTTP response with the customer's balance
            information or an error message.
        """
        service = CustomerService(CustomerRepository())
        try:
            balance_data = service.get_balance(external_id)
            return Response(CustomerBalanceSerializer(balance_data).data)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


class CustomerRetrieveView(ExceptionHandlerMixin, generics.RetrieveAPIView):
    """
    API view for retrieving a specific customer by their external ID.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "external_id"
