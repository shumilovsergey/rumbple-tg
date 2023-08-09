# Generated by Django 4.2.3 on 2023-08-08 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_files_options_alter_chats_last_callback_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='last_callback',
        ),
        migrations.RemoveField(
            model_name='chats',
            name='last_id',
        ),
        migrations.AddField(
            model_name='chats',
            name='first_name',
            field=models.CharField(default='Нет информации', max_length=56, verbose_name='Имя пользователя'),
        ),
        migrations.AddField(
            model_name='chats',
            name='last_name',
            field=models.CharField(default='Нет информации', max_length=56, verbose_name='Фамилия пользователя'),
        ),
        migrations.AddField(
            model_name='chats',
            name='time_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время и дата первого запроса'),
        ),
        migrations.AddField(
            model_name='chats',
            name='username',
            field=models.CharField(default='Нет информации', max_length=56, verbose_name='Имя аккаунта TG'),
        ),
        migrations.AddField(
            model_name='moderators',
            name='first_name',
            field=models.CharField(default='Нет информации', max_length=56, verbose_name='Имя пользователя'),
        ),
        migrations.AddField(
            model_name='moderators',
            name='last_name',
            field=models.CharField(default='Нет информации', max_length=56, verbose_name='Фамилия пользователя'),
        ),
        migrations.AddField(
            model_name='moderators',
            name='time_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время и дата первого запроса'),
        ),
        migrations.AddField(
            model_name='moderators',
            name='username',
            field=models.CharField(default='Нет информации', max_length=56, verbose_name='Имя аккаунта TG'),
        ),
    ]