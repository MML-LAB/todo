from django.shortcuts import render, HttpResponse, redirect
from .models import *

def homepage(request):
    return render(request, 'index.html')

def books(request):
    bshop_list = BookShop.objects.all()
    return render(request, 'books.html', {"bshop_list" : bshop_list})

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list" : todo_list})

def add(request):
    # form = request.POST
    # text = form["todo_text"]
    # todo = ToDo(text=text)
    # todo.save()
    # return redirect(test)

    bform = request.POST
    btext = bform["name_book"]
    s_text = bform["sub_name"]
    b_descr = bform["descr"]
    b_price = bform["price_book"]
    b_genre = bform["genre"]
    b_autor = bform["auth"]
    b_create = bform["cr_date"]
    books = BookShop(btext=title, s_text=subtitle, b_descr=description, b_price=price, b_genre=genre, b_autor=author, b_create=year )
    books.save()
    return redirect(books)
    
def edit(request):
    return render(request, 'edit.html')
    
def delete(request):
    return render(request, 'delete.html')