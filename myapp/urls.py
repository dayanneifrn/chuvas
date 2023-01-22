from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('listagem/', views.listagem, name='listagem'),
    path('consulta/', views.consulta, name='consulta'),
    path('crud/', views.crud, name='crud'),
    path('sobre/', views.sobre, name='sobre'),
]
