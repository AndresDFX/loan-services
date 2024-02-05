# Django
from rest_framework.permissions import BasePermission

# Internal
from services.django_apps.customers.models import Customer


class CustomerAuthenticated(BasePermission):
    def has_permission(self, request, view) -> bool:
        customer = request.user
        return isinstance(customer, Customer)


class IsCustomerOwner(BasePermission):
    def has_permission(self, request, view):
        customer = request.user
        for key, value in view.kwargs.items():
            if hasattr(customer, key):
                return bool(getattr(customer, key) == value)
