from django.urls import path

from . import views

urlpatterns = [
    path('', views.pazzesca, name='pazzesca'),
    path('luna/', views.luna, name='luna'),
]