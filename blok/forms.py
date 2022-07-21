from django.forms import ModelForm
from .models import Coment, Article
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class ComentFrom(ModelForm):
    class Meta:
        model = Coment
        fields = '__all__'
        exclude = ['comented_article', 'coments_author']
