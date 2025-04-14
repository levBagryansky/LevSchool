from django.contrib import admin
from main.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title", "author")
