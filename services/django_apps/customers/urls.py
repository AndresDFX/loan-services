# Django
from django.urls import path

# Current Folder
from .views import (
    CustomerBalanceView,
    CustomerCreateView,
    CustomerRetrieveView,
)

urlpatterns = [
    path("", CustomerCreateView.as_view(), name="customer-create"),
    path(
        "<str:external_id>/balance/",
        CustomerBalanceView.as_view(),
        name="customer-balance",
    ),
    path(
        "<str:external_id>/",
        CustomerRetrieveView.as_view(),
        name="customer-retrieve",
    ),
]
