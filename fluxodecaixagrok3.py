# Importando a biblioteca numpy para cálculos numéricos avançados, como exponenciação eficiente e manipulação de arrays numéricos.
# Razão: Embora não seja estritamente necessário para este código, o NumPy otimiza operações matemáticas em grandes números, como os bilhões em FCF de empresas como a Apple.
# Exemplo: Em cenários com anos > 10, o NumPy pode acelerar projeções de FCFs exponenciais.
# Implicação financeira: Evita erros de precisão em cálculos com números grandes, comum em valuations de megacaps como AAPL.
import numpy as np


# Definindo a função principal para calcular o valuation por Fluxo de Caixa Descontado (DCF).
# Esta função encapsula toda a lógica do modelo DCF, permitindo reutilização para diferentes empresas.
# Parâmetros detalhados:
# - current_fcf: Fluxo de Caixa Livre (FCF) atual da empresa, medido em moeda (ex.: dólares). Representa o caixa gerado após despesas operacionais, impostos e investimentos em capital fixo, mas antes de pagamentos de dívida ou dividendos. Fonte típica: Relatórios 10-K ou sites como Yahoo Finance.
#   Exemplo: Para AAPL em 2025, $96.18 bilhões (TTM até junho).
# - growth_rate: Taxa de crescimento anual composta esperada para os FCFs no período explícito (como decimal, ex.: 0.05 para 5%). Baseada em análises históricas, projeções de analistas ou crescimento do setor.
#   Exemplo: 5% para AAPL, considerando slowdown no crescimento de iPhone, mas expansão em serviços.
#   Implicação: Taxas altas (>10%) são para empresas em crescimento rápido; baixas (<5%) para maduras.
# - years: Número de anos para a projeção explícita dos FCFs. Tipicamente 5-10 anos para capturar o período de alto crescimento antes da maturidade.
#   Exemplo: 5 anos, permitindo projeções detalhadas sem especulação excessiva.
# - wacc: Custo Médio Ponderado de Capital (como decimal, ex.: 0.09 para 9%). Taxa de desconto que reflete o risco da empresa, calculada como (E/V * Re) + (D/V * Rd * (1-Tc)), onde E=equity, D=debt, V=valor total, Re=custo de equity (CAPM), Rd=custo de dívida, Tc=taxa de impostos.
#   Exemplo: 9% para AAPL, baseado em beta ~1.2, risk-free rate ~4%, equity risk premium ~5%.
#   Implicação: WACC alto indica risco maior; afeta diretamente o valor presente (PV) – quanto maior, menor o PV.
# - terminal_growth_rate: Taxa de crescimento perpétuo dos FCFs após o período explícito (ex.: 0.03 para 3%). Geralmente alinhada com o crescimento do PIB nominal de longo prazo (2-4% para EUA).
#   Exemplo: 3% para AAPL, assumindo crescimento estável em um mercado maduro.
#   Implicação: Deve ser < WACC para evitar valores infinitos; conservador para evitar superestimação.
# - shares_outstanding: Número total de ações em circulação. Usado para calcular o preço por ação.
#   Exemplo: 14.857 bilhões para AAPL em junho de 2025.
#   Implicação: Diluição por emissões de ações (ex.: stock options) pode reduzir o preço intrínseco.
# - net_debt: Dívida líquida (dívida total - caixa e equivalentes). Opcional, padrão 0. Ajusta o valor da empresa (Enterprise Value) para o valor do patrimônio (Equity Value).
#   Exemplo: $46.33 bilhões para AAPL (dívida $101.7B - caixa $55.37B).
#   Implicação: Net debt negativo (net cash) aumenta o valor por ação; positivo reduz.
def dcf_valuation(current_fcf, growth_rate, years, wacc, terminal_growth_rate, shares_outstanding, net_debt=0):
    # Validação inicial: Garante que o WACC seja estritamente maior que a taxa de crescimento terminal.
    # Razão: No modelo de Gordon, se wacc <= terminal_growth_rate, o denominador (wacc - terminal_growth_rate) <= 0, levando a valores negativos ou infinitos, o que é matematicamente inválido e financeiramente irrealista (nenhuma empresa cresce perpetuamente mais rápido que seu custo de capital).
    # Exemplo: Se wacc=0.08 e terminal_growth_rate=0.09, erro é lançado para prevenir TV negativo.
    # Implicação: Força o usuário a usar assunções realistas, alinhadas com teoria financeira (ex.: Damodaran recomenda terminal_growth_rate ~ PIB nominal).
    if wacc <= terminal_growth_rate:
        raise ValueError("WACC deve ser maior que a taxa de crescimento terminal.")

    # Validação: Garante que o número de ações seja positivo e maior que zero.
    # Razão: Divisão por zero ou negativo causaria erros no preço por ação; valores negativos não fazem sentido financeiramente.
    # Exemplo: Se shares_outstanding=0, erro evita crash; para AAPL, 14.857B é válido.
    # Implicação: Prevê cenários raros como empresas sem ações públicas, mas essencial para robustez.
    if shares_outstanding <= 0:
        raise ValueError("Número de ações deve ser maior que zero.")

    # Validação: Garante que o FCF atual seja positivo.
    # Razão: FCF negativo implica empresa queimando caixa, o que pode invalidar o modelo DCF (que assume geração de caixa positiva); projeções negativas levariam a valores irreais.
    # Exemplo: Se current_fcf=-$10M, erro; para AAPL, $96.18B é positivo.
    # Implicação: Para empresas deficitárias, use modelos alternativos como EV/EBITDA.
    if current_fcf <= 0:
        raise ValueError("FCF atual deve ser maior que zero.")

    # Validação: Garante que o número de anos seja positivo e inteiro.
    # Razão: Anos <=0 causaria loops vazios ou erros em projeções; modelo DCF requer período explícito >0.
    # Exemplo: Se years=0, erro; 5 anos é padrão.
    # Implicação: Permite flexibilidade, mas previne inputs inválidos.
    if years <= 0:
        raise ValueError("Número de anos deve ser maior que zero.")

    # Validação adicional: Garante que a taxa de crescimento explícita não seja negativa ou irrealisticamente alta (>50%).
    # Razão: Growth_rate negativa implica declínio perpétuo, raro em valuations; >50% é especulativo e pode inflar projeções.
    # Exemplo: Se growth_rate=-0.1, erro; para AAPL, 0.05 é razoável.
    # Implicação: Aumenta realismo, baseado em guidelines de finanças (ex.: CFA recomenda <20% para longo prazo).
    if growth_rate < 0 or growth_rate > 0.5:
        raise ValueError("Taxa de crescimento deve ser entre 0 e 0.5 (50%) para realismo.")

    # Validação adicional: Garante que a taxa de crescimento terminal seja razoável (0% a 5%).
    # Razão: Taxas >5% implicam crescimento infinito acima do PIB, irreal; <0% implica declínio perpétuo.
    # Exemplo: Se terminal_growth_rate=0.06, erro se wacc baixo; para AAPL, 0.03 é conservador.
    # Implicação: Alinha com práticas de mercado (ex.: McKinsey Valuation recomenda 2-4%).
    if terminal_growth_rate < 0 or terminal_growth_rate > 0.05:
        raise ValueError("Taxa de crescimento terminal deve ser entre 0 e 0.05 (5%).")

    # Passo 1: Projeta os Fluxos de Caixa Livres (FCFs) para cada ano do período explícito usando crescimento composto.
    # Fórmula matemática: FCF_t = current_fcf * (1 + growth_rate)^t, para t=1 a years.
    # Razão: Assume crescimento exponencial baseado em assunções históricas ou de analistas; list comprehension é eficiente para gerar a lista.
    # Exemplo detalhado: Para current_fcf=$96.18B, growth_rate=0.05, years=5:
    #   t=1: 96.18B * (1+0.05)^1 = $100.989B
    #   t=2: 96.18B * (1+0.05)^2 = $106.038B
    #   ... até t=5: $122.753B
    # Implicação financeira: Captura o "alto crescimento" inicial; sensível a growth_rate – pequeno aumento pode dobrar o valor final.
    # Depuração: Imprime os FCFs projetados para verificação.
    projected_fcfs = [current_fcf * (1 + growth_rate) ** (i + 1) for i in range(years)]
    print("[Depuração] Fluxos de Caixa Projetados:",
          [f"${fcf:,.2f}" for fcf in projected_fcfs])  # Logging opcional para rastrear

    # Passo 2: Extrai o último FCF projetado, que serve de base para o Valor Terminal.
    # Razão: O TV é calculado a partir do FCF do ano final explícito, assumindo transição para crescimento perpétuo.
    # Exemplo: Para years=5, last_fcf = projected_fcfs[4] = $122.753B para AAPL.
    # Implicação: Erros em projeções explícitas propagam para o TV, que pode representar 60-80% do valor total em DCFs.
    last_fcf = projected_fcfs[-1]
    print(f"[Depuração] Último FCF Projetado: ${last_fcf:,.2f}")  # Logging para verificação

    # Passo 3: Calcula o Valor Terminal (TV) usando o modelo de crescimento perpétuo de Gordon.
    # Fórmula matemática: TV = last_fcf * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    # Razão: Assume que após o período explícito, os FCFs crescem perpetuamente a uma taxa constante, descontados ao WACC. (1 + terminal_growth_rate) ajusta o FCF para o ano n+1.
    # Exemplo detalhado: Para last_fcf=$122.753B, terminal_growth_rate=0.03, wacc=0.09:
    #   Numerador: 122.753B * (1 + 0.03) = $126.436B
    #   Denominador: 0.09 - 0.03 = 0.06
    #   TV = 126.436B / 0.06 = $2,107.255B
    # Implicação financeira: TV captura o "valor residual" da empresa; sensível ao denominador – pequena redução em wacc aumenta TV dramaticamente.
    # Referência: Modelo de Gordon (1959), amplamente usado em finanças corporativas.
    terminal_value = last_fcf * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    print(f"[Depuração] Valor Terminal Calculado: ${terminal_value:,.2f}")  # Logging para rastrear

    # Passo 4: Combina os fluxos de caixa explícitos com o Valor Terminal no último ano.
    # Razão: O TV é recebido no final do último ano explícito, então é somado ao FCF desse ano para desconto conjunto.
    # Exemplo: all_cash_flows = [$100.989B, $106.038B, $111.340B, $116.907B, ($122.753B + $2,107.255B)]
    # Implicação: Garante que o TV seja descontado corretamente como um fluxo futuro.
    all_cash_flows = projected_fcfs[:-1] + [projected_fcfs[-1] + terminal_value]
    print("[Depuração] Todos os Fluxos de Caixa (incluindo TV):",
          [f"${cf:,.2f}" for cf in all_cash_flows])  # Logging para verificação

    # Passo 5: Calcula o Valor Presente (PV) total dos fluxos de caixa usando desconto composto.
    # Fórmula matemática: PV = Σ [cash_flow_t / (1 + wacc)^t] para t=1 a years, onde cash_flow_years inclui TV.
    # Razão: Reflete o "valor do dinheiro no tempo" – fluxos futuros valem menos hoje devido a risco e oportunidade.
    # Exemplo detalhado para AAPL:
    #   t=1: $100.989B / (1+0.09)^1 ≈ $92.650B
    #   t=2: $106.038B / (1+0.09)^2 ≈ $89.235B
    #   t=3: $111.340B / (1+0.09)^3 ≈ $86.052B
    #   t=4: $116.907B / (1+0.09)^4 ≈ $82.840B
    #   t=5: ($122.753B + $2,107.255B) / (1+0.09)^5 ≈ $1,549.272B
    #   Total PV ≈ $1,800.049B
    # Implicação: O loop garante precisão; para anos>10, considere vetorização com NumPy para performance.
    # Referência: Conceito central do DCF, baseado em Irving Fisher (1930).
    present_value = 0
    for t, cash_flow in enumerate(all_cash_flows, start=1):
        discounted_cf = cash_flow / (1 + wacc) ** t  # Cálculo individual para cada fluxo
        present_value += discounted_cf
        print(f"[Depuração] Fluxo Descontado Ano {t}: ${discounted_cf:,.2f}")  # Logging detalhado por ano

    # Passo 6: Calcula o Valor do Patrimônio Líquido (Equity Value).
    # Fórmula: Equity Value = PV - net_debt
    # Razão: O PV é o Enterprise Value (valor da empresa incluindo dívida); subtrair net_debt dá o valor pertencente aos acionistas.
    # Exemplo: Para PV=$1,800.049B e net_debt=$46.33B, Equity Value=$1,753.719B
    # Implicação: Se net_debt negativo (net cash), aumenta o valor; crucial para empresas alavancadas.
    equity_value = present_value - net_debt
    print(f"[Depuração] Valor do Patrimônio Líquido: ${equity_value:,.2f}")  # Logging

    # Passo 7: Calcula o Preço Intrínseco por Ação.
    # Fórmula: intrinsic_price = equity_value / shares_outstanding
    # Razão: Converte o valor total do patrimônio em um preço por ação comparável ao mercado.
    # Exemplo: Para equity_value=$1,753.719B e shares_outstanding=14.857B, preço=$118.04
    # Implicação: Se preço intrínseco > preço de mercado, ação subvalorizada (buy); oposto, sobrevalorizada (sell). Para AAPL em 25/08/2025, preço de mercado ~$227, sugerindo sobrevalorização sob essas assunções.
    intrinsic_price = equity_value / shares_outstanding
    print(f"[Depuração] Preço Intrínseco por Ação: ${intrinsic_price:,.2f}")  # Logging

    # Retorna todos os resultados intermediários para análise externa.
    # Razão: Permite ao usuário acessar não só o preço final, mas todos os passos para sensibilidade ou gráficos.
    # Implicação: Facilita análises avançadas, como Monte Carlo para variações em growth_rate.
    return projected_fcfs, terminal_value, present_value, equity_value, intrinsic_price


# Bloco de teste com dados reais da Apple Inc. (AAPL) em 2025.
# Razão: Demonstra o funcionamento prático; use try-except para capturar erros de validação.
# Implicação: Pode ser adaptado para outras empresas, alterando parâmetros.
try:
    projected_fcfs, terminal_value, present_value, equity_value, intrinsic_price = dcf_valuation(
        current_fcf=96_180_000_000,  # FCF atual da AAPL (TTM junho 2025)
        growth_rate=0.05,  # Crescimento estimado conservador
        years=5,  # Período explícito
        wacc=0.09,  # WACC médio para AAPL
        terminal_growth_rate=0.03,  # Crescimento perpétuo
        shares_outstanding=14_857_000_000,  # Ações em circulação
        net_debt=46_330_000_000  # Dívida líquida estimada
    )

    # Exibe os resultados principais, formatados para legibilidade (sem logging de depuração na saída final).
    # Razão: Fornece uma visão clara e profissional dos outputs.
    print("Fluxos de Caixa Projetados:", [f"${fcf:,.2f}" for fcf in projected_fcfs])
    print(f"Valor Terminal: ${terminal_value:,.2f}")
    print(f"Valor Presente dos Fluxos de Caixa: ${present_value:,.2f}")
    print(f"Valor do Patrimônio Líquido: ${equity_value:,.2f}")
    print(f"Preço Intrínseco por Ação: ${intrinsic_price:,.2f}")
except ValueError as e:
    print(f"Erro na validação: {e}")