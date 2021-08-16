from django.urls import path
#call WeatherAPIView class from view
from .views import WeatherAPIView 

urlpatterns = [
    path('location/<str:city>',WeatherAPIView.as_view(),name='ForecastData') 
]