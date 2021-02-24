from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'EndOf-home'),
    path('about/', views.about, name = 'EndOf-about'),
]