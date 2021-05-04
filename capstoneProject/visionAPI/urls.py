from django.urls import path
from . import views

app_name = 'visionAPI'
urlpatterns = [
    path('', views.API.home, name = 'home'),
]
