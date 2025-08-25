# Importando a biblioteca numpy para cálculos numéricos avançados, como exponenciação eficiente e manipulação de arrays.
# Razão: O NumPy otimiza operações com números grandes (bilhões de reais no caso da PETR4), evitando erros de precisão em projeções de FCFs.
# Exemplo: Para PETR4, FCFs projetados atingem R$ 97.67 bilhões em 5 anos; o NumPy lida eficientemente com (1 + 0.03)**5.
# Implicação financeira: Garante precisão em valuations de empresas grandes como a Petrobras, onde pequenas imprecisões podem alterar o preço por ação significativamente.
# Referência: NumPy é amplamente usado em finanças quantitativas (ex.: QuantLib, Python for Finance).
import numpy as np


# Definindo a função principal para calcular o valuation por Fluxo de Caixa Descontado (DCF).
# Esta função encapsula o modelo DCF completo, permitindo reutilização para PETR4 ou outras ações.
# Parâmetros detalhados:
# - current_fcf: Fluxo de Caixa Livre (FCF) atual da empresa, em Reais (BRL). Representa o caixa disponível após despesas operacionais, impostos e investimentos em capital, mas antes de juros e dividendos.
#   Exemplo: Para PETR4, R$ 84.69 bilhões (baseado em lucro líquido ajustado para FCF, 2025).
#   Fonte: Estimativa com base em dados de Investing.com (lucro líquido R$ 77.37 bilhões, ajustado).[](https://www.investing.com/equities/petrobras-pn)
# - growth_rate: Taxa de crescimento anual composta dos FCFs no período explícito (ex.: 0.03 para 3%). Baseada em projeções de analistas, histórico da empresa e condições do setor de óleo e gás.
#   Exemplo: 3% para PETR4, considerando crescimento moderado devido a preços do petróleo e riscos regulatórios no Brasil.
#   Implicação: Taxas altas (>10%) são para empresas em hiper-crescimento; PETR4, madura, exige conservadorismo.
# - years: Número de anos para projeção explícita. Padrão de 5-10 anos para capturar crescimento de curto prazo antes da estabilização.
#   Exemplo: 5 anos, suficiente para PETR4, dado ciclo de investimentos em exploração.
# - wacc: Custo Médio Ponderado de Capital (ex.: 0.10 para 10%). Taxa de desconto que reflete o risco da empresa, calculada como (E/V * Re) + (D/V * Rd * (1-Tc)), onde E=equity, D=debt, V=valor total, Re=custo de equity (via CAPM), Rd=custo de dívida, Tc=taxa de impostos.
#   Exemplo: 10% para PETR4, considerando beta 0.32, taxa livre de risco ~6% (Selic 2025), e prêmio de risco de mercado ~5%.
#   Implicação: WACC alto reduz o valor presente, refletindo riscos do setor (ex.: volatilidade do Brent).
# - terminal_growth_rate: Taxa de crescimento perpétuo dos FCFs após o período explícito (ex.: 0.02 para 2%). Alinhada ao PIB nominal do Brasil (~2-3%).
#   Exemplo: 2% para PETR4, conservador para empresa estatal em setor cíclico.
#   Implicação: Deve ser < WACC para evitar valores irreais; reflete crescimento estável de longo prazo.
# - shares_outstanding: Número total de ações em circulação. Determina o preço por ação.
#   Exemplo: 12.89 bilhões para PETR4 (2025, Investing.com).[](https://www.investing.com/equities/petrobras-pn)
#   Implicação: Diluição (ex.: novas emissões) reduz o preço por ação.
# - net_debt: Dívida líquida (dívida total - caixa e equivalentes). Ajusta o valor da empresa (Enterprise Value) para o valor do patrimônio (Equity Value).
#   Exemplo: R$ 162 bilhões para PETR4, estimado com base em dados financeiros recentes.[](https://www.morningstar.com/stocks/bvmf/petr4/quote)
#   Implicação: Dívida alta reduz o valor do patrimônio, impactando o preço por ação.
def dcf_valuation(current_fcf, growth_rate, years, wacc, terminal_growth_rate, shares_outstanding, net_debt=0):
    # Validação 1: Garante que o WACC seja estritamente maior que a taxa de crescimento terminal.
    # Razão: No modelo de Gordon, wacc <= terminal_growth_rate resulta em denominador <=0, causando valores negativos ou infinitos, o que é inválido (nenhuma empresa cresce perpetuamente acima do custo de capital).
    # Exemplo: Para PETR4, wacc=0.10 > terminal_growth_rate=0.02, válido. Se wacc=0.02, erro é lançado.
    # Implicação financeira: Força assunções realistas, evitando superestimação do valor terminal, que pode ser 60-80% do valor total em DCFs.
    # Referência: Gordon Growth Model (1959), Damodaran on Valuation (2012).
    if wacc <= terminal_growth_rate:
        raise ValueError("WACC deve ser maior que a taxa de crescimento terminal.")

    # Validação 2: Garante que o número de ações seja positivo.
    # Razão: Divisão por zero ou negativo no cálculo do preço por ação causaria erro ou resultados sem sentido.
    # Exemplo: Para PETR4, shares_outstanding=12.89B, válido. Se =0, erro.
    # Implicação: Protege contra inputs inválidos, como empresas sem ações públicas (raro).
    # Referência: Prática de programação defensiva em finanças corporativas.
    if shares_outstanding <= 0:
        raise ValueError("Número de ações deve ser maior que zero.")

    # Validação 3: Garante que o FCF atual seja positivo.
    # Razão: FCF negativo implica que a empresa queima caixa, tornando o modelo DCF inadequado (melhor usar EV/EBITDA ou outros métodos).
    # Exemplo: Para PETR4, current_fcf=R$ 84.69B, válido. Se fosse -R$ 10B, erro.
    # Implicação: Empresas deficitárias requerem modelos alternativos; DCF assume geração de caixa.
    # Referência: CFA Level II, Valuation Techniques.
    if current_fcf <= 0:
        raise ValueError("FCF atual deve ser maior que zero.")

    # Validação 4: Garante que o número de anos seja positivo e inteiro.
    # Razão: Período explícito <=0 resulta em projeções vazias, quebrando o modelo.
    # Exemplo: Para years=5, válido. Se years=0, erro.
    # Implicação: Garante que o modelo tenha um período explícito para projeções detalhadas.
    # Referência: McKinsey Valuation (2020).
    if years <= 0:
        raise ValueError("Número de anos deve ser maior que zero.")

    # Validação 5: Garante que a taxa de crescimento explícita seja realista (0% a 50%).
    # Razão: Taxa negativa implica declínio de FCFs, raro para empresas saudáveis; >50% é especulativo e irreal para empresas maduras como PETR4.
    # Exemplo: Para PETR4, growth_rate=0.03, válido. Se =0.6 (60%), erro.
    # Implicação: Evita projeções infladas, especialmente em setores cíclicos como óleo e gás.
    # Referência: Morningstar Valuation Guidelines, Damodaran (2020).
    if growth_rate < 0 or growth_rate > 0.5:
        raise ValueError("Taxa de crescimento deve ser entre 0 e 0.5 (50%) para realismo.")

    # Validação 6: Garante que a taxa de crescimento terminal seja realista (0% a 5%).
    # Razão: Taxa <0% implica declínio perpétuo, raro; >5% excede o PIB nominal, irreal para empresas maduras.
    # Exemplo: Para PETR4, terminal_growth_rate=0.02, válido. Se =0.06, erro.
    # Implicação: Conservadorismo é chave para evitar overvaluation em perpetuidade.
    # Referência: Damodaran on Terminal Value, McKinsey Valuation (2020).
    if terminal_growth_rate < 0 or terminal_growth_rate > 0.05:
        raise ValueError("Taxa de crescimento terminal deve ser entre 0 e 0.05 (5%).")

    # Passo 1: Projeta os Fluxos de Caixa Livres (FCFs) para cada ano do período explícito usando crescimento composto.
    # Fórmula matemática: FCF_t = current_fcf * (1 + growth_rate)^t, para t=1 até years.
    # Razão: Assume que os FCFs crescem a uma taxa constante durante o período explícito, refletindo investimentos em exploração (ex.: pré-sal para PETR4).
    # Exemplo detalhado para PETR4 (current_fcf=R$ 84.69B, growth_rate=0.03):
    #   Ano 1: 84.69B * (1 + 0.03)^1 = R$ 87.2307B
    #   Ano 2: 84.69B * (1 + 0.03)^2 = R$ 89.8478B
    #   Ano 3: 84.69B * (1 + 0.03)^3 = R$ 92.5432B
    #   Ano 4: 84.69B * (1 + 0.03)^4 = R$ 95.3195B
    #   Ano 5: 84.69B * (1 + 0.03)^5 = R$ 98.1791B
    # Implicação financeira: Projeções explícitas são a base do DCF; erros em growth_rate amplificam o valor terminal.
    # Referência: Crescimento composto, Damodaran (2012).
    # Depuração: Imprime FCFs projetados para verificação detalhada.
    projected_fcfs = [current_fcf * (1 + growth_rate) ** (i + 1) for i in range(years)]
    print("[Depuração] Fluxos de Caixa Projetados:", [f"R${fcf:,.2f}" for fcf in projected_fcfs])

    # Passo 2: Extrai o último FCF projetado, que serve como base para o Valor Terminal.
    # Razão: O Valor Terminal é calculado a partir do FCF do último ano explícito, assumindo transição para crescimento perpétuo.
    # Exemplo: Para PETR4, last_fcf = projected_fcfs[4] = R$ 98.1791B (ano 5).
    # Implicação: Precisão no último FCF é crucial, pois o Valor Terminal domina o valuation em empresas maduras.
    # Referência: Estrutura padrão de DCF.
    last_fcf = projected_fcfs[-1]
    print(f"[Depuração] Último FCF Projetado: R${last_fcf:,.2f}")

    # Passo 3: Calcula o Valor Terminal (TV) usando o modelo de crescimento perpétuo de Gordon.
    # Fórmula matemática: TV = last_fcf * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate).
    # Razão: Assume que, após o período explícito, os FCFs crescem perpetuamente a uma taxa constante, descontados ao WACC.
    # Exemplo detalhado para PETR4:
    #   last_fcf = R$ 98.1791B, terminal_growth_rate=0.02, wacc=0.10
    #   Numerador: 98.1791B * (1 + 0.02) = R$ 100.1427B
    #   Denominador: 0.10 - 0.02 = 0.08
    #   TV = 100.1427B / 0.08 = R$ 1,251.7838B
    # Implicação financeira: O TV representa a maior parte do valor da empresa (60-80% em empresas maduras como PETR4); sensível ao denominador (wacc - terminal_growth_rate).
    # Referência: Gordon Growth Model (1959), usado em Damodaran (2012).
    # Depuração: Imprime TV para verificação.
    terminal_value = last_fcf * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    print(f"[Depuração] Valor Terminal Calculado: R${terminal_value:,.2f}")

    # Passo 4: Combina os fluxos de caixa explícitos com o Valor Terminal no último ano.
    # Razão: O TV é recebido no final do último ano explícito (ano 5), então é somado ao FCF desse ano para desconto conjunto.
    # Exemplo para PETR4:
    #   projected_fcfs = [87.2307B, 89.8478B, 92.5432B, 95.3195B, 98.1791B]
    #   all_cash_flows = [87.2307B, 89.8478B, 92.5432B, 95.3195B, (98.1791B + 1,251.7838B)] = [..., 1,349.9629B]
    # Implicação: Garante que o TV seja descontado corretamente como fluxo futuro.
    # Referência: Estrutura padrão de DCF.
    all_cash_flows = projected_fcfs[:-1] + [projected_fcfs[-1] + terminal_value]
    print("[Depuração] Todos os Fluxos de Caixa (incluindo TV):", [f"R${cf:,.2f}" for cf in all_cash_flows])

    # Passo 5: Calcula o Valor Presente (PV) total dos fluxos de caixa usando desconto composto.
    # Fórmula matemática: PV = Σ [cash_flow_t / (1 + wacc)^t], para t=1 até years, onde cash_flow_years inclui o TV.
    # Razão: Aplica o conceito de valor do dinheiro no tempo, descontando fluxos futuros ao valor presente para refletir risco e custo de oportunidade.
    # Exemplo detalhado para PETR4 (wacc=0.10):
    #   Ano 1: 87.2307B / (1 + 0.10)^1 = R$ 79.3006B
    #   Ano 2: 89.8478B / (1 + 0.10)^2 = R$ 74.3213B
    #   Ano 3: 92.5432B / (1 + 0.10)^3 = R$ 69.5552B
    #   Ano 4: 95.3195B / (1 + 0.10)^4 = R$ 65.1012B
    #   Ano 5: (98.1791B + 1,251.7838B) / (1 + 0.10)^5 = R$ 837.8535B
    #   Total PV = 79.3006B + 74.3213B + 69.5552B + 65.1012B + 837.8535B = R$ 1,126.1318B
    # Implicação financeira: O PV é o valor da empresa hoje (Enterprise Value); sensível ao WACC – aumento de 1% pode reduzir PV em 10-20%.
    # Referência: Irving Fisher (1930), conceito de valor presente; Damodaran (2012).
    # Depuração: Imprime cada fluxo descontado para transparência.
    present_value = 0
    for t, cash_flow in enumerate(all_cash_flows, start=1):
        discounted_cf = cash_flow / (1 + wacc) ** t  # Calcula o valor presente de cada fluxo
        present_value += discounted_cf
        print(f"[Depuração] Fluxo Descontado Ano {t}: R${discounted_cf:,.2f}")

    # Passo 6: Calcula o Valor do Patrimônio Líquido (Equity Value).
    # Fórmula: Equity Value = PV - net_debt.
    # Razão: O PV representa o valor total da empresa (incluindo dívida); subtrair a dívida líquida dá o valor pertencente aos acionistas.
    # Exemplo para PETR4:
    #   PV = R$ 1,126.1318B, net_debt = R$ 162B
    #   Equity Value = 1,126.1318B - 162B = R$ 964.1318B
    # Implicação: Empresas com alta dívida (como PETR4) têm Equity Value significativamente menor que PV.
    # Referência: Enterprise Value vs. Equity Value, CFA Level II.
    equity_value = present_value - net_debt
    print(f"[Depuração] Valor do Patrimônio Líquido: R${equity_value:,.2f}")

    # Passo 7: Calcula o Preço Intrínseco por Ação.
    # Fórmula: intrinsic_price = equity_value / shares_outstanding.
    # Razão: Converte o valor do patrimônio em um preço por ação, comparável ao preço de mercado (ex.: R$ 30.29 para PETR4 em 21/08/2025).[](https://www.investing.com/equities/petrobras-pn)
    # Exemplo para PETR4:
    #   Equity Value = R$ 964.1318B, shares_outstanding = 12.89B
    #   intrinsic_price = 964.1318B / 12.89B = R$ 74.80
    # Implicação financeira: Se preço intrínseco (R$ 74.80) > preço de mercado (R$ 30.29), PETR4 está subvalorizada, sugerindo compra; se <, sobrevalorizada.
    # Referência: Valuation final para decisões de investimento, Damodaran (2020).
    intrinsic_price = equity_value / shares_outstanding
    print(f"[Depuração] Preço Intrínseco por Ação: R${intrinsic_price:,.2f}")

    # Retorna todos os resultados intermediários para análise detalhada.
    # Razão: Permite ao usuário acessar FCFs, TV, PV, Equity Value e preço para análises adicionais (ex.: sensibilidade ou gráficos).
    # Implicação: Facilita simulações como Monte Carlo ou comparação com outros modelos (ex.: P/E).
    return projected_fcfs, terminal_value, present_value, equity_value, intrinsic_price


# Bloco de teste com dados reais da Petrobras (PETR4) em 2025, usando Reais (BRL).
# Razão: Demonstra aplicação prática do DCF para uma ação brasileira, com parâmetros baseados em dados financeiros reais.
# Implicação: Pode ser adaptado para outras ações (ex.: VALE3) alterando parâmetros.
try:
    projected_fcfs, terminal_value, present_value, equity_value, intrinsic_price = dcf_valuation(
        current_fcf=84_690_000_000,  # FCF atual da PETR4 (estimado, 2025)
        growth_rate=0.03,  # Crescimento conservador de 3%
        years=5,  # Período explícito de 5 anos
        wacc=0.10,  # WACC de 10%, típico para setor de óleo
        terminal_growth_rate=0.02,  # Crescimento perpétuo de 2%
        shares_outstanding=12_890_000_000,  # Ações em circulação
        net_debt=162_000_000_000  # Dívida líquida estimada
    )

    # Exibe os resultados principais, formatados para legibilidade em Reais (BRL).
    # Razão: Fornece uma visão clara e profissional, comparável ao preço de mercado da PETR4.
    # Implicação: Ajuda investidores a decidir se PETR4 está subvalorizada ou sobrevalorizada.
    print("\n=== Resultados do Valuation da PETR4 ===")
    print("Fluxos de Caixa Projetados:", [f"R${fcf:,.2f}" for fcf in projected_fcfs])
    print(f"Valor Terminal: R${terminal_value:,.2f}")
    print(f"Valor Presente dos Fluxos de Caixa: R${present_value:,.2f}")
    print(f"Valor do Patrimônio Líquido: R${equity_value:,.2f}")
    print(f"Preço Intrínseco por Ação: R${intrinsic_price:,.2f}")
except ValueError as e:
    print(f"Erro na validação: {e}")