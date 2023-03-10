from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path ('onlinestore/', views.onlinestore),
    path('cv/', views.CV),
]
