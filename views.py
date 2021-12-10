from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'enroll/index.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        my_user = User.objects.create_user(username, email, pass1)
        my_user.save()
        messages.success(request, 'Your account has been successfully created.')
        return redirect('signin')

    return render(request, 'enroll/register.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'enroll/index.html', {'username' : username})
        else:
            messages.error(request, 'Wrong username or password!')
            return redirect('home')

    return render(request, 'enroll/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')
