from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note, TierList, Password, Card
from django.db.models import Count

# Create your views here.

@login_required
def dashboard(request):
    # Contagem de itens
    notes_count = Note.objects.filter(user=request.user).count()
    tierlists_count = TierList.objects.filter(user=request.user).count()
    passwords_count = Password.objects.filter(user=request.user).count()
    cards_count = Card.objects.filter(user=request.user).count()
    
    # Últimas notas
    latest_notes = Note.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    context = {
        'notes_count': notes_count,
        'tierlists_count': tierlists_count,
        'passwords_count': passwords_count,
        'cards_count': cards_count,
        'latest_notes': latest_notes,
        'user': request.user
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'dashboard/notes.html', {'notes': notes})

@login_required
def tier_lists(request):
    tier_lists = TierList.objects.filter(user=request.user)
    return render(request, 'dashboard/tier_lists.html', {'tier_lists': tier_lists})

@login_required
def passwords(request):
    passwords = Password.objects.filter(user=request.user)
    return render(request, 'dashboard/passwords.html', {'passwords': passwords})

@login_required
def cards(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'dashboard/cards.html', {'cards': cards})
