import requests
from bs4 import BeautifulSoup

url = 'https://investidor10.com.br/acoes/itsa4/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os blocos de indicadores
cells = soup.select('div.cell')

resultados = {}

for cell in cells:
    # Dentro de cada bloco, encontra todos os spans com nome de indicador
    spans_indicadores = cell.find_all('span', recursive=False)
    valores = cell.find_all('div', class_='value')

    for i in range(len(spans_indicadores)):
        nome = spans_indicadores[i].get_text(strip=True)

        # Verifica se há um valor correspondente
        if i < len(valores):
            valor_span = valores[i].find('span')
            valor = valor_span.get_text(strip=True) if valor_span else 'N/A'
            resultados[nome] = valor

# Exibe todos os indicadores encontrados
for nome, valor in resultados.items():
    print(f'{nome}: {valor}')
