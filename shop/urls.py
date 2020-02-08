from django.urls import path
from .views import search,announcment,addAnnounce

urlpatterns=[
    path('search/',search),
    path('',announcment),
    path('add/',addAnnounce),
]