from django.urls import path

from . import views

urlpatterns = [
    path('register', views.UsersRegister.as_view()),
]
