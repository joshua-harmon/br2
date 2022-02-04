import json
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from main.models import Post

def api(request):
    return HttpResponse("You're in an API Endpoint. Missing?")

def get_posts(request):
    posts = Post.objects.filter(archived=False)

    serialized_posts = serialize('json', posts)

    return JsonResponse(json.loads(serialized_posts), safe=False)