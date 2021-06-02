from django.urls import path
from . import views

app_name = 'pill'

urlpatterns = [
        path('getquery/', views.pillquery, name = 'getquery'),
]
