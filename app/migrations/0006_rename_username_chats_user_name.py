# Generated by Django 4.2.3 on 2023-08-15 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_test_logs_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chats',
            old_name='username',
            new_name='user_name',
        ),
    ]
