from django.db import models
from django.utils import timezone

class Chats(models.Model):
    chat_id = models.CharField(
        verbose_name="Telegram chat id", 
        primary_key=True,
        max_length=56, 
        unique=True
    )

    first_name = models.CharField(
        verbose_name="Имя пользователя", 
        default= "Нет информации",
        max_length=56,
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя", 
        default= "Нет информации",
        max_length=56,
    )

    user_name = models.CharField(
        verbose_name="Имя аккаунта TG", 
        default= "Нет информации",
        max_length=56,
    )

    time_date = models.DateTimeField(
        verbose_name='Время и дата первого запроса',
        default=timezone.now
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
        default="Файл без названия"
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
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

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
        default= {"callback":"none"}
    )

    last_id = models.CharField(
        verbose_name="Последний callback ID",
        max_length=56,
        default= {"callback":"none"}
    )

    first_name = models.CharField(
        verbose_name="Имя пользователя", 
        default= "Нет информации",
        max_length=56,
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя", 
        default= "Нет информации",
        max_length=56,
    )

    username = models.CharField(
        verbose_name="Имя аккаунта TG", 
        default= "Нет информации",
        max_length=56,
    )

    time_date = models.DateTimeField(
        verbose_name='Время и дата первого запроса',
        default=timezone.now
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

class Logs(models.Model):
    def_name = models.CharField(
        verbose_name="Имя функции",
        max_length=56,
    )

    time_date = models.DateTimeField(
        verbose_name='Время и дата',
        default=timezone.now
    )

    text = models.TextField(
        verbose_name="текст логов"
    )


    def __str__(self):
        return self.def_name
    
    class Meta:
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'