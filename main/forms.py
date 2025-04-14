from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
        labels = {
            'title': 'Название произведения',
            'author': 'Автор',
            'description': 'Краткое описание (необязательно)',
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Например, «Война и мир»'
        })
        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Лев Толстой'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Добавьте описание или оставьте пустым'
        })

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')

        if title and author:
            existing = Book.objects.filter(title__iexact=title.strip(), author__iexact=author.strip())
            if existing.exists():
                raise forms.ValidationError("Такое произведение уже есть в базе 🛑")


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

    def clean_password1(self):
        # просто возвращаем пароль — без проверки сложности
        return self.cleaned_data.get("password1")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2
