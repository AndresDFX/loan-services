# Standard Library
from typing import Any, List

# Django
from django.db import transaction
from django.db.models import F
from django.utils import timezone

# Internal
from services.django_apps.customers.models import Customer
from services.django_apps.loans.models import Loan
from services.django_apps.payments.models import Payment, PaymentDetail
from services.domain.loans.constants import LoanStatus
from services.domain.payments.constants import PaymentStatus
from services.domain.payments.models import PaymentData, PaymentDetailData
from services.domain.payments.repository import (
    AbstractPaymentDetailRepository,
    AbstractPaymentRepository,
)


class PaymentRepository(AbstractPaymentRepository):
    def add(self, payment_data: PaymentData) -> PaymentData:
        customer = Customer.objects.get(external_id=payment_data.customer_external_id)
        payment = Payment.objects.create(
            external_id=payment_data.external_id,
            customer=customer,
            total_amount=payment_data.total_amount,
            status=payment_data.status or PaymentStatus.COMPLETED,
            paid_at=payment_data.paid_at or timezone.now(),
        )
        payment_data_return = PaymentData(
            id=payment.id,
            external_id=payment.external_id,
            customer_external_id=customer.external_id,
            customer_id=customer.id,
            total_amount=payment.total_amount,
            status=payment.status,
            paid_at=payment.paid_at,
        )

        return payment_data_return

    def get_by_external_id(self, external_id: str) -> Payment:
        return Payment.objects.get(external_id=external_id)

    def list_all(self):
        return Payment.objects.all()

    def get_active_loans_by_customer(self, customer_external_id: str):
        return Loan.objects.filter(
            customer__external_id=customer_external_id,
            status=LoanStatus.ACTIVE,
        ).annotate(loan_external_id=F("external_id"))

    @transaction.atomic
    def update_loan_payment(self, loan, payment_amount):
        loan.outstanding -= payment_amount
        loan.status = LoanStatus.PAID if loan.outstanding <= 0 else loan.status
        loan.save(update_fields=["outstanding", "status"])

    def get_payments_by_customer(self, customer_external_id):
        return (
            Payment.objects.filter(customer__external_id=customer_external_id)
            .annotate(customer_external_id=F("customer__external_id"))
            .prefetch_related("details")
        )

    def delete(self, payment_id):
        Payment.objects.filter(id=payment_id).delete()

    def update(self, payment_id, update_data):
        Payment.objects.filter(id=payment_id).update(**update_data)


class PaymentDetailRepository(AbstractPaymentDetailRepository):
    def add(self, payment_detail_data: PaymentDetailData) -> PaymentDetailData:
        payment_detail = PaymentDetail.objects.create(
            payment_id=payment_detail_data.payment_id,
            loan_id=payment_detail_data.loan_id,
            amount=payment_detail_data.amount,
        )
        return payment_detail

    def get_by_external_id(self, external_id: str) -> None:
        pass

    def update(self, entity: Any) -> None:
        pass

    def delete(self, external_id: str) -> None:
        pass

    def list_all(self) -> List[Any]:
        pass

    def get_payment_details_by_payment(self, payment_id: str) -> List[PaymentDetail]:
        pass

    def get_payment_details_by_customer(self, customer_external_id: str) -> List[PaymentDetail]:
        payment_details = (
            PaymentDetail.objects.filter(payment__customer__external_id=customer_external_id)
            .select_related("payment", "loan")
            .all()
        )
        return payment_details
