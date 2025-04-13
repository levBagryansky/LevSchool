from django.shortcuts import render, redirect
from django.core.cache import cache
from main.models import Book
from main.forms import BookForm


# from . import terms_work


def home(request):
    return render(request, "home.html")

def book_list(request):
    list = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': list})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
