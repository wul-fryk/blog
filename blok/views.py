from django.shortcuts import redirect, render
from .models import Article,Coment
from .forms import ComentFrom, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    stories = Article.objects.all()
    context = {'stories':stories}
    return render(request, 'blok/home.html', context)

def article_page(request,pk):
    story = Article.objects.get(id=pk)
    coments = Coment.objects.all().order_by('-coment_publication')
    form = ComentFrom()
    if request.method == 'POST':
        Coment.objects.create(
            comented_article = story,
            coments_author = request.user,
            coment = request.POST.get('coment'),
        )
        return redirect('article', story.id)
    context = {'story':story, 'coments':coments,'form':form}
    return render(request, 'blok/article.html', context)

def user_register(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, 'Rejestracja zakończona niepowodzeniem.')
    context = {'user_form': user_form}
    return render(request, 'blok/login_register.html', context)
