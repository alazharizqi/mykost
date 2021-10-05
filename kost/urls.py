from django.urls import path
from . import views

urlpatterns = [
    path('', views.kost, name='kost'),
    path('detail/<str:id>', views.detail, name='detail'),
]