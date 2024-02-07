# Generated by Django 5.0 on 2024-02-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0002_alter_bonduserwallet_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonduserwallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='bonduserwallet',
            name='withdraw_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='point',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]