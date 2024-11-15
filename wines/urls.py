# In wines/urls.py
from django.urls import path
from .views import WineListView, WineDetailView, WineCreateView, WineUpdateView, WineDeleteView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', WineListView.as_view(), name='wine-list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('wine/<int:pk>/', WineDetailView.as_view(), name='wine-detail'),
    path('wine/new/', WineCreateView.as_view(), name='wine-create'),
    path('wine/<int:pk>/edit/', WineUpdateView.as_view(), name='wine-update'),
    path('wine/<int:pk>/delete/', WineDeleteView.as_view(), name='wine-delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
