from django.urls import path

from . import views


urlpatterns = [
    path('login', views.UsersLogin.as_view()),
    path('register', views.UsersRegister.as_view()),
    path('u/<username>', views.UserInfo.as_view()),
]
