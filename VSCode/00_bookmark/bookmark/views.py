from django.shortcuts import render, get_object_or_404
from .models import Bookmark

# Create your views here.

def index(request):
    context = {
        'bookmark_list' : Bookmark.objects.all(),
    }
    return render(request,'bookmark/index.html', context)

def detail(request, bookmark_pk):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_pk)
    context = {
        'bookmark' : bookmark,
    }
    return render(request,'bookmark/detail.html', context)