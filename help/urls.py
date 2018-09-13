from django.urls import path

from . import views

urlpatterns = [
    path('add', views.RequestAdd.as_view()),
    # r/ Request
    path('r/<int:id>', views.RequestView.as_view()),
    path('r/<int:id>/status', views.RequestStatus.as_view()),
]
