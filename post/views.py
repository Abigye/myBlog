from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . models import Article
from . serializers import ArticleSerializers

# Create your views here.

# All Post View
def all_post(request):
    posts = Article.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

# Post Detail View 
def post_detail(request, id):
    post = get_object_or_404(Article, id = id)
    return render(request, 'post/post_detail.html', {'post':post})


def all_post_api(request):
    posts = Article.objects.all()
    data = serializers.serialize('json',posts)
    return HttpResponse(data, content_type = 'application/json')


# On the above code first we have imported the serializing object, which will allow us
#  to serialize all the data that we have in our database to JSON objects.
# decorator csrf_exempt, what it does is exempting the csrf token when someone send
#  a post request on the url
@csrf_exempt  
def article_list(request):
    
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializers(article, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(request)
        print(data)
        serializer = ArticleSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
