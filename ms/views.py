from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from ms.forms import *
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
            auth_app = authForm.save(commit=False)
            auth_app.save()
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
    authId = request.GET.get('authorid')
    try:
        authDetails = author.objects.get (id = authId)
        bks = book.objects.filter(writtenby = authDetails)
        return render(request,template,{'authDetails':authDetails, 'books':bks})
    except :
        return render(request,template,{'authDetails':{}, 'books':{}})



def bookdetails (request):
    template = 'ms/book_details.html'
    bookId = request.GET.get('bookid')
    try:
        bkDetails = book.objects.get (id = bookId)
        return render(request,template,{'bkDetails':bkDetails})
    except:
        return render(request,template,{'bkDetails':{}})
