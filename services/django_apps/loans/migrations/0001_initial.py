# Generated by Django 4.0.10 on 2024-02-05 05:35

from django.db import migrations, models
import django.db.models.deletion
import services.domain.loans.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('external_id', models.CharField(max_length=60, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.SmallIntegerField(choices=[(1, 'PENDING'), (2, 'ACTIVE'), (3, 'REJECTED'), (4, 'PAID')], default=services.domain.loans.constants.LoanStatus['ACTIVE'])),
                ('contract_version', models.CharField(blank=True, max_length=30, null=True)),
                ('maximum_payment_date', models.DateTimeField(blank=True, null=True)),
                ('taken_at', models.DateTimeField(auto_now=True, null=True)),
                ('outstanding', models.DecimalField(decimal_places=2, max_digits=12)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='customers.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]