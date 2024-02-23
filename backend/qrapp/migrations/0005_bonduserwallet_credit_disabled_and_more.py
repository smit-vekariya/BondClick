# Generated by Django 5.0 on 2024-02-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0004_transaction_total_amount_transaction_total_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonduserwallet',
            name='credit_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bonduserwallet',
            name='debit_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bonduserwallet',
            name='reason_disabled',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bonduserwallet',
            name='wallet_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
