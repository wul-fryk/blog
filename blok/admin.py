from atexit import register
import site
from django.contrib import admin
from .models import Article, Coment

# Register your models here.
admin.site.register(Article)
admin.site.register(Coment)