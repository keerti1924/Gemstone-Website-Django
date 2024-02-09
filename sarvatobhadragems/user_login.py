from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from gems.emailbackend import EmailBackEnd
from gems.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login

@unauthenticated_user
def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already exists!')
            return redirect('register')
        
        #check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already exists!')
            return redirect('register')
        
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Registered Successfully!')
        return redirect('login')
    
    return render(request,'registration/register.html')


@unauthenticated_user
def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(request, username=email, password=password)

        if user != None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password are invalid !')
            return redirect('login')
        
    return render(request,'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')