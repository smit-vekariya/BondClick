# Generated by Django 5.0 on 2024-05-31 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0004_alter_emaillog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillog',
            name='mail_bcc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='mail_cc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
