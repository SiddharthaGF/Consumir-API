from datetime import date, timedelta
from os import path, remove, linesep
import requests


cant_dias  = 300
fin = date.today()
inicio = fin - timedelta(days=cant_dias - 1)
moneda = 'JPY'

lista_fechas = [inicio + timedelta(days=d)
                for d in range((fin - inicio).days + 1)]

url = f'https://api.apilayer.com/exchangerates_data/timeseries?start_date={inicio.strftime("%Y-%m-%d")}&end_date={fin.strftime("%Y-%m-%d")}&currencies={moneda}'

payload = {}
headers = {
    "apikey": "PHg4rnXJ1vAA9bPqzZrP5M4FDKKSehwi"
}

response = requests.get(url, headers=headers, data=payload).json()

path = path.expanduser('~\\OneDrive\\Documents') + "\\datos.dts"
remove(path)
file = open(path, "w")

for i, fecha in enumerate(lista_fechas):
    line = response.get('quotes').get(fecha.strftime("%Y-%m-%d")).get(f'USD{moneda}')
    if i < len(lista_fechas) - 1:
        file.write(str(line) + linesep)
    else:
        file.write(str(line))

file.close()
