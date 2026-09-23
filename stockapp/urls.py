from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_trend, name='predict_trend'),
]
