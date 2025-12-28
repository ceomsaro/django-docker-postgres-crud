from django.contrib import admin
from .models import Author, Book
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['birthdate']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['published', 'author']