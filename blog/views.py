from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'shihab',
        'book': 'Harry Potter',
        'price': '200 taka',
    },
    {
        'author': 'dipto',
        'book': 'Game Of Thrones',
        'price': '220 taka',
    }
]

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def post(request):
    return render(request, 'post.html', {'posts': posts, 'title': 'Posts'})

def about(request):
    return render(request, 'about.html')