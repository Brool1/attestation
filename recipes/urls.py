from . import views
from django.contrib import admin
from django.urls import path, include
from .views import register

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', include('users.urls')),
    path('', register, name='register'), 
]

