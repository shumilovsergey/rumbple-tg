# Generated by Django 4.2.3 on 2023-08-15 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_logs_def_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='test',
            new_name='text',
        ),
    ]
