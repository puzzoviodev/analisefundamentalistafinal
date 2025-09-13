from bs4 import BeautifulSoup

html = '''SEU_HTML_AQUI'''  # substitua pelo HTML completo que você colou

soup = BeautifulSoup(html, 'html.parser')

# Lista de indicadores que queremos extrair
indicadores = ['P/L', 'P/RECEITA (PSR)']

resultados = {}

for indicador in indicadores:
    # Localiza o <span> que contém o nome do indicador
    span_indicador = soup.find('span', string=lambda text: text and indicador in text)

    if span_indicador:
        # Encontra o próximo <div class="value"> após o indicador
        div_valor = span_indicador.find_next('div', class_='value')
        if div_valor:
            valor = div_valor.find('span').text.strip()
            resultados[indicador] = valor

# Exibe os resultados
for nome, valor in resultados.items():
    print(f'{nome}: {valor}')
