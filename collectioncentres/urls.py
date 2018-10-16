from django.urls import path

from . import views

urlpatterns = [
    path('', views.CollectionCentre.as_view()),
    # c/ Collection Centre
    path('c/<int:id>', views.CollectionCentreView.as_view()),
    path('c/<int:id>/stock', views.CollectionCentreStockView.as_view()),
]
