from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.UserRegister, name='signup'),
]