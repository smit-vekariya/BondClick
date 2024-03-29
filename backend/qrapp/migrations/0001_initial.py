# Generated by Django 5.0 on 2024-01-29 18:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BondUserWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('withdraw_point', models.IntegerField(blank=True, null=True)),
                ('withdraw_balance', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('tran_type', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=100)),
                ('point', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('tran_on', models.DateTimeField(auto_now=True)),
                ('tran_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qrapp.bonduserwallet')),
            ],
        ),
        migrations.CreateModel(
            name='WalletHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(blank=True, null=True)),
                ('action', models.TextField()),
                ('action_type', models.CharField(blank=True, choices=[('credit_point', 'Credit Point'), ('debit_point', 'Debit Point'), ('w_money', 'Withdraw Money'), ('error', 'Error')], max_length=100, null=True)),
                ('ip_addr', models.CharField(default='', max_length=45)),
                ('action_on', models.DateTimeField(auto_now=True)),
                ('action_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
            ],
        ),
    ]
