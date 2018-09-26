from django.urls import path

from . import views

urlpatterns = [
    path('', views.Camp.as_view()),
    # c/ Camp
    path('c/<int:id>', views.ViewCamp.as_view()),
]
