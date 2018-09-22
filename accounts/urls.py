from django.urls import path

from . import views


urlpatterns = [
    path('login', views.UserLogin.as_view()),
    path('register', views.UserRegister.as_view()),
    path('u/<username>', views.UserInfo.as_view()),
]
