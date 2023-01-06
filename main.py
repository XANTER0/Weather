import requests as rq
from api import api_key
import colors as cs

def temp_color(temp):
    if(temp > 0 and temp < 20):
        return cs.green(temp)
    elif(temp > 20):
        return cs.yellow(temp)
    elif(temp < 0):
        return cs.blue(temp)
        

t = True
while t == True:
    f = input('Якщо хочете продовжити впишіть "так", якщо завершити "ні" >>> ')
    if(f == 'так' or f == 'Так'):

        town = str(input("У якому місті Ви зараз? >>> "))        
        params={
        "q": town,
        "appid": api_key,
        "units": "metric",
        }
        response = rq.get("https://api.openweathermap.org/data/2.5/weather", params=params)        

        if response.status_code == 200:

            x = response.json()
            situation = x['weather'][0]['main']
            temperature = round(x['main']['temp'])
            temp_feels = round(x['main']['feels_like'])
            humidity = round(x['main']['humidity'])
            wind_speed = x['wind']['speed']

            print('У місті ' + town + ' температура ' + str(temp_color(temperature)) + '°C' + cs.white(', відчувається як ') + str(temp_color(temp_feels)) + '°C' + cs.white(', ситуація у небі - ' + situation + ', швидкість вітру дорівнює ') + str(cs.purple(wind_speed)) + ' м/с' + cs.white(', вологість - ') + cs.purple(str(humidity) + '%') + cs.white('.'))
        else:
            print("Error", response.status_code)
    elif(f == 'ні' or f == 'Ні'):
        break