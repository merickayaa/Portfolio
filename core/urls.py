from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name="index"),
]
