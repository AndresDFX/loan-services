# Django
from rest_framework import serializers

# Internal
from services.domain.loans.constants import LoanStatus


class LoanSerializer(serializers.Serializer):
    external_id = serializers.CharField()
    customer_external_id = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    status = serializers.IntegerField(default=LoanStatus.ACTIVE)
    contract_version = serializers.CharField(max_length=30, write_only=True)
    maximum_payment_date = serializers.DateTimeField(
        write_only=True, allow_null=True, required=False
    )
    outstanding = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
