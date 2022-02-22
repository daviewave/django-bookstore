from django.shortcuts import render
import json

books_data = open('/Users/dsilveira/Desktop/python-venv-4.2.0/Bookstore-Project/books.json').read()
data = json.loads(books_data)

def index(request):
    context = {'books':data}
    return render(request, 'books/index.html', context)

def show(request, id):
    singleBook = list()
    for book  in data:
        if book['id'] == id:
            singleBook = book
    context = {'book':singleBook}
    return render(request, 'books/show.html', context)