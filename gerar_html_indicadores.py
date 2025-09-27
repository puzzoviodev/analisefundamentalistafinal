
import pandas as pd

# Lê os dados da aba 'IndiRentabilidade' do arquivo Excel
df = pd.read_excel("StatusInvest_html.xlsx", sheet_name="IndiRentabilidade", engine="openpyxl")

# Mapeia cores para cada classificação
cores_classificacao = {
    "Ótimo": "#d4edda",
    "Bom": "#cce5ff",
    "Moderado": "#fff3cd",
    "Ruim": "#f8d7da",
    "Crítico": "#f5c6cb"
}

# Inicia o conteúdo HTML
html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Indicadores Financeiros - ABEV3</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 20px;
        }
        .caixa {
            border-left: 8px solid #333;
            background-color: #fff;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }
        .titulo {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .classificacao, .definicao, .descricao {
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <h1>Indicadores Financeiros - ABEV3</h1>
"""

# Itera sobre as linhas do DataFrame e cria caixas HTML
for _, row in df.iterrows():
    indicador = row["Indicador"]
    classificacao = row["Classificacao"]
    definicao = row["Definição"]
    descricao = row["Descricao"]
    cor = cores_classificacao.get(classificacao, "#ffffff")

    html += f"""
    <div class="caixa" style="border-left-color:{cor}; background-color:{cor};">
        <div class="titulo">{indicador}</div>
        <div class="classificacao"><strong>Classificação:</strong> {classificacao}</div>
        <div class="definicao"><strong>Definição:</strong> {definicao}</div>
        <div class="descricao"><strong>Descrição:</strong> {descricao}</div>
    </div>
    """

# Finaliza o HTML
html += """
</body>
</html>
"""

# Salva o HTML em um arquivo
with open("indicadores_ABEV3_com_variaveis.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Arquivo HTML gerado com sucesso: indicadores_ABEV3_com_variaveis.html")
