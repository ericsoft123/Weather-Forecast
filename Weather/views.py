from django.http import JsonResponse
from django.shortcuts import render




#Rest API framework

from .ServiceAPI.Weather import Weather



from rest_framework.response import Response
from rest_framework.views import APIView

# This Last Import will Make our Display Query String on Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 



class WeatherAPIView(APIView):
    
    days_param_config=openapi.Parameter('days',in_=openapi.IN_QUERY,description='Enter Number',type=openapi.TYPE_NUMBER,required=True) #Describe Query String
    @swagger_auto_schema(manual_parameters=[days_param_config]) #Create Manual Query String
    
    def get(self,request,city,*args, **kwargs):
            
           
      
            days=self.request.GET.get('days','none') #set default 1 in case input is not exist
            
            try:
            
             int(days)
             str(city)

             return Response(Weather.ForeCast(city,days))#call This ForeCast Method inside Weather
            except ValueError:
             return  Response(False)