# Generated by Django 5.0 on 2024-05-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_bonduser_group_remove_bonduser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]