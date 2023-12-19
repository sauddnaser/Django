from django.urls import path
from . import views

urlpatterns = [
    path('tea-info/', views.tea_info, name='tea_info'),
]