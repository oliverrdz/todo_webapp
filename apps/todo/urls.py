from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('list_todo/', views.list_todo, name='list_todo'),
    path('edit/<int:id>', views.edit_todo, name="edit_todo"),
]