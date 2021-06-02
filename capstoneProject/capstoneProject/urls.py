from django.contrib import admin
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visionAPI/', include('visionAPI.urls')),
    #path('DB/',include('blog.urls')),
    path('blog/', include('blog.urls')),
    #path('etcinfoImage/', blog.views.etcinfo),
    path('sendInfo/', include('sendInfo.urls')),
    path('',include('pill.urls')),
    ]
