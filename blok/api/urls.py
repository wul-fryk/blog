from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetRoutes),
    path('articles', views.GetArticles),
    path('article/<str:pk>', views.GetArticle),
    path('articles-coments/<str:pk>', views.GetComents)
]
