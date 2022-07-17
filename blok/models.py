from turtle import title
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    # author =
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title