# Generated by Django 5.0 on 2024-01-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonduserwallet',
            name='point',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bonduserwallet',
            name='withdraw_point',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]