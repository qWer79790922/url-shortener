from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('panda-cute/', admin.site.urls),
    path('', include('page.urls')), 
]
