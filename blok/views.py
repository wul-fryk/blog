from django.shortcuts import render
from .models import Article,Coment
from .forms import ComentFrom

# Create your views here.

def home(request):
    stories = Article.objects.all()
    context = {'stories':stories}
    return render(request, 'blok/home.html', context)

def article_page(request,pk):
    story = Article.objects.get(id=pk)
    coments = Coment.objects.all()
    form = ComentFrom()
    if request.method == 'POST':
        Coment.objects.create(
            comented_article = story,
            coments_author = request.user,
            coment = request.POST.get('coment'),

        )
    context = {'story':story, 'coments':coments,'form':form}
    return render(request, 'blok/article.html', context)