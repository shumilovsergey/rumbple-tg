from django.db import models
from django.utils import timezone

class Chats(models.Model):
    chat_id = models.CharField(
        verbose_name="Telegram chat id", 
        primary_key=True,
        max_length=56, 
        unique=True
    )

    last_callback = models.CharField(
        verbose_name="Последний callback",
        max_length=56,
        default="none"
    )

    last_id = models.CharField(
        verbose_name="Последний callback ID",
        max_length=56,
        default="none"
    )
    
    def __str__(self):
        return self.chat_id
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Janras(models.Model):
    name = models.CharField(
        verbose_name="Название жанра", 
        max_length=56, 
    )  

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Artists(models.Model):
    name = models.CharField(
        verbose_name="Исполнитель", 
        max_length=56, 
    )

    janra = models.ForeignKey(
        Janras,
        on_delete= models.CASCADE
    )  

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

class Files(models.Model):

    name= models.CharField(
        verbose_name="Название", 
        max_length=56, 
        default="История без названия"
    )

    artist = models.ForeignKey(
        Artists,
        on_delete= models.CASCADE
    )

    tg_id = models.CharField(
        verbose_name="ID в телеграмме", 
        max_length=256, 
    )

    time_date = models.DateTimeField(
        verbose_name='Время и дата создания',
        default=timezone.now
    )

    moderator_id = models.CharField(
        verbose_name="id модератора", 
        max_length=56
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

class Moderators(models.Model):
    chat_id = models.CharField(
        verbose_name="Telegram chat id", 
        primary_key=True,
        max_length=56, 
        unique=True
    )

    name = models.CharField(
        verbose_name="ФИО модератора", 
        default="none",
        max_length=56, 
    )   

    last_callback = models.CharField(
        verbose_name="Последний callback",
        max_length=56,
        default="none"
    )

    last_id = models.CharField(
        verbose_name="Последний callback ID",
        max_length=56,
        default="none"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

