from django.contrib import admin
from books.models import Book, Review

admin.site.register(Book)
admin.site.register(Review)