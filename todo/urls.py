from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('test/', test, name = 'test'),
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('delete-todo/<id>/', delete_todo, name='delete-todo'),
    path('books/', books, name='books'),
]   + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


