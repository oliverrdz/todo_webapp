from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_todo/', views.new_todo, name='new_todo'),
]