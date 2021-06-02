from django.urls import path
from . import views

app_name = 'visionAPI'
urlpatterns = [
    path('result/', views.API.home, name = 'home'),
    path('image/', views.getInfoFromAndroid.getImage, name = 'image'),
    path('lanCode/', views.getInfoFromAndroid.getLanCode, name = 'lan_code'),
    path('translate/', views.API.translate, name = 'trans'),
]
