# Generated by Django 4.2.3 on 2023-08-15 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_foreign_key_artists_janra_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('def_name', models.CharField(max_length=56, verbose_name='Имя аккаунта TG')),
                ('time_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время и дата')),
                ('test', models.TextField(verbose_name='текст логов')),
            ],
            options={
                'verbose_name': 'Логи',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
