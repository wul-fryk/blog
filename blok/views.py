from django.shortcuts import redirect, render
from .models import Article, Coment, User
from .forms import ComentFrom, UserForm, ArticleForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    stories = Article.objects.all()
    context = {'stories': stories}
    return render(request, 'blok/home.html', context)


def user_register(request):
    status = 'rejestruj'
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, 'Rejestracja zakończona niepowodzeniem.')
    context = {'user_form': user_form, 'status': status}
    return render(request, 'blok/login_register.html', context)


def user_login(request):
    status = 'login'

    if request.method == 'POST':
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')
        checker = False
        try:
            user = User.objects.get(username=user_username)
        except:
            checker = True

        user = authenticate(request, username=user_username,
                            password=user_password)

        if user is None or checker is True:
            messages.error(request, 'Nieprawidłowy login lub hasło.')

        else:
            login(request, user)
            return redirect('home')
    context = {'status': status}
    return render(request, 'blok/login_register.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request, pk):
    profile_owner = User.objects.get(id=pk)
    coments = profile_owner.coment_set.all()
    context = {'profile_owner': profile_owner, 'coments': coments}
    return render(request, 'blok\profile.html', context)


def article_page(request, pk):
    story = Article.objects.get(id=pk)
    coments = Coment.objects.all().order_by('-coment_publication')
    form = ComentFrom()
    if request.method == 'POST':
        Coment.objects.create(
            comented_article=story,
            coments_author=request.user,
            coment=request.POST.get('coment'),
        )
        return redirect('article', story.id)
    context = {'story': story, 'coments': coments, 'form': form}
    return render(request, 'blok/article.html', context)


def article_add(request):
    form = ArticleForm()
    if request.method == 'POST':
        new_article = Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.user
        )
        return redirect('article', new_article.id)
    return render(request, 'blok/add_article.html', {'form': form})
