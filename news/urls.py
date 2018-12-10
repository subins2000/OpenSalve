from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsView.as_view()),
    # n/ News Item
    path('r/<int:id>', views.NewsInfo.as_view()),
]
