from django.urls import path

from . import views

urlpatterns = [
    path('pizza/', views.menu, name='pizza'),
]