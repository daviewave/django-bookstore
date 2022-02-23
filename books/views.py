from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from books.models import Book, Review

# GENERIC VIEWS #
class BookListView(ListView):
    # template_name = 'books/index.html'
    # context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        return context

# VIEWS #
# def index(request):
#     dbData = Book.objects.all()
#     context = {'books':dbData}
#     return render(request, 'books/index.html', context)

# def show(request, id):
#     singleBook = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-id')
#     context = {'book':singleBook, 'reviews':reviews}
#     return render(request, 'books/show.html', context)

def review(request, id):
    body = request.POST['review']
    new_review = Review(body=body, book_id=id)
    new_review.save()
    return redirect('/book')
   