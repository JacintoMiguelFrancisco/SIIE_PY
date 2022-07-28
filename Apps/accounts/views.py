"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.views import generic

# Models
# from django.contrib.auth.models import User

# Forms 
from .forms import SignupForm, ProfileForm

# Create your views here.

#Actualizar perfil
@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

#Inicio de sesion
def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
             #REDIRECCIONA A UNA URL
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Usuario ó contraseña invalidos'})

    return render(request, 'registration/login.html')

#Registrate
@login_required
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request=request, template_name='registration/signup.html', context={'form': form})

#Cerrar sesion
@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')