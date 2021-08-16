import requests
import statistics
from decouple import config

def ForeCast(city,days):
    try:
             baseUrl=config('WEATHER_URL')
             WeatherKey=config('WEATHER_API_KEY')
             response=requests.get(f'{baseUrl}/forecast.json?key={WeatherKey}&q={city}&days={days}&aqi=no&alerts=no').json()
             
             mydata=response["forecast"]["forecastday"][0]["hour"]
            
           
             list_temp_c=[] #this will store in list temperature in Celicius
             list_temp_f=[] #this will store in list temperature in Fahrenheight
             
             for i in range(0,len(mydata)):
                list_temp_c.append(mydata[i]["temp_c"])
                list_temp_f.append(mydata[i]["temp_f"])
            
            
             return {
                 'Max_temp_c':min(list_temp_c),
                 'Min_temp_c':max(list_temp_c),
                 'Median_temp_c':statistics.median(list_temp_c),
                 'Average_temp_c':statistics.mean( list_temp_c),
                 'Max_temp_f':min(list_temp_f),
                 'Min_temp_f':max(list_temp_f),
                 'Median_temp_f':statistics.median(list_temp_f),
                 'Average_temp_f':statistics.mean( list_temp_f)
             }
             
    except requests.Timeout as error:
            return Response(error)