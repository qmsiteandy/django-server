from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('article', views.create_article),
]