from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetRoutes, name='routes'),
    path('articles', views.GetArticles, name='articles'),
]
