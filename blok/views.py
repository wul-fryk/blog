from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    stories = Article.objects.all()
    context = {'stories':stories}
    return render(request, 'blok/home.html', context)

def article_page(request,pk):
    story = Article.objects.get(id=pk)
    context = {'story':story}
    return render(request, 'blok/article.html', context)