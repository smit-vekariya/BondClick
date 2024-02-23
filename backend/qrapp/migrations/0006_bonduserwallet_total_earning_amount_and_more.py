# Generated by Django 5.0 on 2024-02-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0005_bonduserwallet_credit_disabled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonduserwallet',
            name='total_earning_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='bonduserwallet',
            name='total_earning_point',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
