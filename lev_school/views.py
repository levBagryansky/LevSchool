from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from main.models import Book
from main.forms import BookForm
from main.forms import RegisterForm

def home(request):
    return render(request, "home.html")

def book_list(request):
    list = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': list})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # логин сразу после регистрации
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

