# Generated by Django 4.2.13 on 2024-05-17 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_allpermissions_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='allpermissions',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='allpermissions',
            name='page_group',
        ),
        migrations.AlterUniqueTogether(
            name='grouppermission',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='grouppermission',
            name='group',
        ),
        migrations.RemoveField(
            model_name='grouppermission',
            name='permissions',
        ),
        migrations.DeleteModel(
            name='SystemParameter',
        ),
        migrations.DeleteModel(
            name='AllPermissions',
        ),
        migrations.DeleteModel(
            name='GroupPermission',
        ),
        migrations.DeleteModel(
            name='PageGroup',
        ),
    ]
