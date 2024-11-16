from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm, UserUpdateForm
from .models import User

def home(request):
    return render(request, 'home.html', context={})

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, 'login.html')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:       
            messages.error(request, "Email or Password does not exist.")        
    return render(request, 'login.html', context={'page':'login'})

def userLogout(request):
    logout(request)
    return redirect('home')

def userSignup(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
        except Exception as e:
            messages.error(request, f'{e}')
    return render(request, 'signup.html', context={'form':form})

@ login_required(login_url='login')
def userUpdate(request):
    form = UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        try:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'Profile updated.')
                return redirect('user-profile')
        except Exception as e:
            messages.error(request,f'{e}')
    return render(request, 'user_update.html',  context={'form':form})

@ login_required(login_url='login')
def userProfile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'user_profile.html', context={'user':user})
