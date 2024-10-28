from django.contrib import admin
from . models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_ad', 'isbn', 'count_page', 'language')