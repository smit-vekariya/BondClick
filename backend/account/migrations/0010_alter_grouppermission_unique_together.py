# Generated by Django 5.0 on 2024-05-09 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_bonduser_group_delete_usergroup'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grouppermission',
            unique_together={('group', 'permissions')},
        ),
    ]