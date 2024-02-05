# Django
from django.urls import path

# Current Folder
from .views import LoanCreateView, LoansByCustomerView

urlpatterns = [
    path("", LoanCreateView.as_view(), name="loan-create"),
    path(
        "customer/<str:customer_external_id>/",
        LoansByCustomerView.as_view(),
        name="loans-by-customer",
    ),
]
