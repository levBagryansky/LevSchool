from django import forms
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
