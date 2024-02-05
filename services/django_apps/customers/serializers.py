# Django
from rest_framework import serializers

# Current Folder
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerBalanceSerializer(serializers.Serializer):
    external_id = serializers.UUIDField()
    score = serializers.DecimalField(max_digits=10, decimal_places=2)
    available_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_debt = serializers.DecimalField(max_digits=10, decimal_places=2)
