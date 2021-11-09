from django.contrib import admin
from django.urls import path
from noteapp import views 

urlpatterns = [
    path('', views.home , name='home'),
    path('add/', views.add_notes ,name='add_notes'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('edit/<int:note_id>', views.edit , name='edit')
]