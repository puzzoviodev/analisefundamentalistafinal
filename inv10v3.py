import requests
from bs4 import BeautifulSoup

url = 'https://investidor10.com.br/acoes/itsa4/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra todas as células que contêm indicadores
cells = soup.select('div.cell')

resultados = {}

for cell in cells:
    spans = cell.find_all('span', recursive=False)
    values = cell.find_all('div', class_='value')

    for span, value in zip(spans, values):
        nome_indicador = span.get_text(strip=True).split(' ')[0]  # pega o nome antes do ícone
        valor = value.find('span').get_text(strip=True)
        resultados[nome_indicador] = valor

# Exibe os resultados
for nome, valor in resultados.items():
    print(f'{nome}: {valor}')
