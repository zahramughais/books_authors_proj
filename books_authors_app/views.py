from ast import Return
from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from .models import *

def index(request):
    books = Book.objects.all()
    context ={
        'books':books
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.method == 'POST':
        addedBook = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
        )
        addedBook.save()
    return redirect('/')

def book_dis(request, id):
    book = Book.objects.get(id=id)
    authors = book.authors.all()
    all_authors = Author.objects.exclude(books = book)
    context = {
        'book': book,
        'authors': authors,
        'all_authors':all_authors,
    }
    return render(request, "book.html", context)

def add_aurthor_to(request, id):
    book = Book.objects.get(id=id)
    author_val = Author.objects.get(id = request.POST['sel_author'])
    book.authors.add(author_val)
    return redirect('book_page', id=id)

def auth_index(request):
    authors = Author.objects.all()
    context ={
        'authors':authors
    }
    return render(request, "index2.html", context)

def add_author(request):
    if request.method == 'POST':
        addedAuthor = Author.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            notes=request.POST['notes']
        )
        addedAuthor.save()
    return redirect('/authors')

def author_dis(request,id):
    author = Author.objects.get(id=id)
    books = author.books.all()
    all_books = Book.objects.exclude(authors = author)
    context = {
        'author': author,
        'books': books,
        'all_books':all_books,
    }
    return render(request, "author.html", context)

def add_book_to(request, id):
    author = Author.objects.get(id=id)
    book_val = Book.objects.get(id = request.POST['sel_book'])
    author.books.add(book_val)
    return redirect('author_page', id=id)