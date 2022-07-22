from rest_framework.serializers import ModelSerializer
from blok.models import Article, Coment


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ComentsSerializers(ModelSerializer):
    class Meta:
        model = Coment
        fields = '__all__'
