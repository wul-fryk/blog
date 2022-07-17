from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<str:pk>', views.article_page, name='article'),
]