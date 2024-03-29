# Generated by Django 5.0 on 2024-02-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qradmin', '0009_companywallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrbatch',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='qrbatch',
            name='total_used_qr_code',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
