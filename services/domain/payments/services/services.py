# Django
from django.db import transaction

# Internal
from services.django_apps.customers.adapters.repository import (
    CustomerRepository,
)
from services.django_apps.loans.adapters.repository import LoanRepository
from services.django_apps.payments.adapters.repository import (
    PaymentDetailRepository,
    PaymentRepository,
)
from services.domain.payments.models import PaymentData, PaymentDetailData
from services.domain.payments.services.base import AbstractServicePayment
from services.domain.payments.specifications import (
    CustomerHasActiveLoansSpecification,
    PaymentDoesNotExceedDebtSpecification,
)


class PaymentService(AbstractServicePayment):
    def __init__(
        self,
        payment_repository: PaymentRepository,
        payment_detail_repository: PaymentDetailRepository,
        loan_repository: LoanRepository,
        customer_repository: CustomerRepository,
    ):
        self.payment_repository = payment_repository
        self.payment_detail_repository = payment_detail_repository
        self.loan_repository = loan_repository
        self.customer_repository = customer_repository
        self.active_loans_spec = CustomerHasActiveLoansSpecification(loan_repository)
        self.payment_exceeds_debt_spec = PaymentDoesNotExceedDebtSpecification(loan_repository)

    @transaction.atomic
    def create_payment(self, payment_data: PaymentData) -> PaymentData:

        self.active_loans_spec.is_satisfied_by(payment_data.customer_external_id)
        self.payment_exceeds_debt_spec.is_satisfied_by(payment_data)

        customer = self.customer_repository.get_by_external_id(payment_data.customer_external_id)
        payment_data.customer_id = customer.id
        payment = self.payment_repository.add(payment_data)

        active_loans = self.loan_repository.get_active_loans_by_customer(
            payment_data.customer_external_id
        )
        remaining_payment_amount = payment_data.total_amount

        for loan in active_loans:
            if remaining_payment_amount <= 0:
                break
            payment_amount = min(loan.outstanding, remaining_payment_amount)

            self.loan_repository.update_loan_payment(loan.id, payment_amount)

            payment_detail_data = PaymentDetailData(
                payment_id=payment.id, loan_id=loan.id, amount=payment_amount
            )
            self.payment_detail_repository.add(payment_detail_data)

            remaining_payment_amount -= payment_amount

        return payment

    def get_payments_by_customer(self, customer_external_id):
        payments = self.payment_repository.get_payments_by_customer(customer_external_id)
        return payments

    def get_payment_details_by_customer(self, customer_external_id):
        payments_details = self.payment_detail_repository.get_payment_details_by_customer(
            customer_external_id
        )
        return payments_details
