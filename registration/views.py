
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        confpass = request.POST['confpass']

        if password == confpass:
            if User.objects.filter(username = username).exists():
                print("username taken")
            else:
                user = User.objects.create_user(username, password)

                user.save()
                print("yep")
        else:
            print("nop")

        

        return redirect('signin')

    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request, "loggedin.html")
        else:
            return redirect('index')

    return render(request, 'signin.html')

def loggedin(request):
    return render(request, 'loggedin.html')