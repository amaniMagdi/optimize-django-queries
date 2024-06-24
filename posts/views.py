from django.shortcuts import render
from .models import Post, Auther

# Create your views here.
def main_view(request):
    data = []
    return render(request, "main.html", {"data":data})