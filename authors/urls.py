from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.regiter_view, name='register'),
]
