# Generated by Django 4.2.3 on 2023-08-17 08:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_username_chats_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoJanras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56, verbose_name='Название жанра')),
            ],
            options={
                'verbose_name': 'Видео Жанр',
                'verbose_name_plural': 'Видео Жанры',
            },
        ),
        migrations.CreateModel(
            name='VideoFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Файл без названия', max_length=56, verbose_name='Название')),
                ('tg_id', models.CharField(max_length=256, verbose_name='ID в телеграмме')),
                ('time_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время и дата создания')),
                ('moderator_id', models.CharField(max_length=56, verbose_name='id модератора')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.artists')),
            ],
            options={
                'verbose_name': 'Видео Файл',
                'verbose_name_plural': 'Видео Файлы',
            },
        ),
        migrations.CreateModel(
            name='VideoArtists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56, verbose_name='Исполнитель')),
                ('janra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.janras')),
            ],
            options={
                'verbose_name': 'Видео Исполнитель',
                'verbose_name_plural': 'Видео Исполнители',
            },
        ),
    ]
