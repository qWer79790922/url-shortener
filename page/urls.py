from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.create_short_url, name='create_url'),  # 首頁直接建立短網址
    path('<str:short_code>/', views.redirect_short_url, name='redirect_url'),
]