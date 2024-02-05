# Django
from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    external_id = serializers.CharField()
    customer_external_id = serializers.CharField(max_length=255)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.IntegerField()
    paid_at = serializers.DateTimeField(allow_null=True, required=False)


class PaymentDetailSerializer(serializers.Serializer):
    external_id = serializers.CharField(source="payment.external_id")
    customer_external_id = serializers.CharField(max_length=255, source="loan.customer.external_id")
    loan_external_id = serializers.CharField(source="loan.external_id")
    payment_date = serializers.DateTimeField(format="%Y-%m-%d", source="payment.paid_at")
    status = serializers.IntegerField(source="payment.status")
    total_amount = serializers.DecimalField(
        source="payment.total_amount", max_digits=10, decimal_places=2
    )
    payment_amount = serializers.DecimalField(source="amount", max_digits=20, decimal_places=2)
