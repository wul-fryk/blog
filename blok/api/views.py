from rest_framework.decorators import api_view
from rest_framework.response import Response
from blok.models import Article
from . serializers import ArticleSerializer


@api_view(['GET'])
def GetRoutes(request):
    routes = [
        'GET/api/articles',
        'GET/api/article/:id',
        'GET/api/articles-coments'
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
