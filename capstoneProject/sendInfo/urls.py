
from django.urls import path
from . import views

app_name = 'sendInfo'

urlpatterns = [
        path('otcinfoImage/', views.sendImage.otcinfoImage, name = 'otcinfoImage'),
        path('etcinfoImage/', views.sendImage.etcinfoImage, name = 'etcinfoImage'),
        path('pillImage/', views.sendImage.pillImage, name = 'pillImage'),
        ]
