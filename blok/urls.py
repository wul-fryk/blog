from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<str:pk>', views.article_page, name='article'),

    path('register', views.user_register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile/<str:pk>', views.profile, name='profile'),


    path('add_article', views.article_add, name='add')
]
