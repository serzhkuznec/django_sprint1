from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    # Напишите адрес тут
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
