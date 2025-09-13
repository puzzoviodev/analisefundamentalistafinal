import requests
from bs4 import BeautifulSoup

# URL da página
url = 'https://investidor10.com.br/acoes/itsa4/'

# Requisição HTTP
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Criação do objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Lista de indicadores que queremos extrair
indicadores = ['P/L', 'P/VP', 'P/RECEITA (PSR)']
resultados = {}

# Busca por cada indicador
for indicador in indicadores:
    span_indicador = soup.find('span', string=lambda text: text and indicador in text)
    if span_indicador:
        div_valor = span_indicador.find_next('div', class_='value')
        if div_valor:
            valor = div_valor.find('span').text.strip()
            resultados[indicador] = valor

# Exibe os resultados
for nome, valor in resultados.items():
    print(f'{nome}: {valor}')
