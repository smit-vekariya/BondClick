# Generated by Django 5.0 on 2024-05-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_grouppermission_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500)),
                ('value', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
    ]