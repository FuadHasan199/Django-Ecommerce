from django.urls import path
from auth import views

urlpatterns = [
   path('signIn/',views.signIn, name='signIn'),
   path('logIn/',views.handleLogin, name='logIn'),
   path('logOut/',views.handleLogOut, name='logOut'),
]