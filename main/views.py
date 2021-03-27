from django.shortcuts import render, HttpResponse
from .models import ToDo, BookShop

def homepage(request):
    return render(request, 'index.html')

def books(request):
    bshop_list = BookShop.objects.all()
    return render(request, 'books.html', {"bshop_list" : bshop_list})


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list" : todo_list})

def add(request):
    return render(request, 'add.html')
    
def edit(request):
    return render(request, 'edit.html')
    
def delete(request):
    return render(request, 'delete.html')