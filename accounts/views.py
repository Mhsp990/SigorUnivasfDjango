from django.shortcuts import render, redirect
#from .models import Produto
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.

def register(request):
    

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Uma conta foi criada para o usuário '+ user)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_page(request):
    #if request.user.is_authenticated:
    #   return redirect('home')
    #else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sistema')
        else:
            messages.info(request, 'Nome de usuário ou senha está incorretos.')
            
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'accounts/index.html')