from django import forms
from main.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

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