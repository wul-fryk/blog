from django.forms import ModelForm
from .models import Coment


class ComentFrom(ModelForm):
    class Meta:
        model = Coment
        fields = '__all__'
        exclude = ['comented_article', 'coments_author']