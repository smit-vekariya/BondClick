# Generated by Django 5.0 on 2024-06-04 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_commentquestions_commentanswars'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentAnswars',
            new_name='CommentAnswer',
        ),
    ]
