# Generated by Django 5.0.7 on 2024-09-12 05:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('UZS', 'Uzbekistani Som'), ('EUR', 'Euro')], default='UZS', max_length=3)),
                ('payment_type', models.CharField(choices=[('LOAN_REPAYMENT', 'Loan Repayment'), ('INSTALLMENT_PAYMENT', 'Installment Payment'), ('INTEREST_PAYMENT', 'Interest Payment'), ('PRINCIPAL_PAYMENT', 'Principal Payment'), ('PENALTY_PAYMENT', 'Penalty Payment'), ('ADVANCE_PAYMENT', 'Advance Payment'), ('REFUND', 'Refund'), ('RESTRUCTURED_PAYMENT', 'Restructured Payment')], max_length=32)),
                ('payment_method', models.CharField(choices=[('CASH', 'Cash'), ('BANK_TRANSFER', 'Bank Transfer'), ('MOBILE_MONEY', 'Mobile Money'), ('POS', 'POS Terminal'), ('ONLINE_PAYMENT', 'Online Payment')], max_length=32)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('reference_number', models.CharField(max_length=128, unique=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_payments', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='clients.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PaymentSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField()),
                ('installment_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('is_paid', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='payments.payment')),
            ],
            options={
                'verbose_name': 'Payment Schedule',
                'verbose_name_plural': 'Payment Schedules',
                'ordering': ['due_date'],
            },
        ),
    ]
