from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.Home.as_view()),
]