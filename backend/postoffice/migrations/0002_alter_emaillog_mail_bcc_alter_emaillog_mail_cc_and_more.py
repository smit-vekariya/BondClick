# Generated by Django 5.0 on 2024-05-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillog',
            name='mail_bcc',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='mail_cc',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='mail_subject',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='emaillog',
            name='mail_to',
            field=models.TextField(),
        ),
    ]
