from rest_framework.serializers import ModelSerializer
from blok.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
