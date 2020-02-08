from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username,password=password)
    if user is not None:
        login(request,user)
        else:
            return HttpResponse('0')

    def signup(request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,email,password)
        user=authenticate(username=username,password=password)
        if user is None:
            login(request,user)
        else:
            return HttpResponse('0')
    
    def signout(request)
      logout(request)