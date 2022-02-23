from django.contrib import admin
from books.models import Book, Author

admin.site.register(Book)
# admin.site.register(Review)
admin.site.register(Author)