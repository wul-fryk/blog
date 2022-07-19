from django.forms import ModelForm
from .models import Coment
from django.contrib.auth.models import User

class ComentFrom(ModelForm):
    class Meta:
        model = Coment
        fields = '__all__'
        exclude = ['comented_article', 'coments_author']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']