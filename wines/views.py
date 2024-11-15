from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Wine
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

class WineListView(ListView):
    model = Wine
    template_name = 'wine_list.html'

class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine_detail.html'

class WineCreateView(CreateView):
    model = Wine
    fields = ['name', 'price', 'type', 'vintage_year', 'region', 'description', 'rating', 'serving_temperature', 'Alcohol', 'Bottle_size', 'image']
    template_name = 'wine_form.html'
    success_url = reverse_lazy('wine-list')

class WineUpdateView(UpdateView):
    model = Wine
    fields = ['name', 'price', 'type', 'vintage_year', 'region', 'description', 'rating', 'serving_temperature', 'Alcohol', 'Bottle_size', 'image']
    template_name = 'wine_form.html'
    success_url = reverse_lazy('wine-list')

class WineDeleteView(DeleteView):
    model = Wine
    template_name = 'wine_confirm_delete.html'
    success_url = reverse_lazy('wine-list')

def get_similar_wines(wine):
    similar_wines = Wine.objects.filter(type=wine.type).exclude(id=wine.id)[:5]
    return similar_wines

def dashboard(request):
    total_wines = Wine.objects.count()
    recent_wines = Wine.objects.order_by('-id')[:5]
    top_rated_wines = Wine.objects.filter(rating__gte=4)
    wine_type_counts = {
        'red': Wine.objects.filter(type='Red').count(),
        'white': Wine.objects.filter(type='White').count(),
        'rose': Wine.objects.filter(type='Rose').count(),
    }
    
    average_ratings = {
        1: Wine.objects.filter(rating=1).count(),
        2: Wine.objects.filter(rating=2).count(),
        3: Wine.objects.filter(rating=3).count(),
        4: Wine.objects.filter(rating=4).count(),
        5: Wine.objects.filter(rating=5).count(),
    }

    context = {
        'total_wines': total_wines,
        'recent_wines': recent_wines,
        'top_rated_wines': top_rated_wines,
        'wine_type_counts': wine_type_counts,
        'average_ratings': average_ratings,
    }

    return render(request, 'dashboard.html', context)

def wine_list(request):
    wines = Wine.objects.all()
    return render(request, 'wine_list.html', {'wines': wines})

def home(request):
    return render(request, 'home.html')

def wine_detail(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    return render(request, 'wine_detail.html', {'wine': wine})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Error occurred during registration')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})

def logout_view(request):
    logout(request)
    return redirect('wine-list')
