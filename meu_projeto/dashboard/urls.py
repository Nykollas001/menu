from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('notes/', views.notes, name='notes'),
    path('tier-lists/', views.tier_lists, name='tier_lists'),
    path('passwords/', views.passwords, name='passwords'),
    path('cards/', views.cards, name='cards'),
]
