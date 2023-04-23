"""Defines the URL patterns for learning logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index')
]
