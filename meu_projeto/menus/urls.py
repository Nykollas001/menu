from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_menus, name='lista_menus'),
]
