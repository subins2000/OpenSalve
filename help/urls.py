from django.urls import path

from . import views

urlpatterns = [
    path('add', views.AddRequest.as_view()),
    # r/ Request
    path('r/<int:id>', views.ViewRequest.as_view()),
    path('r/<int:id>/status', views.StatusRequest.as_view()),
]
