"""
URL configuration for home_expenses project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls', namespace='expenses')),  # Adicionando o namespace
    path('login/', auth_views.LoginView.as_view(template_name='expenses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
