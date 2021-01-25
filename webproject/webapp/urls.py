
from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.deshboard, name='home'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('list_person/', views.list_person, name='list_person'),
    path('imageEdit/<int:id>', views.imageEdit, name='/imageEdit'),
]
