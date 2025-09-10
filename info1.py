import pandas as pd
#from comoparador import LucroLiquidoEvaluator, EBITDAEvaluator, DividaBrutaEvaluator, VPAEvaluator, PLEvaluator, MargemBrutaEvaluator, PVPEvaluator, ResultadoIND
from analiseativos import LucroLiquidoEvaluator, EBITDAEvaluator, DividaBrutaEvaluator, VPAEvaluator, PLEvaluator, MargemBrutaEvaluator, PVPEvaluator, ResultadoIND


# Função para coletar resultados de todas as condições de uma classe
def coletar_resultados_avaliacao():
    resultados = []

    # Função auxiliar para adicionar resultados ao dicionário
    def adicionar_resultado(resultado, classe_nome, metodo):
        resultado_dict = resultado.to_dict()
        resultado_dict['Classe'] = classe_nome
        resultado_dict['Metodo'] = metodo
        resultados.append(resultado_dict)

    # 1. Testes para LucroLiquidoEvaluator
    lucro_evaluator = LucroLiquidoEvaluator()
    receita_liquida = 1000  # Valor fixo para receita líquida
    testes_lucro = [
        (-100, "Negativo"),  # Lucro Líquido < 0
        (0, "Baixo"),  # 0 <= Margem Líquida <= 5%
        (75, "Moderado"),  # 5% < Margem Líquida <= 10%
        (150, "Bom"),  # 10% < Margem Líquida <= 20%
        (300, "Ótimo"),  # Margem Líquida > 20%
        ("invalido", "Erro")  # Entrada inválida
    ]
    for lucro, condicao in testes_lucro:
        resultado = lucro_evaluator.avaliar(lucro, receita_liquida)
        adicionar_resultado(resultado, "LucroLiquidoEvaluator", f"avaliar (lucro={lucro}, receita={receita_liquida})")

    # 2. Testes para EBITDAEvaluator
    ebitda_evaluator = EBITDAEvaluator()
    testes_ebitda = [
        (-100, "Negativo"),  # EBITDA < 0
        (50, "Baixo"),  # 0 <= Margem EBITDA <= 10%
        (150, "Moderado"),  # 10% < Margem EBITDA <= 20%
        (250, "Bom"),  # 20% < Margem EBITDA <= 30%
        (400, "Ótimo"),  # Margem EBITDA > 30%
        ("invalido", "Erro")  # Entrada inválida
    ]
    for ebitda, condicao in testes_ebitda:
        resultado = ebitda_evaluator.avaliar(ebitda, receita_liquida)
        adicionar_resultado(resultado, "EBITDAEvaluator", f"avaliar (ebitda={ebitda}, receita={receita_liquida})")

    # 3. Testes para DividaBrutaEvaluator
    divida_evaluator = DividaBrutaEvaluator()
    ativos_totais = 1000  # Valor fixo para ativos totais
    testes_divida = [
        (-100, "Negativo"),  # Dívida Bruta < 0
        (0, "Nula"),  # Dívida Bruta = 0
        (150, "Bom"),  # 0 < Dívida Bruta / Ativos <= 0.3
        (450, "Moderado"),  # 0.3 < Dívida Bruta / Ativos <= 0.6
        (800, "Baixo"),  # 0.6 < Dívida Bruta / Ativos <= 1.0
        (1200, "Crítico"),  # Dívida Bruta / Ativos > 1.0
        ("invalido", "Erro")  # Entrada inválida
    ]
    for divida, condicao in testes_divida:
        resultado = divida_evaluator.avaliar(divida, ativos_totais)
        adicionar_resultado(resultado, "DividaBrutaEvaluator", f"avaliar (divida={divida}, ativos={ativos_totais})")

    # 4. Testes para VPAEvaluator
    vpa_evaluator = VPAEvaluator()
    preco_acao = 10  # Valor fixo para preço da ação
    testes_vpa = [
        (-1, "Crítico"),  # P/VPA < 0
        (0.1, "Ótimo"),  # 0 <= P/VPA <= 0.8
        (1.1, "Bom"),  # 0.8 < P/VPA <= 1.2
        (1.3, "Moderado"),  # 1.2 < P/VPA <= 1.8
        (1.9, "Ruim"),  # 1.8 < P/VPA <= 2.5
        (2.6, "Crítico"),  # P/VPA > 2.5
        ("invalido", "Erro")  # Entrada inválida
    ]
    for vpa, condicao in testes_vpa:
        resultado = vpa_evaluator.avaliar(vpa, preco_acao)
        adicionar_resultado(resultado, "VPAEvaluator", f"avaliar (vpa={vpa}, preco_acao={preco_acao})")

    # 5. Testes para PLEvaluator
    pl_evaluator = PLEvaluator()
    testes_pl = [
        (-1, "Negativo"),  # P/L < 0
        (5, "Ótimo"),  # 0 <= P/L <= 10
        (12, "Bom"),  # 10 < P/L <= 15
        (18, "Moderado"),  # 15 < P/L <= 20
        (22, "Elevado"),  # 20 < P/L <= 25
        (30, "Excessivo"),  # P/L > 25
        ("invalido", "Erro")  # Entrada inválida
    ]
    for pl, condicao in testes_pl:
        resultado = pl_evaluator.avaliar(pl)
        adicionar_resultado(resultado, "PLEvaluator", f"avaliar (p_l={pl})")

    # 6. Testes para MargemBrutaEvaluator
    margem_bruta_evaluator = MargemBrutaEvaluator()
    testes_margem_bruta = [
        (-10, "Negativo"),  # Margem Bruta < 0%
        (10, "Baixo"),  # 0 <= Margem Bruta <= 20%
        (30, "Moderado"),  # 20 < Margem Bruta <= 40%
        (50, "Bom"),  # 40 < Margem Bruta <= 60%
        (70, "Ótimo"),  # Margem Bruta > 60%
        ("invalido", "Erro")  # Entrada inválida
    ]
    for margem, condicao in testes_margem_bruta:
        resultado = margem_bruta_evaluator.avaliar(margem)
        adicionar_resultado(resultado, "MargemBrutaEvaluator", f"avaliar (margem_bruta={margem})")

    # 7. Testes para PVPEvaluator
    pvp_evaluator = PVPEvaluator()
    testes_pvp = [
        (-1, "Negativo"),  # P/VP < 0
        (0.5, "Ótimo"),  # 0 <= P/VP <= 0.8
        (1.0, "Bom"),  # 0.8 < P/VP <= 1.2
        (1.5, "Moderado"),  # 1.2 < P/VP <= 1.8
        (2.0, "Elevado"),  # 1.8 < P/VP <= 2.5
        (3.0, "Alto"),  # 2.5 < P/VP <= 4
        (5.0, "Excessivo"),  # P/VP > 4
        ("invalido", "Erro")  # Entrada inválida
    ]
    for pvp, condicao in testes_pvp:
        resultado = pvp_evaluator.avaliar(pvp)
        adicionar_resultado(resultado, "PVPEvaluator", f"avaliar (p_vp={pvp})")

    return resultados


# Função para exibir resultados no console
def exibir_resultados(resultados):
    print("📊 Resultados das Avaliações")
    for i, resultado in enumerate(resultados, 1):
        print(f"\nResultado {i}:")
        print(f"Classe: {resultado['Classe']}")
        print(f"Método: {resultado['Metodo']}")
        print(f"Classificação: {resultado['classificacao']}")
        print(f"Faixa: {resultado['faixa']}")
        print(f"Descrição: {resultado['descricao']}")
        print(f"Definição: {resultado['definicao']}")
        print(f"Agrupador: {resultado['agrupador']}")
        print(f"Fórmula: {resultado['formula']}")
        print(f"Riscos: {resultado['riscos']}")
        print(f"Referência Cruzada: {resultado['referencia_cruzada']}")
        print(f"Recomendação: {resultado['recomendacao']}")
        print("-" * 60)


# Função para exportar resultados para Excel
def exportar_para_excel(resultados, nome_arquivo="resultados_avaliacao.xlsx"):
    df = pd.DataFrame(resultados)
    df.to_excel(nome_arquivo, index=False, engine='openpyxl')
    print(f"\n✅ Resultados exportados para '{nome_arquivo}'")


# Bloco principal
if __name__ == "__main__":
    # Coletar resultados
    resultados = coletar_resultados_avaliacao()

    # Exibir resultados no console
    exibir_resultados(resultados)

    # Exportar para Excel
    exportar_para_excel(resultados)