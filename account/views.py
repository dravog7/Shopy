from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import shop
def signin(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(request, username=username,password=password)
    if user is not None:
        return HttpResponse('1')
    else:
        return HttpResponse('0')

def signup(request):
    data = dict()
    data['own_name'] = request.GET['name']
    password = request.GET['password']
    email = request.GET['email']
    data['shop_name'] = request.GET['shop']
    data['sunday'] = request.GET['sunday']
    data['start_time'] = request.GET['start']
    data['end_time'] = request.GET['end']
    data['latitude'] = request.GET['lat']
    data['longtitude'] = request.GET['long']

    data['user'] = User.objects.create_user(data['own_name'],email,password)
    shopp = shop(**data)
    user=authenticate(request,username=data['own_name'],password=password)
    shopp.save()
    if user is not None:
        login(request,user)
        return HttpResponse('1')
    else:
        return HttpResponse('0')

@login_required
def signout(request):
    logout(request)
    return HttpResponse('1')