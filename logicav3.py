import pandas as pd
#from comoparador import LucroLiquidoEvaluator, EBITDAEvaluator, DividaBrutaEvaluator, VPAEvaluator, PLEvaluator, MargemBrutaEvaluator, PVPEvaluator, ResultadoIND
#from analiseativos import (MargemEBITEvaluator, MargemEBITDAEvaluator,GiroAtivoEvaluator,\
#                          ROICEvaluator, ROAEvaluator,ROEEvaluator,LucroLiquidoEvaluator,\
#                          EBITDAEvaluator, DividaBrutaEvaluator, VPAEvaluator, PLEvaluator, \
#                          MargemBrutaEvaluator, PVPEvaluator,MargemLiquidaEvaluator,DivLiquidaPatrimonioLiquidoEvaluator,\
#                          DivLiquidaEBITDAEvaluator,DivLiquidaEBITEvaluator,PLAtivosEvaluator,\
#                          LiquidezCorrenteEvaluator,DividendYieldEvaluator,PatrimonioLiquidoEvaluator
#                           )

from analiseativos import *

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
        (-1, "Crítico"),  # 'Dívida Bruta < 0',
        (0, "Ótimo"),  # 'Dívida Bruta = 0',
        (0.2, "Bom"),  # '0 < Dívida Bruta / Ativos <= 0.3',
        (0.4, "Moderado"),  #'0.3 < Dívida Bruta / Ativos <= 0.6',
        (0.7, "Ruim"),  # '0.6 < Dívida Bruta / Ativos <= 1.0',
        (1.8, "Crítico"),  # 'Dívida Bruta / Ativos > 1.0',
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
        (-10, "Crítico"),  # 'Margem Bruta < 0%',
        (10, "Ruim"),  # '0 <= Margem Bruta <= 20%',
        (30, "Moderado"),  # '20 < Margem Bruta <= 40%',
        (50, "Bom"),  # '40 < Margem Bruta <= 60%',
        (70, "Ótimo"),  # 'Margem Bruta > 60%',
        ("invalido", "Erro")  # Entrada inválida
    ]
    for margem, condicao in testes_margem_bruta:
        resultado = margem_bruta_evaluator.avaliar(margem)
        adicionar_resultado(resultado, "MargemBrutaEvaluator", f"avaliar (margem_bruta={margem})")

    # 7. Testes para PVPEvaluator
    PVPE_evaluator = PVPEvaluator()
    testes_PVPEvaluator = [
        (-1, "Crítico"),  # 'P/VP < 0',
        (0.5, "Ótimo"),  # '0 <= P/VP <= 0.8',
        (1.0, "Bom"),  # '0.8 < P/VP <= 1.2',
        (1.5, "Moderado"),  # '1.2 < P/VP <= 1.8',
        (2.0, "Ruim"),  # '1.8 < P/VP <= 2.5',
        (3.0, "Alto"),  # '2.5 < P/VP <= 4',
        (5.0, "Excessivo"),  # P/VP > 4
        ("invalido", "Erro")  # Entrada inválida
    ]
    for PVPE, condicao in testes_PVPEvaluator:
        resultado = PVPE_evaluator.avaliar(PVPE)
        adicionar_resultado(resultado, "PVPEvaluator", f"avaliar (p_vp={PVPE})")

     # 8. Testes para ROEEvaluator
    ROE_evaluator = ROEEvaluator()

    testes_ROE = [
            (-10, "Crítico"),  # ROE < 0%',
            (4, "Ruim"),  # '0 <= ROE <= 5%',
            (8, "Moderado"),  # 5 < ROE <= 15%',
            (16, "Bom"),  # '15 < ROE <= 25%',
            (26, "Ótimo"),  # 'ROE > 25%',
            ("invalido", "Erro")  # Entrada inválida
        ]
    for ROE, condicao in testes_ROE:
            resultado = ROE_evaluator.avaliar(ROE)
            adicionar_resultado(resultado, "ROEEvaluator", f"avaliar (lucro={ROE})")

     # 9. Testes para ROAEvaluator
    ROA_evaluator = ROAEvaluator()

    testes_ROA = [
                (-10, "Crítico"),  # 'ROA < 0%',
                (3, "Ruim"),  # ''0 <= ROA <= 3%',
                (4, "Moderado"),  # '3 < ROA <= 7%',
                (8, "Bom"),  # '7 < ROA <= 12%',
                (13, "Ótimo"),  # 'ROA > 12%',
                ("invalido", "Erro")  # Entrada inválida
            ]
    for ROA, condicao in testes_ROA:
                resultado = ROA_evaluator.avaliar(ROA)
                adicionar_resultado(resultado, "ROAEvaluator", f"avaliar (lucro={ROA})")
     # 10 . Testes para ROICEvaluator
    ROIC_evaluator = ROICEvaluator()

    testes_ROIC = [
                (-10, "Crítico"),  # 'ROIC < 0%',
                (3, "Ruim"),  # '0 <= ROIC <= 5%',
                (6, "Moderado"),  # '5 < ROIC <= 10%',
                (11, "Bom"),  # '10 < ROIC <= 15%',
                (16, "Ótimo"),  # 'ROIC > 15%',
                ("invalido", "Erro")  # Entrada inválida
            ]
    for ROIC, condicao in testes_ROIC:
                resultado = ROIC_evaluator.avaliar(ROIC)
                adicionar_resultado(resultado, "ROICEvaluator", f"avaliar (lucro={ROIC})")

     # 11 . Testes para GiroAtivoEvaluator
    GiroAtivo_evaluator = GiroAtivoEvaluator()

    testes_GiroAtivo = [
                (-10, "Crítico"),  # 'Giro do Ativo < 0',
                (0.4, "Ruim"),  # ''0 <= Giro do Ativo <= 0.5',
                (0.6, "Moderado"),  # '0.5 < Giro do Ativo <= 1.0',
                (1.1, "Bom"),  # '1.0 < Giro do Ativo <= 2.0',
                (16, "Ótimo"),  # 'Giro do Ativo > 2.0',
                ("invalido", "Erro")  # Entrada inválida
            ]
    for GiroAtivo, condicao in testes_GiroAtivo:
                resultado = GiroAtivo_evaluator.avaliar(GiroAtivo)
                adicionar_resultado(resultado, "GiroAtivoEvaluator", f"avaliar (lucro={GiroAtivo})")

     # 12 . Testes para MargemEBITDAEvaluator
    MargemEBITDA_evaluator = MargemEBITDAEvaluator()

    testes_MargemEBITDA = [
                (-10, "Crítico"),  # 'Margem EBITDA < 0%',
                (1, "Ruim"),  # ''0 <= Margem EBITDA <= 10%',
                (11, "Moderado"),  # '10 < Margem EBITDA <= 20%',
                (21, "Bom"),  # ''20 < Margem EBITDA <= 30%',
                (31, "Ótimo"),  # 'Margem EBITDA > 30%',
                ("invalido", "Erro")  # Entrada inválida
            ]
    for MargemEBITDA, condicao in testes_MargemEBITDA:
                resultado = MargemEBITDA_evaluator.avaliar(MargemEBITDA)
                adicionar_resultado(resultado, "MargemEBITDAEvaluator", f"avaliar (lucro={MargemEBITDA})")

    # 13 . Testes para MargemEBITEvaluator
    MargemEBITE_evaluator = MargemEBITEvaluator()

    testes_MargemEBITE = [
        (-10, "Crítico"),  # 'Margem EBIT < 0%',
        (1, "Ruim"),  # '0 <= Margem EBIT <= 5%',
        (11, "Moderado"),  # '5 < Margem EBIT <= 15%',
        (21, "Bom"),  # '15 < Margem EBIT <= 25%',
        (31, "Ótimo"),  # 'Margem EBIT > 25%',
        ("invalido", "Erro")  # Entrada inválida
    ]
    for MargemEBITE, condicao in testes_MargemEBITE:
        resultado = MargemEBITE_evaluator.avaliar(MargemEBITE)
        adicionar_resultado(resultado, "MargemEBITEvaluator", f"avaliar (lucro={MargemEBITE})")

        # 14 . Testes para MargemLiquidaEvaluator
        MargemLiquida_evaluator = MargemLiquidaEvaluator()

        testes_MargemLiquida = [
            (-10, "Crítico"),  # 'Margem Líquida < 0%',
            (1, "Ruim"),  # ''0 <= Margem Líquida <= 5%',
            (11, "Moderado"),  # '5 < Margem Líquida <= 15%',
            (21, "Bom"),  # '15 < Margem Líquida <= 25%',
            (31, "Ótimo"),  # 'Margem Líquida > 25%',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for MargemLiquida, condicao in testes_MargemLiquida:
            resultado = MargemLiquida_evaluator.avaliar(MargemLiquida)
            adicionar_resultado(resultado, "MargemLiquidaEvaluator", f"avaliar (lucro={MargemLiquida})")

        # 15 . Testes para DivLiquidaPatrimonioLiquido
        DivLiquidaPatrimonioLiquido_evaluator = DivLiquidaPatrimonioLiquidoEvaluator()

        testes_DivLiquidaPatrimonioLiquido= [
            (4, "Crítico"),  # 'Dívida Líquida / PL > 3',
            (2.1, "Ruim"),  # '2 < Dívida Líquida / PL <= 3',
            (1.1, "Moderado"),  # '1 < Dívida Líquida / PL <= 2',
            (0.1, "Bom"),  # '0.5 < Dívida Líquida / PL <= 1',
            (-1, "Ótimo"),  # ''Dívida Líquida / PL < 0',
            (1, "Muito Bom"),  # '''0 <= Dívida Líquida / PL <= 0.5',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for DivLiquidaPatrimonioLiquido, condicao in testes_DivLiquidaPatrimonioLiquido:
            resultado = DivLiquidaPatrimonioLiquido_evaluator.avaliar(DivLiquidaPatrimonioLiquido)
            adicionar_resultado(resultado, "DivLiquidaPatrimonioLiquidoEvaluator", f"avaliar (lucro={DivLiquidaPatrimonioLiquido})")

        # 16 . Testes para DivLiquidaEBITDAEvaluator
        DivLiquidaEBITDA_evaluator = DivLiquidaEBITDAEvaluator()

        testes_DivLiquidaEBITDA = [
            (5, "Crítico"),  # ''Dívida Líquida / EBITDA > 4',
            (3.1, "Ruim"),  # '3 < Dívida Líquida / EBITDA <= 4',
            (2.1, "Moderado"),  # '2 < Dívida Líquida / EBITDA <= 3',
            (1.1, "Bom"),  # '1 < Dívida Líquida / EBITDA <= 2',
            (-21, "Muito Bom"),  # '0 <= Dívida Líquida / EBITDA <= 1',
            (-1, "Ótimo"),  # 'Dívida Líquida / EBITDA < 0',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for DivLiquidaEBITDA, condicao in testes_DivLiquidaEBITDA:
            resultado = DivLiquidaEBITDA_evaluator.avaliar(DivLiquidaEBITDA)
            adicionar_resultado(resultado, "DivLiquidaEBITDAEvaluator",
                                f"avaliar (lucro={DivLiquidaEBITDA})")

            # 17 . Testes para DivLiquidaEBITDAEvaluator
        DivLiquidaEBIT_evaluator = DivLiquidaEBITEvaluator()

        testes_DivLiquidaEBIT = [
            (5, "Crítico"),  # ''4.5 < Dívida Líquida / EBIT <= 6',
            (3.1, "Ruim"),  # '3 < Dívida Líquida / EBIT <= 4.5',
            (3, "Moderado"),  # '1.5 < Dívida Líquida / EBIT <= 3',
            (1.5, "Bom"),  # '0 <= Dívida Líquida / EBIT <= 1.5',
            (7, "Muito Crítico"),  # 'Dívida Líquida / EBIT > 6',
            (-1, "Ótimo"),  # 'Dívida Líquida / EBIT < 0',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for DivLiquidaEBIT, condicao in testes_DivLiquidaEBIT:
            resultado = DivLiquidaEBIT_evaluator.avaliar(DivLiquidaEBIT)
            adicionar_resultado(resultado, "DivLiquidaEBIT",
                                f"avaliar (lucro={DivLiquidaEBIT})")
            # 18 . Testes para PLAtivosEvaluator
        PLAtivos_evaluator = PLAtivosEvaluator()

        testes_PLAtivos = [
            (-5, "Crítico"),  # 'PL/Ativos < 0',
            (0.1, "Ruim"),  # '0 <= PL/Ativos <= 0.2',
            (0.2, "Moderado"),  # ''0.2 < PL/Ativos <= 0.4',
            (0.4, "Bom"),  # '0.4 < PL/Ativos <= 0.6',
            (0.7, "Ótimo"),  # 'PL/Ativos > 0.6',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for PLAtivos, condicao in testes_PLAtivos:
            resultado = PLAtivos_evaluator.avaliar(PLAtivos)
            adicionar_resultado(resultado, "PLAtivos",
                                f"avaliar (lucro={PLAtivosEvaluator})")

        # 19 . Testes para DividendYieldEvaluator
        DividendYieldEvaluator_evaluator = DividendYieldEvaluator()

        testes_DividendYieldEvaluator = [
            (-5, "Muito Crítico"),  # Dividend Yield < 0%',
            (0, "Crítico"),  # 'Dividend Yield = 0%',
            (1, "Ruim"),  # '0 < Dividend Yield <= 2%',
            (2, "Moderado"),  # '2 < Dividend Yield <= 4%',
            (5, "Bom"),  # '4 < Dividend Yield <= 6%',
            (7, "Ótimo"),  # 'Dividend Yield > 6%',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for DividendYield, condicao in testes_DividendYieldEvaluator:
            resultado = DividendYieldEvaluator_evaluator.avaliar(DividendYield)
            adicionar_resultado(resultado, "DividendYieldEvaluator",
                                f"avaliar (lucro={DividendYield})")

            # 20 . Testes para LiquidezCorrenteEvaluator
        LiquidezCorrenteEvaluator_evaluator = LiquidezCorrenteEvaluator()

        testes_LiquidezCorrenteEvaluator = [
                (-5, "Crítico"),  # 'Liquidez Corrente < 0',
                (0.1, "Ruim"),  # '0 <= Liquidez Corrente < 0.8',
                (0.9, "Moderado"),  # '0.8 <= Liquidez Corrente < 1.2',
                (1.4, "Bom"),  # '1.2 <= Liquidez Corrente <= 2.0',
                (2.1, "Ótimo"),  # ''Liquidez Corrente > 2.0',
                ("invalido", "Erro")  # Entrada inválida
            ]
        for LiquidezCorrente, condicao in testes_LiquidezCorrenteEvaluator:
                resultado = LiquidezCorrenteEvaluator_evaluator.avaliar(LiquidezCorrente)
                adicionar_resultado(resultado, "LiquidezCorrenteEvaluator",
                                    f"avaliar (lucro={LiquidezCorrente})")
                # 21 . Testes para LiquidezCorrenteEvaluator
        PatrimonioLiquidoEvaluator_evaluator = PatrimonioLiquidoEvaluator()

        testes_PatrimonioLiquidoEvaluator = [
            (-5, "Crítico"),  # 'Patrimônio Líquido < 0',
            (0.1, "Ruim"),  # '0 <= Patrimônio Líquido / Ativos <= 0.2',
            (0.2, "Moderado"),  # '0.2 < Patrimônio Líquido / Ativos <= 0.4',
            (0.5, "Bom"),  # 0.4 < Patrimônio Líquido / Ativos <= 0.6',
            (1, "Ótimo"),  # 'Patrimônio Líquido / Ativos > 0.6',
            ("invalido", "Erro")  # Entrada inválida
        ]
        for PatrimonioLiquido, condicao in testes_PatrimonioLiquidoEvaluator:
            resultado = PatrimonioLiquidoEvaluator_evaluator.avaliar(PatrimonioLiquido)
            adicionar_resultado(resultado, "PatrimonioLiquidoEvaluator",
                                f"avaliar (lucro={PatrimonioLiquido})")

    return resultados

#



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