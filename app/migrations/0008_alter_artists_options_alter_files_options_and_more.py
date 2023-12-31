# Generated by Django 4.2.3 on 2023-08-17 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_videojanras_videofiles_videoartists'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artists',
            options={'verbose_name': 'Аудио Исполнитель', 'verbose_name_plural': 'Аудио Исполнители'},
        ),
        migrations.AlterModelOptions(
            name='files',
            options={'verbose_name': 'Аудио Файл', 'verbose_name_plural': 'Аудио Файлы'},
        ),
        migrations.AlterModelOptions(
            name='janras',
            options={'verbose_name': 'Аудио Жанр', 'verbose_name_plural': 'Аудио Жанры'},
        ),
        migrations.AlterField(
            model_name='videoartists',
            name='janra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.videojanras'),
        ),
        migrations.AlterField(
            model_name='videofiles',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.videoartists'),
        ),
    ]
