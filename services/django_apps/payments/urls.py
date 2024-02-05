# Django
from django.urls import path

# Current Folder
from .views import PaymentCreateView, PaymentsByCustomerView

urlpatterns = [
    path("", PaymentCreateView.as_view(), name="create-payment"),
    path(
        "by-customer/<str:customer_external_id>/",
        PaymentsByCustomerView.as_view(),
        name="payments-by-customer",
    ),
]
