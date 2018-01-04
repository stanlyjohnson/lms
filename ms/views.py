from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import auth_form, book_form
# Create your views here.
def welcome (request):
    template='ms/home.html'
    return render(request,template,{})

class Author(View):
    def get (self, request):
        context = {}
        template = 'ms/author.html'
        authors = author.objects.all()
        return render(request,template,{'authors':authors, 'aForm': auth_form})

    def post (self, request):
        context = {}
        template = 'ms/author.html'
        authForm = auth_form(data=request.POST)
        if authForm.is_valid():
            auth_app = authForm.save()
        authors = author.objects.all()
        return render(request,template,{'authors':authors,  'aForm': auth_form})

class Book(View):
    def get (self, request):
        context = {}
        template = 'ms/book.html'
        books = book.objects.all()
        return render(request,template,{'books':books, 'bForm': book_form})

    def post (self, request):
        context = {}
        template = 'ms/book.html'
        data=request.POST
        n = data.pop('name')
        bookForm = book_form(data= data)
        if bookForm.is_valid():
            book_app = bookForm.save(commit = false)
            # n = book_app.name
            book_app.writtenby = author.objects.get(name = n)
            book_app.save()
        books = book.objects.all()
        return render(request,template,{'books':books, 'bForm': book_form})
        pass

def authordetails (request):
    template = 'ms/auth_details.html'
    authName = request.GET.get('author')
    authDetails = author.objects.get (name = authName)
    return render(request,template,{'authDetails':authDetails})

def bookdetails (request):
    template = 'ms/book_details.html'
    bookName = request.GET.get('book')
    bkDetails = book.GET.get (title = bookName)
    return render(request,template,{'bkDetails':bkDetails})
