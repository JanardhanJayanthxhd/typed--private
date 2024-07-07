from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registration complete. You're now logged in.")
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'members/register.html',
                  {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.success(request, 'Invalid credentials')
            return redirect('login_user')
    return render(request, 'members/login.html',
                  {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')
