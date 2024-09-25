import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Obtener la ruta absoluta de la raíz del proyecto
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
dotenv_path = os.path.join(project_root, '.env')

# Cargar las variables del archivo .env
load_dotenv(dotenv_path)


def get_financial_data(symbol: str, interval: str):
    API_KEY = os.getenv('API_KEY')
    URL_API = os.getenv('URL_API')
    
    params = {
        'function': 'TIME_SERIES_INTRADAY',  
        'symbol': symbol, 
        'interval':interval,
        'outputsize': 'full',
        'apikey': API_KEY, 
        'datatype': 'json'
    }
    

    # Realizar la solicitud GET a la API
    response = requests.get(URL_API, params)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        data = response.json()  # Convertir la respuesta a formato JSON
                
    # Comprobar si la respuesta contiene datos válidos
    if "Time Series ("+interval+")" not in data:
        raise ValueError("Error al obtener datos de la API")
    
    # Convertir los datos a un DataFrame
    df = pd.DataFrame.from_dict(data['Time Series ('+interval+')'], orient='index', dtype=float)
    
    # Renombrar columnas para que tengan nombres más intuitivos
    df.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    }, inplace=True)
    
    # Convertir el índice a formato de fecha
    df.index = pd.to_datetime(df.index)
    
    return df