from rest_framework.decorators import api_view
from rest_framework.response import Response
from blok.models import Article, Coment
from . serializers import ArticleSerializer, ComentsSerializers


@api_view(['GET'])
def GetRoutes(request):
    routes = [
        'GET/api/articles',
        'GET/api/article/:id',
        'GET/api/articles-coments/:id'
    ]

    return Response(routes)


@api_view(['GET'])
def GetArticles(request):
    articles = Article.objects.all()
    serialized = ArticleSerializer(articles, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def GetArticle(request, pk):
    articles = Article.objects.get(id=pk)
    serialized = ArticleSerializer(articles, many=False)
    return Response(serialized.data)


@api_view(['GET'])
def GetComents(request, pk):
    article = Article.objects.get(id=pk)
    coments = article.coment_set.all()
    serialized = ComentsSerializers(coments, many=True)
    return Response(serialized.data)
