# Generated by Django 5.0 on 2024-02-08 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_authotp'),
        ('qradmin', '0008_remove_qrbatch_is_used_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_limit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_point', models.IntegerField(blank=True, default=0, null=True)),
                ('total_user_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_user_point', models.IntegerField(blank=True, default=0, null=True)),
                ('total_withdraw_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_withdraw_point', models.IntegerField(blank=True, default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.company')),
            ],
        ),
    ]
