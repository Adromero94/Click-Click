from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse

from .models import CommentSection

# Create your views here.

def index(request):
    # return JsonResponse('Yesir', safe=False)
    return render(request, 'clickapp/index.html', context={}, status=200)

def comment_list():
    query = CommentSection.objects.all()
    comments = [{"id": x.id, "body": x.body} for x in query]
    data = {
        "response": comments
    }
    return JsonResponse(data)

def comment_view(request, comment_id, *args, **kwargs):
    print(args, kwargs)
    obj = CommentSection.objects.get(id=comment_id)

    data = {
        "id": comment_id,
        "body": obj.body,
    }
    return JsonResponse(data)