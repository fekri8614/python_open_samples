import requests

data = requests.get('https://data.snb.ch/api/cube/amarbma/data/csv/en').text

data_text = str(data).splitlines()[-6].split(';')

rate = float(data_text[2].replace('"', ''))

print(rate)