from django.http import JsonResponse


def GetRoutes(request):
    routes = [
        'GET/api/articles',
        'GET/api/articles-coments'
    ]

    return JsonResponse(routes, safe=False)
