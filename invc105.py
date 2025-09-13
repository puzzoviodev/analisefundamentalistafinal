import requests
from bs4 import BeautifulSoup

url = 'https://investidor10.com.br/acoes/itsa4/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

resultados = {}

# 🔹 Parte 1: Indicadores Múltiplos
cells = soup.select('div.cell')
for cell in cells:
    spans = cell.find_all('span', recursive=False)
    values = cell.find_all('div', class_='value')

    for span, value in zip(spans, values):
        nome_indicador = span.get_text(strip=True).split(' ')[0]
        valor = value.find('span').get_text(strip=True)
        resultados[nome_indicador] = valor

# 🔹 Parte 2: Indicadores da Grid Financeira
indicadores_grid = [
    'Lucro Bruto', 'Lucro Líquido', 'EBITDA', 'EBIT',
    'Dívida Bruta', 'Dívida Líquida',
    'Margem Bruta', 'Margem EBITDA', 'Margem Líquida',
    'ROE', 'ROIC'
]

for indicador in indicadores_grid:
    span_indicador = soup.find('span', string=lambda text: text and indicador in text)
    if span_indicador:
        valor_span = span_indicador.find_next('span')
        valor = valor_span.get_text(strip=True) if valor_span else 'N/A'
        resultados[indicador] = valor

# 🔹 Parte 3: Liquidez Média Diária
liquidez_span = soup.find('span', string=lambda text: text and 'Liquidez Média Diária' in text)
if liquidez_span:
    valor_span = liquidez_span.find_next('span')
    valor = valor_span.get_text(strip=True) if valor_span else 'N/A'
    resultados['Liquidez Média Diária'] = valor

# 🔹 Exibe todos os resultados
print('\n📊 Indicadores Financeiros da ITSA4:\n')
for nome, valor in resultados.items():
    print(f'{nome}: {valor}')
