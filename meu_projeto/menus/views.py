from django.shortcuts import render
from .models import Menu

def lista_menus(request):
    menus = Menu.objects.all()
    return render(request, 'menus/lista_menus.html', {'menus': menus})
