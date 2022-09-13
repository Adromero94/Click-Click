import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import CustomUserCreationForm
from .models import CommentSection

# Create your views here.

def index(request):
    # return JsonResponse('Yesir', safe=False)
    return render(request, 'clickapp/index.html', context={}, status=200)

def comment_list(request, *args, **kwargs):
    query = CommentSection.objects.all()
    comments = [{"id": x.id, "body": x.body, "likes": random.randint(0, 1234567890)} for x in query]
    data = {
        "isUser": False,
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


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["email"]} registered successfully!')

    context = {
        'form': form
    }
    return render(request, 'clickapp/register.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in as {request.user.username}')
        return redirect('clickapp/index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'User {user.username} logged in successfully!')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('clickapp/index')
        else:
            messages.warning(request, 'could not authenticate, check credintials.')

    return render(request, 'clickapp/login.html', context={"username": username})


def logout(request):
    context = {}
    return redirect('clickapp:login')