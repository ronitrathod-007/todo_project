from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTo, name ='add'),
    path('complete/<todo_id>', views.complete, name='complete'),
    path('delete_comp/', views.delete_comp, name='delete_comp'),
    path('delete_all/', views.delete_all, name= 'delete_all')


]