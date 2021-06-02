from django.urls import path
from . import views

app_name = 'blog'

"""
urlpatterns = [
        path('otcinfoImage/', views.blog.otcinfoImage, name = 'otcinfoImage'),
        path('etcinfoImage/', views.blog.etcinfoImage, name = 'etcinfoImage'),
        path('pillImage/', views.blog.pillImage, name = 'pillImage'),
]
"""
urlpatterns = [
        path('otcinfoImage/', views.otcinfo, name = 'otcinfo'),
        #path('etcinfoImage/', views.etcinfo, name = 'etcinfo'),
        path('pillImage/', views.pill, name = 'pill'),
    
]
