from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Coment(models.Model):
    comented_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    coments_author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default='profl usunięty')
    coment = models.TextField()
    coment_publication = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.coment
