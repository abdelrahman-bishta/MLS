from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *  # Import all models
from .forms import *
from django.shortcuts import redirect, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializer
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES) # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index view after saving the book
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect('index')
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formcat':CategoryForm(),
        'allbooks': Book.objects.all().count(),
        'rentedbooks': Book.objects.filter(status='rented').count(),
        'soldbooks': Book.objects.filter(status='sold').count(),
        'availablebooks': Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)
def books(request):
    searsh=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            searsh=Book.objects.filter(title__icontains=title)

    context = {
        'category': Category.objects.all(),
        'books': searsh,
        'formcat':CategoryForm(),
        
    }
    return render(request, 'pages/books.html', context)
def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        booksave = BookForm(request.POST, request.FILES, instance=book_id) # Include request.FILES to handle file uploads
        if booksave.is_valid():
            booksave.save()
            return redirect('/')  # Redirect to the index view after updating the book
    else:
        booksave = BookForm(instance=book_id)
    context = {
            'form': booksave,
            'category': Category.objects.all(),
        }
    return render(request, 'pages/update.html', context)
def delete(request, id):

    book_id = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Filters
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # فلترة مباشرة
    filterset_fields = ['title', 'author', 'status', 'category']

    # بحث
    search_fields = ['title', 'author','category']

    # ترتيب
    ordering_fields = ['price', 'pages', 'id']