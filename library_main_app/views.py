from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Books,Readers,Donor
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


@login_required(login_url='login')
def add_books(request):
    if request.method == 'POST':

        isbn_num = request.POST['ISBN_NUM']
        books_name= request.POST['BOOKS_NAME']
        authors = request.POST['AUTHORS']
        availabel_copies= request.POST['AVAILABLE_COPIES']

        isbn_num=isbn_num.upper()
        books_name=books_name.upper()
        authors=authors.upper()

        if isbn_num=='' or books_name=='' or authors=='' or availabel_copies=='':
            message="Please input data in the fields"
            return render(request,'add_books.html',{"message":message})
        else:
            if Books.objects.filter(ISBN_NUM=isbn_num).exists():
                book=Books.objects.get(ISBN_NUM=isbn_num)
                book.AVAILABLE_COPIES+=int(availabel_copies)
                book.save()
                message= "Aready has the book so updated the Available Copies !!"
            else:
                book=Books.objects.create(ISBN_NUM=isbn_num,BOOKS_NAME=books_name,AUTHORS=authors,AVAILABLE_COPIES=availabel_copies)
                book.save()
                message="Book added successfully !!"

            return render(request,'add_books.html',{"message":message}) 
     
    else:
        return render(request,'add_books.html')

 
@login_required(login_url='login')
def display_books(request):
    b=Books.objects.all()

    query = request.GET.get('q')
    if query:
        qb = b.filter(BOOKS_NAME__contains=query)
        return render(request,'display_book.html',{"books":qb})
    else:
        return render(request,'display_book.html', {"books":b})



@login_required(login_url='login')
def borrow(request,pk):
    Book = Books.objects.get(id=pk)

    if request.method == 'POST':
        READERS_ID = request.POST['READERS_ID']
        READERS_NAME = request.POST['READERS_NAME']

        Book.AVAILABLE_COPIES-=1
        Book.save()
        reader = Readers(READERS_ID = READERS_ID,READERS_NAME= READERS_NAME,Book = Book)
        reader.save()
        msg = "Readers got the book succesfully"

        return HttpResponseRedirect(reverse(display_readers))
        
    else:
        return render(request,"borrow.html",{"book":Book})



@login_required(login_url='login')
def display_readers(request):
    readers = Readers.objects.all()
    return render(request,"display_readers.html",{"readers":readers})




@login_required(login_url='login')
def donate_books(request):
    if request.method == 'POST':

        # Book info
        isbn_num = request.POST['ISBN_NUM']
        books_name= request.POST['BOOKS_NAME']
        authors = request.POST['AUTHORS']
        copies = request.POST['COPIES']

        #Donor Info
        donors_id = request.POST['DONORS_ID']
        donors_name = request.POST['DONORS_NAME']


        isbn_num=isbn_num.upper()
        books_name=books_name.upper()
        authors=authors.upper()

        #if donated book already exist in the library
        if Books.objects.filter(ISBN_NUM=isbn_num).exists():
            book=Books.objects.get(ISBN_NUM=isbn_num)
            book.AVAILABLE_COPIES+=int(copies)
            book.save()
        else:
            book=Books.objects.create(ISBN_NUM=isbn_num,BOOKS_NAME=books_name,AUTHORS=authors,AVAILABLE_COPIES=copies)
            book.save()


        donor = Donor(DONOR_NAME=donors_name,DONOR_ID=donors_id,HOW_MANY_COPIES=copies,Book=book)
        donor.save() 
        message = "added success"
        return render(request,'add_books.html',{"message":message}) 

    else:
        return render(request,"donate_books.html")





@login_required(login_url='login')
def display_donors(request):
    donor = Donor.objects.all()

    return render(request,"display_donors.html",{"donor":donor})
