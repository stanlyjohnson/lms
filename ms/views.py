from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
        return render(request,template,{'authors':authors, 'aForm': auth_form, 'count':authors.count()})

    def post (self, request):
        context = {}
        template = 'ms/author.html'
        authForm = auth_form(data=request.POST)
        if authForm.is_valid():
            auth_app = authForm.save(commit=False)
            auth_app.save()
        authors = author.objects.all()
        return render(request,template,{'authors':authors,  'aForm': auth_form, 'count':authors.count()})

class Book(View):
    def get (self, request):
        context = {}
        template = 'ms/book.html'
        books = book.objects.all()
        return render(request,template,{'books':books, 'bForm': book_form, 'count':books.count()})

    def post (self, request):
        context = {}
        template = 'ms/book.html'
        bookForm = book_form(data = request.POST)
        if bookForm.is_valid():
            book_app = bookForm.save(commit = false)
            book_app.save()
        books = book.objects.all()
        return render(request,template,{'books':books, 'bForm': book_form, 'count':books.count()})
        pass

def authordetails (request):
    template = 'ms/authDetails.html'
    authId = request.GET.get('authorid')
    try:
        authDetails = author.objects.get (id = authId)
        bks = book.objects.filter(writtenby = authDetails)
        return render(request,template,{'authDetails':authDetails, 'books':bks})
    except :
        authDetails = author.objects.all().first()
        return HttpResponseRedirect('/welcome/authorDetails?authorid=%d'%(authDetails.id))



def bookdetails (request):
    template = 'ms/bookDetails.html'
    bookId = request.GET.get('bookid')
    try:
        bkDetails = book.objects.get (id = bookId)
        return render(request,template,{'bkDetails':bkDetails})
    except:
        bkDetails = book.objects.all().first()
        return HttpResponseRedirect('/welcome/bookDetails?bookid=%d'%(bkDetails.id))
