from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Notas (Grades)
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/create/', views.grade_create, name='grade_create'),
    path('grades/<int:pk>/edit/', views.grade_edit, name='grade_edit'),
    path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),
    
    # Tier Lists
    path('tierlists/', views.tierlist_list, name='tierlist_list'),
    path('tierlists/create/', views.tierlist_create, name='tierlist_create'),
    path('tierlists/<int:pk>/', views.tierlist_detail, name='tierlist_detail'),
    path('tierlists/<int:pk>/edit/', views.tierlist_edit, name='tierlist_edit'),
    path('tierlists/<int:pk>/delete/', views.tierlist_delete, name='tierlist_delete'),
    
    # Tier Items
    path('tieritems/create/<int:tierlist_id>/', views.tieritem_create, name='tieritem_create'),
    path('tieritems/<int:pk>/edit/', views.tieritem_edit, name='tieritem_edit'),
    path('tieritems/<int:pk>/delete/', views.tieritem_delete, name='tieritem_delete'),
    
    # Diário
    path('diary/', views.diary_list, name='diary_list'),
    path('diary/add/', views.diary_create, name='diary_create'),
    path('diary/<int:pk>/delete/', views.diary_delete, name='diary_delete'),
    
    # Senhas
    path('passwords/', views.password_list, name='password_list'),
    path('passwords/add/', views.password_create, name='password_create'),
    
    # Cartas
    path('cards/', views.draw_card, name='draw_card'),
]
