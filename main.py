import requests
import os
from dotenv import load_dotenv

def get_temperature(ciudad):
    try:
        load_dotenv()
        key = os.getenv('KEY')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={key}')
        
        if response.status_code == 200:
           json_response = response.json()
           temp_min = json_response['main']['temp_min']
           temp_max = json_response['main']['temp_max']
           print(f'Temperatura Maxima: {temp_max} Temperatura Minima: {temp_min}')
        else:
            print('Error al obtener la temperatura')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    ciudad = input('Ingrese el nombre de la ciudad a obtener su temperatura: ')
    get_temperature(ciudad)

