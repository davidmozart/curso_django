from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.regiter_view, name='register'),
    path('register/create/', views.regiter_create, name='create'),
]
