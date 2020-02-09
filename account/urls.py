from django.urls import path
from .views import signin,signup,logout
from django.http import HttpResponse
urlpatterns=[
    path('signin/',signin),
    path('signup/',signup),
    path('signout/',logout),
    path('out/',lambda x: HttpResponse('1'))
]