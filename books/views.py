from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

from books.models import Book, Review

# GENERIC VIEWS #
class BookListView(ListView):
    # template_name = 'books/index.html'
    # context_object_name = 'books'
    # login_url = '/login/'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
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

def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)

def review(request, id):
    print(request.user)
    if request.user.is_authenticated:
        image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(image.name, image)

        body = request.POST['review']
        new_review = Review(body=body, book_id=id, user=request.user, image=fs.url(name))
        new_review.save()
    return redirect('/book')
    
   