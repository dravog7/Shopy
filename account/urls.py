from django.urls import path
from .views import signin,signup,logout

urlpatterns=[
    path('signin/',signin),
    path('signup/',signup),
    path('logout/',logout),
]