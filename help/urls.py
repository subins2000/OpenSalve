from django.urls import path

from . import views

urlpatterns = [
    path('', views.Request.as_view()),
    # r/ Request
    path('r/<int:id>', views.RequestView.as_view()),
    path('r/<int:id>/status', views.RequestStatus.as_view()),
    path('r/<int:id>/comments', views.RequestComments.as_view()),
]
