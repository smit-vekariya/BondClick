# Generated by Django 5.0 on 2024-05-22 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_mainmenu_code'),
        ('manager', '0007_alter_allpermissions_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpermissions',
            name='page_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.mainmenu'),
        ),
        migrations.AlterUniqueTogether(
            name='allpermissions',
            unique_together={('page_name', 'act_code')},
        ),
    ]