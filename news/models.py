from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserRoles:
    USER = "user"
    ADMIN = "admin"
    CHOICES = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    role = models.CharField(
        max_length=9, choices=UserRoles.choices, default=UserRoles.USER)

    def is_admin(self):
        if self.role == UserRoles.ADMIN:
            return True
        return False


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               verbose_name="Автор", related_name='news')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Создан')

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Автор комментария',
                             on_delete=models.CASCADE)
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             )
    text = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.text
