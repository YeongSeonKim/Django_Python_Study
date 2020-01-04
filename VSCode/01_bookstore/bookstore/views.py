from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def Bookstore_index(request):
    context = {
        'book_list' : Book.objects.all(),
    }
    return render(request, 'bookstore/bookstore_index.html', context)

def Bookstore_detail(request, bookstore_code):
    book = get_object_or_404(Book, code=bookstore_code)
    context = {
        'book' : book,
    }
    return render(request, 'bookstore/bookstore_detail.html', context)