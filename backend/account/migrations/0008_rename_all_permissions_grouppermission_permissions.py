# Generated by Django 5.0 on 2024-05-07 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_allpermissions_pagegroup_grouppermission_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouppermission',
            old_name='all_permissions',
            new_name='permissions',
        ),
    ]
