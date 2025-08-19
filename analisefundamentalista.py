"""
analisefundamentalista_1.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Dívida Líquida/EBITDA, Margem EBITDA, ROA, Payout de Dividendos.
"""


def evaluate_divida_liquida_ebitda(divida_liquida_ebitda):
    """
    Avalia a Dívida Líquida/EBITDA com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/EBITDA < 0: Fora da faixa (sem dívida líquida ou EBITDA negativo)
    - 0 ≤ Dívida Líquida/EBITDA ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida Líquida/EBITDA ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida Líquida/EBITDA ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida Líquida/EBITDA ≤ 4: Péssimo (endividamento muito alto)
    - Dívida Líquida/EBITDA > 4: Crítico (endividamento excessivo, risco elevado)
    """
    definicao = """
    A Dívida Líquida/EBITDA mede a capacidade da empresa de pagar sua dívida líquida com base no EBITDA,
    calculada como (Dívida Total - Caixa e Equivalentes) / EBITDA. É um indicador chave de alavancagem
    financeira, mostrando quantos anos a empresa levaria para quitar sua dívida líquida com sua geração
    de caixa operacional. Um valor baixo indica saúde financeira, enquanto um valor alto sugere risco
    financeiro elevado. É amplamente utilizado em setores intensivos em capital, como mineração e energia.
    """
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/EBITDA = (Dívida Total - Caixa e Equivalentes) / EBITDA'

    try:
        if divida_liquida_ebitda < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida/EBITDA < 0',
                'descricao': """
                Um valor negativo indica que a empresa não possui dívida líquida (caixa excede a dívida)
                ou que o EBITDA é negativo. Empresas como a Totvs (TOTS3), com forte geração de caixa, podem
                apresentar valores negativos em períodos de alta liquidez. Para investidores, isso pode ser
                positivo, sugerindo solidez financeira, mas também pode indicar ineficiência na alocação de
                capital, como excesso de caixa ocioso. Análises complementares, como ROIC e fluxo de caixa livre,
                são recomendadas para avaliar a eficiência do uso do caixa.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_liquida_ebitda <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Líquida/EBITDA <= 1',
                'descricao': """
                Um valor entre 0 e 1 reflete endividamento muito baixo, indicando que a empresa pode quitar
                sua dívida líquida rapidamente com sua geração de caixa. Empresas como a Vale (VALE3) em períodos
                de alta nos preços de minério de ferro frequentemente operam nessa faixa. Para investidores,
                essa faixa é atrativa, pois sugere baixo risco financeiro e flexibilidade para investimentos ou
                dividendos. É importante verificar a consistência do EBITDA e a composição da dívida.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_liquida_ebitda <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida Líquida/EBITDA <= 2',
                'descricao': """
                Um valor entre 1 e 2 indica endividamento aceitável, com a empresa mantendo um equilíbrio entre
                dívida e geração de caixa. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa
                faixa devido à sua gestão financeira eficiente. Para investidores, essa faixa sugere risco moderado,
                com a empresa capaz de suportar oscilações econômicas sem grandes pressões. É importante avaliar
                a estrutura da dívida (curto vs. longo prazo) e a geração de fluxo de caixa livre.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_liquida_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Líquida/EBITDA <= 3',
                'descricao': """
                Um valor entre 2 e 3 sugere endividamento elevado, indicando que a empresa levaria um tempo
                considerável para quitar sua dívida líquida com o EBITDA. Isso é comum em setores intensivos em
                capital, como a Petrobras (PETR4) em períodos de investimentos pesados. Para investidores, essa
                faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros ou quedas na receita.
                Análise de fluxo de caixa e covenants de dívida é recomendada.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_liquida_ebitda <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida Líquida/EBITDA <= 4',
                'descricao': """
                Um valor entre 3 e 4 reflete endividamento muito alto, indicando risco significativo de pressão
                financeira. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises, enfrentando dificuldades
                para gerenciar dívidas elevadas. Para investidores, essa faixa é preocupante, exigindo análise detalhada
                da estrutura de capital, planos de desalavancagem e fluxo de caixa operacional.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_liquida_ebitda > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Líquida/EBITDA > 4',
                'descricao': """
                Um valor acima de 4 indica endividamento excessivo, sugerindo que a empresa depende fortemente de
                dívidas em relação à sua geração de caixa. Isso é alarmante e típico de empresas em dificuldades
                financeiras, como a Gol (GOLL4) em períodos de crise no setor aéreo. Para investidores, essa faixa é
                de altíssimo risco, com possibilidade de reestruturação ou insolvência. A análise deve focar na
                capacidade de geração de caixa, estratégias de redução de dívida e covenants financeiros.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f"""
            Ocorreu um erro ao processar a Dívida Líquida/EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a dívida líquida e o EBITDA estejam corretos e sejam valores numéricos válidos.
            """,
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_margem_ebitda(margem_ebitda):
    '''
    Avalia a Margem EBITDA com base em faixas definidas para o mercado brasileiro:
    - Margem EBITDA < 0%: Crítico (prejuízo operacional, risco elevado)
    - 0% ≤ Margem EBITDA ≤ 10%: Ruim (rentabilidade operacional baixa)
    - 10% < Margem EBITDA ≤ 20%: Moderado (rentabilidade operacional aceitável)
    - 20% < Margem EBITDA ≤ 30%: Ótimo (rentabilidade operacional robusta)
    - Margem EBITDA > 30%: Fora da faixa (rentabilidade operacional excepcional)
    '''
    definicao = '''
    A Margem EBITDA mede a proporção da receita bruta que se converte em EBITDA, calculada como
    (EBITDA / Receita Bruta). É um indicador de rentabilidade operacional que reflete a eficiência da
    empresa em gerar caixa antes de juros, impostos, depreciação e amortização. Uma margem alta sugere
    forte geração de caixa operacional, enquanto uma margem baixa ou negativa indica ineficiência ou
    prejuízo. É especialmente útil em setores com alta intensidade de capital, como energia e mineração.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem EBITDA = EBITDA / Receita Bruta'

    try:
        if margem_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem EBITDA < 0%',
                'descricao': '''
                Uma Margem EBITDA negativa indica que a empresa está gerando prejuízo operacional, com custos
                superando a receita antes de juros, impostos, depreciação e amortização. Isso é comum em empresas
                em crise, como a Oi (OIBR3) durante períodos de reestruturação. Para investidores, essa faixa é um
                alerta de risco elevado, pois reflete dificuldades operacionais graves. A análise deve focar na
                estrutura de custos, estratégias de recuperação e tendências setoriais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_ebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Margem EBITDA <= 10%',
                'descricao': '''
                Uma Margem EBITDA entre 0% e 10% reflete rentabilidade operacional baixa, indicando que a empresa
                tem dificuldade em converter receita em caixa operacional significativo. Isso é comum em setores com
                margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere
                risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações econômicas.
                Análise de redução de custos e crescimento da receita é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < margem_ebitda <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '10% < Margem EBITDA <= 20%',
                'descricao': '''
                Uma Margem EBITDA entre 10% e 20% indica rentabilidade operacional aceitável, típico de empresas
                com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio
                entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante
                avaliar a sustentabilidade da margem e o impacto de fatores macroeconômicos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < margem_ebitda <= 30:
            return {
                'classificacao': 'Ótimo',
                'faixa': '20% < Margem EBITDA <= 30%',
                'descricao': '''
                Uma Margem EBITDA entre 20% e 30% reflete rentabilidade operacional robusta, indicando que a empresa
                converte uma proporção significativa de sua receita em caixa operacional. Empresas como a Ambev (ABEV3),
                com forte controle de custos, frequentemente apresentam margem nessa faixa. Para investidores, essa faixa
                é atrativa, pois sugere solidez financeira e potencial para dividendos ou reinvestimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_ebitda > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem EBITDA > 30%',
                'descricao': '''
                Uma Margem EBITDA acima de 30% é excepcional, indicando que a empresa converte uma proporção
                extremamente alta de sua receita em caixa operacional. Isso é raro, mas pode ocorrer em empresas
                com alta eficiência operacional, como a Weg (WEGE3) em períodos de forte desempenho. Para investidores,
                essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis
                a longo prazo. A análise deve focar na escalabilidade do modelo de negócios e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o EBITDA e a receita bruta estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_roa(roa):
    '''
    Avalia o Retorno sobre Ativos (ROA) com base em faixas definidas para o mercado brasileiro:
    - ROA < 0%: Crítico (prejuízo, destruição de valor)
    - 0% ≤ ROA ≤ 5%: Ruim (retorno baixo, ineficiência)
    - 5% < ROA ≤ 10%: Moderado (retorno aceitável)
    - 10% < ROA ≤ 15%: Ótimo (retorno robusto)
    - ROA > 15%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre Ativos (ROA) mede a eficiência da empresa em gerar lucro com seus ativos totais,
    calculado como (Lucro Líquido / Ativos Totais). É um indicador de rentabilidade que reflete como
    a empresa utiliza seus recursos para gerar retorno. Um ROA alto indica eficiência operacional, enquanto
    um valor baixo ou negativo sugere ineficiência ou prejuízo. É útil para comparar empresas dentro do
    mesmo setor, mas deve ser analisado com margem líquida e giro de ativos.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROA = Lucro Líquido / Ativos Totais'

    try:
        if roa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROA < 0%',
                'descricao': '''
                Um ROA negativo indica que a empresa está gerando prejuízo, destruindo valor com seus ativos.
                Isso é comum em empresas em crise, como a Gol (GOLL4) durante períodos de baixa demanda no setor
                aéreo. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras
                graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roa <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROA <= 5%',
                'descricao': '''
                Um ROA entre 0% e 5% reflete retorno baixo, indicando ineficiência na utilização dos ativos.
                Isso é comum em setores com alta intensidade de capital ou margens apertadas, como varejo
                (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa
                pode ser vulnerável a oscilações econômicas. Análise de giro de ativos e margem líquida é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < roa <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < ROA <= 10%',
                'descricao': '''
                Um ROA entre 5% e 10% indica retorno aceitável, típico de empresas com eficiência moderada na
                utilização de ativos. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio
                entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < roa <= 15:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < ROA <= 15%',
                'descricao': '''
                Um ROA entre 10% e 15% reflete retorno robusto, indicando que a empresa utiliza seus ativos de
                forma eficiente para gerar lucro. Empresas como a Ambev (ABEV3), com forte gestão operacional,
                frequentemente apresentam ROA nessa faixa. Para investidores, essa faixa é atrativa, pois sugere
                solidez financeira e potencial para crescimento sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roa > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROA > 15%',
                'descricao': '''
                Um ROA acima de 15% é excepcional, indicando que a empresa gera retornos extremamente altos com
                seus ativos. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg
                (WEGE3) em períodos de forte desempenho. Para investidores, essa faixa é altamente atrativa, mas
                exige cautela, pois retornos tão altos podem não ser sustentáveis. A análise deve focar na
                escalabilidade do modelo de negócios e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o lucro líquido e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_dividend_payout(payout):
    '''
    Avalia o Payout de Dividendos com base em faixas definidas para o mercado brasileiro:
    - Payout < 0%: Fora da faixa (sem dividendos ou prejuízo)
    - 0% ≤ Payout ≤ 25%: Ruim (distribuição baixa de dividendos)
    - 25% < Payout ≤ 50%: Moderado (distribuição aceitável de dividendos)
    - 50% < Payout ≤ 75%: Ótimo (distribuição robusta de dividendos)
    - Payout > 75%: Crítico (distribuição excessiva, risco de sustentabilidade)
    '''
    definicao = '''
    O Payout de Dividendos mede a proporção do lucro líquido distribuído como dividendos, calculado como
    (Dividendos Pagos / Lucro Líquido). É um indicador que reflete a política de distribuição de lucros da
    empresa, mostrando quanto do lucro é retornado aos acionistas versus reinvestido no negócio. Um payout
    alto é atrativo para investidores focados em renda, mas pode indicar menor reinvestimento. Um payout baixo
    pode sugerir crescimento, mas também insatisfação para investidores de dividendos.
    '''
    agrupador = 'Dividendos'
    formula = 'Payout = Dividendos Pagos / Lucro Líquido'

    try:
        if payout < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Payout < 0%',
                'descricao': '''
                Um Payout negativo ou zero indica que a empresa não distribui dividendos, seja por prejuízo ou
                por reinvestir todo o lucro no negócio. Isso é comum em empresas em crescimento, como o Nubank
                (NUBR33), ou em crise, como a Oi (OIBR3). Para investidores focados em renda, essa faixa é
                desvantajosa, mas pode ser positiva para quem busca crescimento. A análise deve focar no motivo da
                ausência de dividendos (crescimento ou dificuldades financeiras).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= payout <= 25:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Payout <= 25%',
                'descricao': '''
                Um Payout entre 0% e 25% reflete distribuição baixa de dividendos, indicando que a empresa prioriza
                reinvestimento em vez de retorno aos acionistas. Isso é comum em empresas em expansão, como a Magazine
                Luiza (MGLU3). Para investidores focados em renda, essa faixa é pouco atrativa, mas pode ser positiva
                para quem busca crescimento. É importante analisar o potencial de crescimento e a eficiência do
                reinvestimento (ex.: ROIC).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 25 < payout <= 50:
            return {
                'classificacao': 'Moderado',
                'faixa': '25% < Payout <= 50%',
                'descricao': '''
                Um Payout entre 25% e 50% indica distribuição aceitável de dividendos, com equilíbrio entre retorno
                aos acionistas e reinvestimento. No Brasil, empresas como a Vale (VALE3) frequentemente operam nessa
                faixa em períodos de lucros estáveis. Para investidores, essa faixa é adequada para quem busca renda
                moderada com potencial de crescimento. É importante avaliar a consistência dos lucros e a política
                de dividendos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 50 < payout <= 75:
            return {
                'classificacao': 'Ótimo',
                'faixa': '50% < Payout <= 75%',
                'descricao': '''
                Um Payout entre 50% e 75% reflete distribuição robusta de dividendos, indicando que a empresa retorna
                uma parte significativa de seus lucros aos acionistas. Empresas como a Engie Brasil (EGIE3), do setor
                de energia, frequentemente apresentam payout nessa faixa. Para investidores focados em renda, essa faixa
                é atrativa, pois sugere estabilidade e retorno consistente. No entanto, é importante verificar a
                sustentabilidade dos dividendos com base no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif payout > 75:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Payout > 75%',
                'descricao': '''
                Um Payout acima de 75% indica distribuição excessiva de dividendos, sugerindo que a empresa está
                retornando quase todo o lucro aos acionistas, com pouco reinvestimento. Isso pode ocorrer em empresas
                maduras, como a Taesa (TAEE11), mas é arriscado, pois pode comprometer o crescimento futuro. Para
                investidores, essa faixa exige cautela, pois dividendos altos podem não ser sustentáveis. A análise deve
                focar no fluxo de caixa livre e nas perspectivas de crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Payout de Dividendos: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o lucro líquido for zero, o que impede o cálculo. Verifique os dados
            de entrada, assegurando que os dividendos pagos e o lucro líquido estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

    """
    analisefundamentalista_2.py
    Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
    e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
    Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
    Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
    Indicadores incluídos: Crescimento da Receita, Liquidez Seca, Margem Operacional, P/EBITDA.
    """

    def evaluate_crescimento_receita(crescimento_receita):
        '''
        Avalia o Crescimento da Receita com base em faixas definidas para o mercado brasileiro:
        - Crescimento Receita < 0%: Crítico (redução de receita, risco elevado)
        - 0% ≤ Crescimento Receita ≤ 5%: Ruim (crescimento baixo ou estagnação)
        - 5% < Crescimento Receita ≤ 10%: Moderado (crescimento aceitável)
        - 10% < Crescimento Receita ≤ 20%: Ótimo (crescimento robusto)
        - Crescimento Receita > 20%: Fora da faixa (crescimento excepcional)
        '''
        definicao = '''
        O Crescimento da Receita mede a taxa anual de aumento da receita bruta, calculada como
        ((Receita Final / Receita Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador de
        crescimento que reflete a capacidade da empresa de expandir suas vendas. Um crescimento alto sugere
        expansão bem-sucedida, enquanto um valor baixo ou negativo indica estagnação ou declínio. É especialmente
        relevante em setores de alto crescimento, como tecnologia, mas deve ser analisado com margens de lucro
        e fluxo de caixa.
        '''
        agrupador = 'Crescimento'
        formula = 'Crescimento Receita = ((Receita Final / Receita Inicial)^(1/n) - 1)'

        try:
            if crescimento_receita < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Crescimento Receita < 0%',
                    'descricao': '''
                    Um Crescimento da Receita negativo indica que a empresa está enfrentando uma redução nas vendas,
                    sugerindo dificuldades de mercado ou operacionais. Isso é comum em empresas em crise, como a Gol
                    (GOLL4) durante períodos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado,
                    pois reflete desafios significativos. A análise deve focar nas causas da queda (ex.: concorrência,
                    crise setorial) e estratégias de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= crescimento_receita <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= Crescimento Receita <= 5%',
                    'descricao': '''
                    Um Crescimento da Receita entre 0% e 5% reflete crescimento baixo ou estagnação, indicando que a
                    empresa tem dificuldade em expandir suas vendas. Isso é comum em setores maduros, como varejo
                    (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa
                    pode ser vulnerável a oscilações econômicas. Análise de estratégias de crescimento e margens de lucro
                    é recomendada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < crescimento_receita <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < Crescimento Receita <= 10%',
                    'descricao': '''
                    Um Crescimento da Receita entre 5% e 10% indica crescimento aceitável, típico de empresas com
                    expansão moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido
                    à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre
                    crescimento e segurança, sendo adequada para quem busca retornos consistentes.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < crescimento_receita <= 20:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '10% < Crescimento Receita <= 20%',
                    'descricao': '''
                    Um Crescimento da Receita entre 10% e 20% reflete crescimento robusto, indicando que a empresa está
                    expandindo suas vendas de forma significativa. Empresas como a Magazine Luiza (MGLU3), em períodos
                    de forte crescimento no e-commerce, frequentemente apresentam crescimento nessa faixa. Para investidores,
                    essa faixa é atrativa, pois sugere potencial de valorização. É importante verificar a sustentabilidade
                    do crescimento com base em margens e fluxo de caixa.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif crescimento_receita > 20:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Crescimento Receita > 20%',
                    'descricao': '''
                    Um Crescimento da Receita acima de 20% é excepcional, indicando expansão extremamente rápida das
                    vendas. Isso é raro, mas pode ocorrer em empresas em setores de alto crescimento, como o Nubank
                    (NUBR33) em sua fase inicial. Para investidores, essa faixa é altamente atrativa, mas exige cautela,
                    pois crescimentos tão altos podem não ser sustentáveis. A análise deve focar na escalabilidade do
                    modelo de negócios e barreiras de entrada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar o Crescimento da Receita: {str(e)}. Isso pode ter acontecido se o valor
                fornecido não for numérico ou se a receita inicial for zero, o que impede o cálculo. Verifique os dados
                de entrada, assegurando que as receitas inicial e final estejam corretas e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_liquidez_seca(liquidez_seca):
        '''
        Avalia a Liquidez Seca com base em faixas definidas para o mercado brasileiro:
        - Liquidez Seca < 0.3: Crítico (dificuldade extrema em pagar obrigações sem estoques)
        - 0.3 ≤ Liquidez Seca ≤ 0.7: Ruim (capacidade limitada de pagar obrigações sem estoques)
        - 0.7 < Liquidez Seca ≤ 1.2: Moderado (capacidade aceitável de pagar obrigações sem estoques)
        - 1.2 < Liquidez Seca ≤ 1.8: Ótimo (boa capacidade de pagar obrigações sem estoques)
        - Liquidez Seca > 1.8: Fora da faixa (excesso de liquidez, possível ineficiência)
        '''
        definicao = '''
        A Liquidez Seca mede a capacidade da empresa de pagar suas obrigações de curto prazo sem depender da
        venda de estoques, calculada como (Ativo Circulante - Estoques) / Passivo Circulante. É um indicador
        conservador de liquidez, útil em setores onde os estoques são menos líquidos, como indústria pesada.
        Um valor alto sugere solidez financeira, enquanto um valor baixo indica risco de inadimplência.
        '''
        agrupador = 'Liquidez'
        formula = 'Liquidez Seca = (Ativo Circulante - Estoques) / Passivo Circulante'

        try:
            if liquidez_seca < 0.3:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Liquidez Seca < 0.3',
                    'descricao': '''
                    Uma Liquidez Seca abaixo de 0.3 indica dificuldade extrema em pagar obrigações de curto prazo sem
                    depender da venda de estoques, sugerindo risco elevado de inadimplência. Isso é comum em empresas
                    em crise, como a Oi (OIBR3) durante reestruturações. Para investidores, essa faixa é um alerta grave,
                    pois reflete problemas de liquidez severos. A análise deve focar na gestão de caixa e estratégias de
                    recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.3 <= liquidez_seca <= 0.7:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0.3 <= Liquidez Seca <= 0.7',
                    'descricao': '''
                    Uma Liquidez Seca entre 0.3 e 0.7 reflete capacidade limitada de pagar obrigações de curto prazo
                    sem estoques, indicando dependência de conversão de ativos em caixa. Isso é comum em setores com
                    estoques elevados, como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco
                    moderado, exigindo análise da qualidade dos ativos circulantes e do ciclo operacional.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.7 < liquidez_seca <= 1.2:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '0.7 < Liquidez Seca <= 1.2',
                    'descricao': '''
                    Uma Liquidez Seca entre 0.7 e 1.2 indica capacidade aceitável de pagar obrigações de curto prazo
                    sem depender de estoques. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                    devido à sua gestão eficiente de caixa. Para investidores, essa faixa sugere equilíbrio entre liquidez
                    e eficiência, sendo adequada para quem busca segurança financeira de curto prazo.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 1.2 < liquidez_seca <= 1.8:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '1.2 < Liquidez Seca <= 1.8',
                    'descricao': '''
                    Uma Liquidez Seca entre 1.2 e 1.8 reflete boa capacidade de pagar obrigações de curto prazo sem
                    depender de estoques, indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente
                    apresentam liquidez nessa faixa devido à sua forte geração de caixa. Para investidores, essa faixa
                    é atrativa, sugerindo resiliência a choques financeiros de curto prazo.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif liquidez_seca > 1.8:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Liquidez Seca > 1.8',
                    'descricao': '''
                    Uma Liquidez Seca acima de 1.8 indica excesso de liquidez, com ativos circulantes (excluindo estoques)
                    muito superiores às obrigações de curto prazo. Isso pode ocorrer em empresas com alta geração de caixa,
                    como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa pode
                    ser positiva, mas também pode indicar ineficiência na alocação de capital, como excesso de caixa ocioso.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar a Liquidez Seca: {str(e)}. Isso pode ter acontecido se o valor fornecido
                não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os dados de
                entrada, assegurando que o ativo circulante, estoques e passivo circulante estejam corretos e sejam
                valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_margem_operacional(margem_operacional):
        '''
        Avalia a Margem Operacional com base em faixas definidas para o mercado brasileiro:
        - Margem Operacional < 0%: Crítico (prejuízo operacional, risco elevado)
        - 0% ≤ Margem Operacional ≤ 5%: Ruim (rentabilidade operacional baixa)
        - 5% < Margem Operacional ≤ 15%: Moderado (rentabilidade operacional aceitável)
        - 15% < Margem Operacional ≤ 25%: Ótimo (rentabilidade operacional robusta)
        - Margem Operacional > 25%: Fora da faixa (rentabilidade operacional excepcional)
        '''
        definicao = '''
        A Margem Operacional mede a proporção da receita bruta que se converte em lucro operacional,
        calculada como (Lucro Operacional / Receita Bruta). É um indicador de rentabilidade que reflete a
        eficiência da empresa em gerenciar custos operacionais antes de juros e impostos. Uma margem alta
        sugere forte desempenho operacional, enquanto uma margem baixa ou negativa indica ineficiência.
        '''
        agrupador = 'Rentabilidade'
        formula = 'Margem Operacional = Lucro Operacional / Receita Bruta'

        try:
            if margem_operacional < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Margem Operacional < 0%',
                    'descricao': '''
                    Uma Margem Operacional negativa indica prejuízo operacional, sugerindo que a empresa não consegue
                    cobrir seus custos operacionais com a receita. Isso é comum em empresas em crise, como a CSN (CSNA3)
                    durante quedas de preços de commodities. Para investidores, essa faixa é um alerta de risco elevado,
                    exigindo análise detalhada da estrutura de custos e estratégias de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= margem_operacional <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= Margem Operacional <= 5%',
                    'descricao': '''
                    Uma Margem Operacional entre 0% e 5% reflete rentabilidade operacional baixa, indicando dificuldade
                    em gerar lucro significativo a partir das operações. Isso é comum em setores com margens apertadas,
                    como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado,
                    exigindo análise de redução de custos e potencial de melhoria da margem.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < margem_operacional <= 15:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < Margem Operacional <= 15%',
                    'descricao': '''
                    Uma Margem Operacional entre 5% e 15% indica rentabilidade operacional aceitável, típico de empresas
                    com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                    devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere equilíbrio entre
                    rentabilidade e segurança.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 15 < margem_operacional <= 25:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '15% < Margem Operacional <= 25%',
                    'descricao': '''
                    Uma Margem Operacional entre 15% e 25% reflete rentabilidade operacional robusta, indicando que a
                    empresa converte uma proporção significativa de sua receita em lucro operacional. Empresas como a
                    Ambev (ABEV3) frequentemente apresentam margem nessa faixa devido à sua eficiência operacional.
                    Para investidores, essa faixa é atrativa, sugerindo solidez financeira.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif margem_operacional > 25:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Margem Operacional > 25%',
                    'descricao': '''
                    Uma Margem Operacional acima de 25% é excepcional, indicando que a empresa converte uma proporção
                    extremamente alta de sua receita em lucro operacional. Isso pode ocorrer em empresas com alta
                    eficiência, como a Weg (WEGE3). Para investidores, essa faixa é atrativa, mas exige cautela, pois
                    margens tão altas podem não ser sustentáveis. A análise deve focar na escalabilidade e barreiras de
                    entrada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar a Margem Operacional: {str(e)}. Isso pode ter acontecido se o valor
                fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados
                de entrada, assegurando que o lucro operacional e a receita bruta estejam corretos e sejam valores
                numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_p_ebitda(p_ebitda):
        '''
        Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
        - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
        - 0 ≤ P/EBITDA ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
        - 5 < P/EBITDA ≤ 8: Moderado (valuation justo)
        - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
        - 12 < P/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
        - P/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado)
        '''
        definicao = '''
        O Preço/EBITDA compara o preço da ação (ou valor de mercado da empresa) ao EBITDA, calculado como
        (Preço da Ação * Número de Ações) / EBITDA ou (Valor de Mercado + Dívida Líquida) / EBITDA para EV/EBITDA.
        É um indicador de valuation que avalia se a empresa está cara ou barata em relação à sua geração de
        caixa operacional. Um valor baixo sugere subvalorização, enquanto um valor alto indica sobrevalorização.
        É útil em setores com alta intensidade de capital, mas menos eficaz em empresas com EBITDA negativo.
        '''
        agrupador = 'Valuation'
        formula = 'P/EBITDA = (Preço da Ação * Número de Ações) / EBITDA'

        try:
            if p_ebitda < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'P/EBITDA < 0',
                    'descricao': '''
                    Um P/EBITDA negativo indica que a empresa tem EBITDA negativo, sugerindo prejuízo operacional.
                    Isso é comum em empresas em crise, como a Oi (OIBR3) durante reestruturações. Para investidores,
                    essa faixa é um alerta de risco elevado, exigindo análise detalhada da saúde financeira e estratégias
                    de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= p_ebitda <= 5:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '0 <= P/EBITDA <= 5',
                    'descricao': '''
                    Um P/EBITDA entre 0 e 5 sugere que a ação está subvalorizada em relação à sua geração de caixa,
                    indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de
                    baixa, como a Vale (VALE3). Para investidores, essa faixa é atrativa, mas é importante verificar a
                    sustentabilidade do EBITDA.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < p_ebitda <= 8:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5 < P/EBITDA <= 8',
                    'descricao': '''
                    Um P/EBITDA entre 5 e 8 reflete um valuation justo, típico de empresas com geração de caixa estável.
                    No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores, essa
                    faixa sugere equilíbrio entre preço e fundamentos, sendo adequada para retornos consistentes.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 8 < p_ebitda <= 12:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '8 < P/EBITDA <= 12',
                    'descricao': '''
                    Um P/EBITDA entre 8 e 12 sugere que a ação está sobrevalorizada, indicando que o mercado espera
                    crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos
                    de expansão. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar
                    sem crescimento robusto.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 12 < p_ebitda <= 15:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '12 < P/EBITDA <= 15',
                    'descricao': '''
                    Um P/EBITDA entre 12 e 15 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                    prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/EBITDA nessa faixa em momentos
                    de otimismo. Para investidores, essa faixa é de alto risco, exigindo análise de crescimento e
                    escalabilidade do modelo de negócios.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif p_ebitda > 15:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'P/EBITDA > 15',
                    'descricao': '''
                    Um P/EBITDA acima de 15 é extremamente elevado, geralmente associado a empresas com altíssimas
                    expectativas de crescimento, como o Nubank (NUBR33) após sua estreia na bolsa. Para investidores,
                    essa faixa é de altíssimo risco, pois reflete mais especulação do que fundamentos. A análise deve
                    focar em projeções de longo prazo e comparação com peers globais.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar o P/EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não
                for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando
                que o preço da ação, número de ações e EBITDA estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }


"""
analisefundamentalista_3.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Free Cash Flow Yield, Crescimento do Lucro, Dívida/Patrimônio, Margem Líquida Crescimento.
"""


def evaluate_free_cash_flow_yield(fcf_yield):
    '''
    Avalia o Free Cash Flow Yield com base em faixas definidas para o mercado brasileiro:
    - FCF Yield < 0%: Crítico (fluxo de caixa livre negativo, risco elevado)
    - 0% ≤ FCF Yield ≤ 3%: Ruim (fluxo de caixa livre baixo)
    - 3% < FCF Yield ≤ 6%: Moderado (fluxo de caixa livre aceitável)
    - 6% < FCF Yield ≤ 10%: Ótimo (fluxo de caixa livre robusto)
    - FCF Yield > 10%: Fora da faixa (fluxo de caixa livre excepcional)
    '''
    definicao = '''
    O Free Cash Flow Yield mede o fluxo de caixa livre por ação em relação ao preço da ação, calculado
    como (Fluxo de Caixa Livre / Valor de Mercado). É um indicador que reflete a capacidade da empresa
    de gerar caixa após despesas operacionais e investimentos, em relação ao seu valor de mercado. Um
    yield alto sugere subvalorização, enquanto um valor baixo ou negativo indica ineficiência ou sobrevalorização.
    '''
    agrupador = 'Fluxo de Caixa'
    formula = 'FCF Yield = Fluxo de Caixa Livre / Valor de Mercado'

    try:
        if fcf_yield < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'FCF Yield < 0%',
                'descricao': '''
                Um FCF Yield negativo indica que a empresa não gera fluxo de caixa livre, sugerindo dificuldades
                financeiras ou altos investimentos. Isso é comum em empresas em crise, como a Gol (GOLL4). Para
                investidores, essa faixa é um alerta de risco elevado, exigindo análise de endividamento e estratégias
                de geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= fcf_yield <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= FCF Yield <= 3%',
                'descricao': '''
                Um FCF Yield entre 0% e 3% reflete fluxo de caixa livre baixo, indicando que a empresa gera pouco
                caixa em relação ao seu valor de mercado. Isso é comum em setores com margens apertadas, como varejo
                (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo análise
                de eficiência operacional e potencial de melhoria do fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < fcf_yield <= 6:
            return {
                'classificacao': 'Moderado',
                'faixa': '3% < FCF Yield <= 6%',
                'descricao': '''
                Um FCF Yield entre 3% e 6% indica fluxo de caixa livre aceitável, típico de empresas com eficiência
                moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere equilíbrio entre geração de caixa e valuation, sendo adequada para retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 6 < fcf_yield <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '6% < FCF Yield <= 10%',
                'descricao': '''
                Um FCF Yield entre 6% e 10% reflete fluxo de caixa livre robusto, indicando que a empresa gera
                caixa significativo em relação ao seu valor de mercado. Empresas como a Ambev (ABEV3) frequentemente
                apresentam yield nessa faixa. Para investidores, essa faixa é atrativa, sugerindo subvalorização e
                solidez financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif fcf_yield > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'FCF Yield > 10%',
                'descricao': '''
                Um FCF Yield acima de 10% é excepcional, indicando que a empresa gera fluxo de caixa livre extremamente
                alto em relação ao seu valor de mercado. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos
                de alta geração de caixa. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois
                yields tão altos podem não ser sustentáveis. A análise deve focar na consistência do fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o FCF Yield: {str(e)}. Isso pode ter acontecido se o valor fornecido não
            for numérico ou se o valor de mercado for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o fluxo de caixa livre e o valor de mercado estejam corretos e sejam valores numéricos
            válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_lucro(crescimento_lucro):
    '''
    Avalia o Crescimento do Lucro com base em faixas definidas para o mercado brasileiro:
    - Crescimento Lucro < 0%: Crítico (redução de lucro, risco elevado)
    - 0% ≤ Crescimento Lucro ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento Lucro ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento Lucro ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento Lucro > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento do Lucro mede a taxa anual de aumento do lucro líquido, calculada como
    ((Lucro Final / Lucro Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador de crescimento
    que reflete a capacidade da empresa de aumentar sua rentabilidade. Um crescimento alto sugere sucesso
    operacional, enquanto um valor baixo ou negativo indica dificuldades. É útil em setores de alto crescimento,
    como tecnologia, mas deve ser analisado com margens e fluxo de caixa.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Lucro = ((Lucro Final / Lucro Inicial)^(1/n) - 1)'

    try:
        if crescimento_lucro < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Lucro < 0%',
                'descricao': '''
                Um Crescimento do Lucro negativo indica que a empresa está enfrentando uma redução no lucro líquido,
                sugerindo dificuldades operacionais ou financeiras. Isso é comum em empresas em crise, como a Gol
                (GOLL4). Para investidores, essa faixa é um alerta de risco elevado, exigindo análise das causas da
                queda e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_lucro <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Lucro <= 5%',
                'descricao': '''
                Um Crescimento do Lucro entre 0% e 5% reflete crescimento baixo ou estagnação, indicando que a
                empresa tem dificuldade em aumentar sua rentabilidade. Isso é comum em setores maduros, como varejo
                (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo análise
                de estratégias de crescimento e eficiência operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_lucro <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento Lucro <= 15%',
                'descricao': '''
                Um Crescimento do Lucro entre 5% e 15% indica crescimento aceitável, típico de empresas com
                rentabilidade estável. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre crescimento e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_lucro <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento Lucro <= 25%',
                'descricao': '''
                Um Crescimento do Lucro entre 15% e 25% reflete crescimento robusto, indicando que a empresa está
                aumentando sua rentabilidade de forma significativa. Empresas como a Magazine Luiza (MGLU3) podem
                apresentar crescimento nessa faixa em períodos de expansão. Para investidores, essa faixa é atrativa,
                sugerindo potencial de valorização.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_lucro > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Lucro > 25%',
                'descricao': '''
                Um Crescimento do Lucro acima de 25% é excepcional, indicando aumento extremamente rápido da
                rentabilidade. Isso pode ocorrer em empresas em setores de alto crescimento, como o Nubank (NUBR33).
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos
                podem não ser sustentáveis. A análise deve focar na escalabilidade e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento do Lucro: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o lucro inicial for zero, o que impede o cálculo. Verifique os dados
            de entrada, assegurando que os lucros inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_debt_equity(debt_equity):
    '''
    Avalia a Dívida/Patrimônio Líquido com base em faixas definidas para o mercado brasileiro:
    - Dívida/Patrimônio < 0: Fora da faixa (sem dívida ou patrimônio negativo)
    - 0 ≤ Dívida/Patrimônio ≤ 0.5: Ótimo (endividamento muito baixo)
    - 0.5 < Dívida/Patrimônio ≤ 1: Moderado (endividamento aceitável)
    - 1 < Dívida/Patrimônio ≤ 2: Ruim (endividamento elevado)
    - 2 < Dívida/Patrimônio ≤ 3: Péssimo (endividamento muito alto)
    - Dívida/Patrimônio > 3: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida/Patrimônio Líquido mede a proporção da dívida total em relação ao patrimônio líquido,
    calculada como (Dívida Total / Patrimônio Líquido). É um indicador de alavancagem financeira que
    avalia o nível de endividamento em relação ao capital próprio. Um valor baixo sugere solidez financeira,
    enquanto um valor alto indica maior risco financeiro devido à dependência de dívidas.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida/Patrimônio = Dívida Total / Patrimônio Líquido'

    try:
        if debt_equity < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida/Patrimônio < 0',
                'descricao': '''
                Uma Dívida/Patrimônio negativa indica que a empresa não tem dívida ou que o patrimônio líquido
                é negativo. Empresas como a Totvs (TOTS3) podem apresentar valores negativos em períodos de alta
                liquidez, enquanto um patrimônio negativo (ex.: Oi - OIBR3) é alarmante. Para investidores, essa
                faixa exige análise detalhada da estrutura de capital e geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= debt_equity <= 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida/Patrimônio <= 0.5',
                'descricao': '''
                Uma Dívida/Patrimônio entre 0 e 0.5 reflete endividamento muito baixo, indicando solidez financeira.
                Empresas como a Vale (VALE3) em períodos de alta geração de caixa frequentemente operam nessa faixa.
                Para investidores, essa faixa é atrativa, sugerindo baixo risco financeiro e flexibilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < debt_equity <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Dívida/Patrimônio <= 1',
                'descricao': '''
                Uma Dívida/Patrimônio entre 0.5 e 1 indica endividamento aceitável, com equilíbrio entre dívida e
                capital próprio. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere risco moderado, com a empresa capaz de suportar oscilações econômicas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < debt_equity <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < Dívida/Patrimônio <= 2',
                'descricao': '''
                Uma Dívida/Patrimônio entre 1 e 2 sugere endividamento elevado, indicando que a empresa depende
                significativamente de dívidas. Isso é comum em setores intensivos em capital, como a Petrobras (PETR4).
                Para investidores, essa faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < debt_equity <= 3:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < Dívida/Patrimônio <= 3',
                'descricao': '''
                Uma Dívida/Patrimônio entre 2 e 3 reflete endividamento muito alto, indicando risco significativo.
                Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises. Para investidores, essa faixa é
                preocupante, exigindo análise detalhada da estrutura de capital e planos de desalavancagem.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif debt_equity > 3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida/Patrimônio > 3',
                'descricao': '''
                Uma Dívida/Patrimônio acima de 3 indica endividamento excessivo, sugerindo dependência extrema de
                dívidas. Isso é alarmante e típico de empresas em dificuldades, como a Gol (GOLL4) em crises. Para
                investidores, essa faixa é de altíssimo risco, com possibilidade de insolvência. A análise deve focar
                na capacidade de geração de caixa e estratégias de redução de dívida.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida/Patrimônio: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que a dívida total e o patrimônio líquido estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_margem_liquida_crescimento(margem_liquida_crescimento):
    '''
    Avalia o Crescimento da Margem Líquida com base em faixas definidas para o mercado brasileiro:
    - Crescimento Margem Líquida < 0%: Crítico (redução da margem, risco elevado)
    - 0% ≤ Crescimento Margem Líquida ≤ 2%: Ruim (crescimento baixo ou estagnação)
    - 2% < Crescimento Margem Líquida ≤ 5%: Moderado (crescimento aceitável)
    - 5% < Crescimento Margem Líquida ≤ 10%: Ótimo (crescimento robusto)
    - Crescimento Margem Líquida > 10%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento da Margem Líquida mede a taxa anual de aumento da margem líquida, calculada como
    ((Margem Líquida Final / Margem Líquida Inicial)^(1/n) - 1), onde n é o número de anos. É um
    indicador que reflete a melhoria na eficiência da empresa em converter receita em lucro líquido.
    Um crescimento alto sugere maior eficiência operacional, enquanto um valor baixo ou negativo indica
    deterioração da rentabilidade.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Crescimento Margem Líquida = ((Margem Líquida Final / Margem Líquida Inicial)^(1/n) - 1)'

    try:
        if margem_liquida_crescimento < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Margem Líquida < 0%',
                'descricao': '''
                Um Crescimento da Margem Líquida negativo indica redução da rentabilidade, sugerindo dificuldades
                operacionais ou aumento de custos. Isso é comum em empresas em crise, como a Oi (OIBR3). Para
                investidores, essa faixa é um alerta de risco elevado, exigindo análise da estrutura de custos e
                estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_liquida_crescimento <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Margem Líquida <= 2%',
                'descricao': '''
                Um Crescimento da Margem Líquida entre 0% e 2% reflete crescimento baixo ou estagnação, indicando
                que a empresa tem dificuldade em melhorar sua rentabilidade. Isso é comum em setores maduros, como
                varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo
                análise de estratégias de redução de custos e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < margem_liquida_crescimento <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Crescimento Margem Líquida <= 5%',
                'descricao': '''
                Um Crescimento da Margem Líquida entre 2% e 5% indica crescimento aceitável, típico de empresas com
                eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre rentabilidade e segurança, sendo adequada para
                retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < margem_liquida_crescimento <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Crescimento Margem Líquida <= 10%',
                'descricao': '''
                Um Crescimento da Margem Líquida entre 5% e 10% reflete crescimento robusto, indicando que a empresa
                está melhorando significativamente sua eficiência em converter receita em lucro. Empresas como a Ambev
                (ABEV3) podem apresentar crescimento nessa faixa. Para investidores, essa faixa é atrativa, sugerindo
                potencial de valorização sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_liquida_crescimento > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Margem Líquida > 10%',
                'descricao': '''
                Um Crescimento da Margem Líquida acima de 10% é excepcional, indicando melhoria extremamente rápida
                da rentabilidade. Isso pode ocorrer em empresas em setores de alto crescimento, como o Nubank (NUBR33).
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem
                não ser sustentáveis. A análise deve focar na escalabilidade e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento da Margem Líquida: {str(e)}. Isso pode ter acontecido se o
            valor fornecido não for numérico ou se a margem líquida inicial for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que as margens líquidas inicial e final estejam corretas e
            sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_4.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: ROE, P/L, Liquidez Corrente, Cobertura de Juros.
"""


def evaluate_roe(roe):
    '''
    Avalia o Retorno sobre o Patrimônio Líquido (ROE) com base em faixas definidas para o mercado brasileiro:
    - ROE < 0%: Crítico (prejuízo, destruição de valor)
    - 0% ≤ ROE ≤ 5%: Ruim (retorno baixo, ineficiência)
    - 5% < ROE ≤ 15%: Moderado (retorno aceitável)
    - 15% < ROE ≤ 25%: Ótimo (retorno robusto)
    - ROE > 25%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre o Patrimônio Líquido (ROE) mede a rentabilidade do capital próprio, calculado como
    (Lucro Líquido / Patrimônio Líquido). É um indicador de eficiência que mostra quanto a empresa gera
    de lucro com o capital dos acionistas. Um ROE alto sugere eficiência, enquanto um valor baixo ou
    negativo indica ineficiência ou prejuízo. É útil para comparar empresas dentro do mesmo setor.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROE = Lucro Líquido / Patrimônio Líquido'

    try:
        if roe < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROE < 0%',
                'descricao': '''
                Um ROE negativo indica que a empresa está gerando prejuízo, destruindo valor para os acionistas.
                Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores, essa faixa é um alerta de
                risco elevado, exigindo análise detalhada da estrutura de custos e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roe <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROE <= 5%',
                'descricao': '''
                Um ROE entre 0% e 5% reflete retorno baixo, indicando ineficiência na geração de lucro com o capital
                próprio. Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3).
                Para investidores, essa faixa sugere risco moderado, exigindo análise de estratégias de melhoria da
                rentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < roe <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < ROE <= 15%',
                'descricao': '''
                Um ROE entre 5% e 15% indica retorno aceitável, típico de empresas com eficiência moderada. No Brasil,
                empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere
                equilíbrio entre rentabilidade e segurança, sendo adequada para retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < roe <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < ROE <= 25%',
                'descricao': '''
                Um ROE entre 15% e 25% reflete retorno robusto, indicando que a empresa utiliza o capital próprio
                de forma eficiente. Empresas como a Ambev (ABEV3) frequentemente apresentam ROE nessa faixa. Para
                investidores, essa faixa é atrativa, sugerindo solidez financeira e potencial de valorização.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roe > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROE > 25%',
                'descricao': '''
                Um ROE acima de 25% é excepcional, indicando retornos extremamente altos com o capital próprio.
                Isso pode ocorrer em empresas como a Weg (WEGE3) em períodos de forte desempenho. Para investidores,
                essa faixa é altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROE: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o lucro líquido e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_p_l(p_l):
    '''
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (lucro negativo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 25: Péssimo (muito caro, alto risco)
    - P/L > 25: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/Lucro (P/L) compara o preço da ação ao lucro por ação, calculado como (Preço da Ação / Lucro por Ação).
    É um indicador de valuation que avalia se a ação está cara ou barata em relação aos lucros. Um P/L baixo
    sugere subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
    '''
    agrupador = 'Valuation'
    formula = 'P/L = Preço da Ação / Lucro por Ação'

    try:
        if p_l < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/L < 0',
                'descricao': '''
                Um P/L negativo indica que a empresa está operando com prejuízo ou teve eventos extraordinários (como baixas contábeis).
                 Não é diretamente comparável a P/L positivo, mas pode sinalizar oportunidades em empresas com recuperação potencial ou
                 distorções temporárias.Recomendações: Avaliar a causa do prejuízo (cíclica, estrutural ou contábil).
                 Empresas em setores voláteis (como commodities) podem ter P/L negativo temporário. Foco em fundamentos: fluxo de caixa, perspectivas de recuperação e balanço patrimonial. Ideal para investidores com alta tolerância a risco..
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Prejuízos persistentes podem indicar problemas estruturais, '
                          'má gestão ou exposição a riscos macroeconômicos. Alta volatilidade e incerteza no curto prazo.',
                'referencia_cruzada': 'Analise evaluate_cash_flow para verificar geração de caixa e evaluate_debt_to_equity para saúde financeira. '
                                      'Considere também evaluate_p_vp para valuation patrimonial em cenários de recuperação.'
            }
        elif 0 <= p_l <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/L <= 10',
                'descricao': '''
                Subvalorização significativa. Exemplo: Vale (VALE3) teve P/L ~8 em 2023, com lucros robustos.
                Implicações: Oportunidade para investidores de valor, com potencial de valorização. 
                Recomendações: Confirmar sustentabilidade de lucros e exposição a ciclos; ideal para longo prazo. 
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos' : 'Lucros elevados podem ser temporários; analisar histórico',
                'referencia_cruzada' : 'Analise evaluate_peg_ratio para crescimento e evaluate_p_vp para valuation patrimonial'

            }
        elif 10 < p_l <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '10 < P/L <= 15',
                'descricao': '''
                Valuation justo, comum em empresas estáveis. Exemplo: Ambev (ABEV3) pode ter P/L ~13,
                 com lucros consistentes. Implicações: Equilíbrio para moderados, 
                 com risco e retorno balanceados. Recomendações: Avaliar crescimento de lucros e
                  estabilidade setorial; ideal para portfólios diversificados. 
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Estagnação em setores maduros pode limitar valorização',
                'referencia_cruzada': 'Compare com evaluate_evebitda para valuation operacional e evaluate_roe para rentabilidade.'
            }
        elif 15 < p_l <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < P/L <= 20',
                'descricao': '''
                Sobrevalorização moderada, comum em empresas com crescimento esperado.
                Exemplo: Raia Drogasil (RADL3) pode ter P/L ~18 devido à expansão no varejo. 
                Implicações: Cautela para conservadores; atrativo para crescimento se 
                projeções forem sólidas. Recomendações: Validar crescimento com análise de mercado; moderados avaliar concorrência
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Expectativas não realizadas podem levar a correçõeso',
                'referencia_cruzada': 'Verifique evaluate_psr para relação com receita e evaluate_crescimento_lucro para tendências..'
            }
        elif 20 < p_l <= 25:
            return {
                'classificacao': 'Péssimo',
                'faixa': '20 < P/L <= 25',
                'descricao': '''
                Um P/L entre 20 e 25 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/L nessa faixa em momentos de
                otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Sensibilidade a mudanças macroeconômicas (ex.: juros altos). ',
                'referencia_cruzada': 'Combine com evaluate_p_ebitda para fluxo de caixa e evaluate_margem_liquida para eficiência.'
            }
        elif p_l > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/L > 25',
                'descricao': '''
                ): Especulação, com preço muito acima dos lucros. Exemplo: Nubank (NUBR33) pode ter P/L > 25 
                devido a expectativas de crescimento digital. Implicações: Alto risco, adequado para especulativos.
                 Recomendações: Analisar projeções de mercado; conservadores evitar
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'SBolhas especulativas ou falha em entregar crescimento',
                'referencia_cruzada': 'Avalie evaluate_peg_ratio para crescimento e evaluate_p_ativo para relação com ativos.'
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/L: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se o lucro por ação for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o preço da ação e o lucro por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_liquidez_corrente(liquidez_corrente):
    '''
    Avalia a Liquidez Corrente com base em faixas definidas para o mercado brasileiro:
    - Liquidez Corrente < 0.5: Crítico (dificuldade extrema em pagar obrigações de curto prazo)
    - 0.5 ≤ Liquidez Corrente ≤ 1: Ruim (capacidade limitada de pagar obrigações de curto prazo)
    - 1 < Liquidez Corrente ≤ 1.5: Moderado (capacidade aceitável de pagar obrigações de curto prazo)
    - 1.5 < Liquidez Corrente ≤ 2: Ótimo (boa capacidade de pagar obrigações de curto prazo)
    - Liquidez Corrente > 2: Fora da faixa (excesso de liquidez, possível ineficiência)
    '''
    definicao = '''
    A Liquidez Corrente mede a capacidade da empresa de pagar suas obrigações de curto prazo com seus
    ativos circulantes, calculada como (Ativo Circulante / Passivo Circulante). É um indicador de liquidez
    que reflete a saúde financeira de curto prazo. Um valor alto sugere solidez, enquanto um valor baixo
    indica risco de inadimplência.
    '''
    agrupador = 'Liquidez'
    formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'

    try:
        if liquidez_corrente < 0.5:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Liquidez Corrente < 0.5',
                'descricao': '''
                Uma Liquidez Corrente abaixo de 0.5 indica dificuldade extrema em pagar obrigações de curto prazo,
                sugerindo risco elevado de inadimplência. Isso é comum em empresas em crise, como a Oi (OIBR3).
                Para investidores, essa faixa é um alerta grave, exigindo análise da gestão de caixa e recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 <= liquidez_corrente <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 <= Liquidez Corrente <= 1',
                'descricao': '''
                Uma Liquidez Corrente entre 0.5 e 1 reflete capacidade limitada de pagar obrigações de curto prazo,
                indicando dependência de conversão de ativos em caixa. Isso é comum em setores com margens apertadas,
                como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < liquidez_corrente <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Liquidez Corrente <= 1.5',
                'descricao': '''
                Uma Liquidez Corrente entre 1 e 1.5 indica capacidade aceitável de pagar obrigações de curto prazo.
                Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere
                equilíbrio entre liquidez e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < liquidez_corrente <= 2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1.5 < Liquidez Corrente <= 2',
                'descricao': '''
                Uma Liquidez Corrente entre 1.5 e 2 reflete boa capacidade de pagar obrigações de curto prazo,
                indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam liquidez nessa
                faixa. Para investidores, essa faixa é atrativa, sugerindo resiliência financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif liquidez_corrente > 2:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez Corrente > 2',
                'descricao': '''
                Uma Liquidez Corrente acima de 2 indica excesso de liquidez, com ativos circulantes muito superiores
                às obrigações de curto prazo. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos de alta
                geração de caixa. Para investidores, essa faixa pode ser positiva, mas também pode indicar ineficiência
                na alocação de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Liquidez Corrente: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o ativo circulante e o passivo circulante estejam corretos e sejam
            valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_cobertura_juros(cobertura_juros):
    '''
    Avalia a Cobertura de Juros com base em faixas definidas para o mercado brasileiro:
    - Cobertura de Juros < 1: Crítico (dificuldade em cobrir juros, risco elevado)
    - 1 ≤ Cobertura de Juros ≤ 2: Ruim (capacidade limitada de cobrir juros)
    - 2 < Cobertura de Juros ≤ 4: Moderado (capacidade aceitável de cobrir juros)
    - 4 < Cobertura de Juros ≤ 6: Ótimo (boa capacidade de cobrir juros)
    - Cobertura de Juros > 6: Fora da faixa (excelente capacidade de cobrir juros)
    '''
    definicao = '''
    A Cobertura de Juros mede a capacidade da empresa de pagar os juros de suas dívidas com o lucro
    operacional, calculada como (EBIT / Despesa com Juros). É um indicador de solvência que reflete a
    segurança financeira em relação às obrigações de dívida. Um valor alto sugere solidez, enquanto um
    valor baixo indica risco de inadimplência.
    '''
    agrupador = 'Solvência'
    formula = 'Cobertura de Juros = EBIT / Despesa com Juros'

    try:
        if cobertura_juros < 1:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Cobertura de Juros < 1',
                'descricao': '''
                Uma Cobertura de Juros abaixo de 1 indica que a empresa não gera lucro operacional suficiente
                para cobrir os juros de suas dívidas, sugerindo risco elevado de inadimplência. Isso é comum em
                empresas em crise, como a Gol (GOLL4). Para investidores, essa faixa é um alerta grave, exigindo
                análise da estrutura de dívida e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 <= cobertura_juros <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 <= Cobertura de Juros <= 2',
                'descricao': '''
                Uma Cobertura de Juros entre 1 e 2 reflete capacidade limitada de cobrir os juros, indicando
                dependência de lucros operacionais apertados. Isso é comum em setores intensivos em capital, como a
                Petrobras (PETR4). Para investidores, essa faixa sugere risco moderado, exigindo análise da gestão
                de dívida.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < cobertura_juros <= 4:
            return {
                'classificacao': 'Moderado',
                'faixa': '2 < Cobertura de Juros <= 4',
                'descricao': '''
                Uma Cobertura de Juros entre 2 e 4 indica capacidade aceitável de cobrir os juros, típico de empresas
                com estabilidade financeira moderada. Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre solvência e risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < cobertura_juros <= 6:
            return {
                'classificacao': 'Ótimo',
                'faixa': '4 < Cobertura de Juros <= 6',
                'descricao': '''
                Uma Cobertura de Juros entre 4 e 6 reflete boa capacidade de cobrir os juros, indicando solidez
                financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam cobertura nessa faixa. Para
                investidores, essa faixa é atrativa, sugerindo resiliência financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif cobertura_juros > 6:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Cobertura de Juros > 6',
                'descricao': '''
                Uma Cobertura de Juros acima de 6 indica excelente capacidade de cobrir os juros, sugerindo baixa
                dependência de dívidas. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos de alta geração
                de caixa. Para investidores, essa faixa é altamente atrativa, mas pode indicar subalavancagem.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Cobertura de Juros: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se a despesa com juros for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o EBIT e a despesa com juros estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_5.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Margem Bruta, Giro de Ativos, Dívida/EBIT, Dividend Yield.
"""


def evaluate_margem_bruta(margem_bruta):
    '''
    Avalia a Margem Bruta com base em faixas definidas para o mercado brasileiro:
    - Margem Bruta < 10%: Crítico (rentabilidade bruta muito baixa, risco elevado)
    - 10% ≤ Margem Bruta ≤ 20%: Ruim (rentabilidade bruta baixa)
    - 20% < Margem Bruta ≤ 30%: Moderado (rentabilidade bruta aceitável)
    - 30% < Margem Bruta ≤ 50%: Ótimo (rentabilidade bruta robusta)
    - Margem Bruta > 50%: Fora da faixa (rentabilidade bruta excepcional)
    '''
    definicao = '''
    A Margem Bruta mede a proporção da receita bruta que permanece após os custos diretos, calculada
    como (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta. É um indicador de rentabilidade
    que reflete a eficiência da empresa em gerenciar custos diretos. Uma margem alta sugere forte
    precificação ou controle de custos, enquanto uma margem baixa indica dificuldades operacionais.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem Bruta = (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta'

    try:
        if margem_bruta < 10:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem Bruta < 10%',
                'descricao': '''
                Uma Margem Bruta abaixo de 10% indica rentabilidade bruta muito baixa, sugerindo dificuldades em
                cobrir custos diretos. Isso é comum em setores altamente competitivos, como varejo (ex.: Casas Bahia
                - BHIA3). Para investidores, essa faixa é um alerta de risco elevado, exigindo análise da estrutura
                de custos e concorrência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 <= margem_bruta <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '10% <= Margem Bruta <= 20%',
                'descricao': '''
                Uma Margem Bruta entre 10% e 20% reflete rentabilidade bruta baixa, indicando desafios na gestão
                de custos diretos. Isso é comum em setores com margens apertadas, como varejo alimentar (ex.: Carrefour
                Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo análise de estratégias
                de precificação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < margem_bruta <= 30:
            return {
                'classificacao': 'Moderado',
                'faixa': '20% < Margem Bruta <= 30%',
                'descricao': '''
                Uma Margem Bruta entre 20% e 30% indica rentabilidade bruta aceitável, típico de empresas com
                eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre rentabilidade e competitividade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 30 < margem_bruta <= 50:
            return {
                'classificacao': 'Ótimo',
                'faixa': '30% < Margem Bruta <= 50%',
                'descricao': '''
                Uma Margem Bruta entre 30% e 50% reflete rentabilidade bruta robusta, indicando forte controle de
                custos ou precificação. Empresas como a Ambev (ABEV3) frequentemente apresentam margem nessa faixa.
                Para investidores, essa faixa é atrativa, sugerindo solidez operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_bruta > 50:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem Bruta > 50%',
                'descricao': '''
                Uma Margem Bruta acima de 50% é excepcional, indicando altíssima eficiência na gestão de custos
                diretos. Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa é altamente
                atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem Bruta: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a receita bruta e o custo dos produtos vendidos estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_giro_ativos(giro_ativos):
    '''
    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
    - Giro de Ativos < 0.2: Crítico (baixa eficiência no uso de ativos)
    - 0.2 ≤ Giro de Ativos ≤ 0.5: Ruim (eficiência limitada no uso de ativos)
    - 0.5 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável no uso de ativos)
    - 1 < Giro de Ativos ≤ 1.5: Ótimo (alta eficiência no uso de ativos)
    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional no uso de ativos)
    '''
    definicao = '''
    O Giro de Ativos mede a eficiência da empresa em gerar receita com seus ativos totais, calculado
    como (Receita Bruta / Ativos Totais). É um indicador que reflete como a empresa utiliza seus ativos
    para gerar vendas. Um valor alto sugere eficiência, enquanto um valor baixo indica subutilização de
    ativos.
    '''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

    try:
        if giro_ativos < 0.2:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Giro de Ativos < 0.2',
                'descricao': '''
                Um Giro de Ativos abaixo de 0.2 indica baixa eficiência no uso de ativos, sugerindo subutilização
                ou ativos ociosos. Isso é comum em empresas com grandes investimentos fixos, como a CSN (CSNA3) em
                períodos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 <= giro_ativos <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 <= Giro de Ativos <= 0.5',
                'descricao': '''
                Um Giro de Ativos entre 0.2 e 0.5 reflete eficiência limitada no uso de ativos, indicando que a
                empresa gera receita moderada em relação aos ativos. Isso é comum em setores intensivos em capital,
                como a Petrobras (PETR4). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < giro_ativos <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Giro de Ativos <= 1',
                'descricao': '''
                Um Giro de Ativos entre 0.5 e 1 indica eficiência aceitável no uso de ativos. Empresas como a
                Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio
                entre eficiência e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < giro_ativos <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Giro de Ativos <= 1.5',
                'descricao': '''
                Um Giro de Ativos entre 1 e 1.5 reflete alta eficiência no uso de ativos, indicando que a empresa
                gera receita significativa com seus ativos. Empresas como a Ambev (ABEV3) frequentemente apresentam
                giro nessa faixa. Para investidores, essa faixa é atrativa, sugerindo eficiência operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif giro_ativos > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro de Ativos > 1.5',
                'descricao': '''
                Um Giro de Ativos acima de 1.5 é excepcional, indicando eficiência extremamente alta no uso de
                ativos. Isso pode ocorrer em empresas como a Magazine Luiza (MGLU3) em períodos de forte crescimento.
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois pode não ser sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que a receita bruta e os ativos totais estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_ebit(divida_ebit):
    '''
    Avalia a Dívida/EBIT com base em faixas definidas para o mercado brasileiro:
    - Dívida/EBIT < 0: Fora da faixa (sem dívida ou EBIT negativo)
    - 0 ≤ Dívida/EBIT ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida/EBIT ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida/EBIT ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida/EBIT ≤ 4: Péssimo (endividamento muito alto)
    - Dívida/EBIT > 4: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida/EBIT mede a capacidade da empresa de pagar sua dívida total com o lucro antes de juros e
    impostos, calculada como (Dívida Total / EBIT). É um indicador de alavancagem financeira que avalia
    quantos anos a empresa levaria para quitar sua dívida com seu lucro operacional. Um valor baixo
    sugere solidez financeira, enquanto um valor alto indica risco elevado.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida/EBIT = Dívida Total / EBIT'

    try:
        if divida_ebit < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida/EBIT < 0',
                'descricao': '''
                Uma Dívida/EBIT negativa indica que a empresa não tem dívida ou que o EBIT é negativo. Empresas
                como a Totvs (TOTS3) podem apresentar valores negativos em períodos de alta liquidez, enquanto um
                EBIT negativo (ex.: Oi - OIBR3) é alarmante. Para investidores, essa faixa exige análise detalhada
                da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_ebit <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida/EBIT <= 1',
                'descricao': '''
                Uma Dívida/EBIT entre 0 e 1 reflete endividamento muito baixo, indicando que a empresa pode quitar
                sua dívida rapidamente com o lucro operacional. Empresas como a Vale (VALE3) podem operar nessa faixa
                em períodos de alta geração de caixa. Para investidores, essa faixa é atrativa, sugerindo baixo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_ebit <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida/EBIT <= 2',
                'descricao': '''
                Uma Dívida/EBIT entre 1 e 2 indica endividamento aceitável, com equilíbrio entre dívida e lucro
                operacional. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_ebit <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida/EBIT <= 3',
                'descricao': '''
                Uma Dívida/EBIT entre 2 e 3 sugere endividamento elevado, indicando dependência significativa de
                dívidas. Isso é comum em setores intensivos em capital, como a Petrobras (PETR4). Para investidores,
                essa faixa exige cautela, pois a empresa pode ser vulnerável a oscilações econômicas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_ebit <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida/EBIT <= 4',
                'descricao': '''
                Uma Dívida/EBIT entre 3 e 4 reflete endividamento muito alto, indicando risco significativo.
                Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises. Para investidores, essa faixa
                é preocupante, exigindo análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_ebit > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida/EBIT > 4',
                'descricao': '''
                Uma Dívida/EBIT acima de 4 indica endividamento excessivo, sugerindo dependência extrema de dívidas.
                Isso é típico de empresas em dificuldades, como a Gol (GOLL4) em crises. Para investidores, essa
                faixa é de altíssimo risco, com possibilidade de insolvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida/EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a dívida total e o EBIT estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_dividend_yield(dividend_yield):
    '''
    Avalia o Dividend Yield com base em faixas definidas para o mercado brasileiro:
    - Dividend Yield < 0%: Fora da faixa (sem dividendos)
    - 0% ≤ Dividend Yield ≤ 2%: Ruim (retorno baixo em dividendos)
    - 2% < Dividend Yield ≤ 5%: Moderado (retorno aceitável em dividendos)
    - 5% < Dividend Yield ≤ 8%: Ótimo (retorno robusto em dividendos)
    - Dividend Yield > 8%: Crítico (retorno muito alto, risco de insustentabilidade)
    '''
    definicao = '''
    O Dividend Yield mede o retorno anual em dividendos em relação ao preço da ação, calculado como
    (Dividendos por Ação / Preço da Ação). É um indicador que reflete o retorno direto para os acionistas
    por meio de dividendos. Um yield alto é atrativo para investidores focados em renda, mas pode indicar
    risco se for insustentável.
    '''
    agrupador = 'Dividendos'
    formula = 'Dividend Yield = Dividendos por Ação / Preço da Ação'

    try:
        if dividend_yield < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dividend Yield < 0%',
                'descricao': '''
                Um Dividend Yield negativo ou zero indica que a empresa não paga dividendos, seja por prejuízo ou
                reinvestimento total dos lucros. Isso é comum em empresas em crescimento, como o Nubank (NUBR33).
                Para investidores focados em renda, essa faixa é desvantajosa, mas pode ser positiva para quem busca
                crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dividend_yield <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Dividend Yield <= 2%',
                'descricao': '''
                Um Dividend Yield entre 0% e 2% reflete retorno baixo em dividendos, indicando que a empresa
                prioriza reinvestimento. Isso é comum em empresas como a Magazine Luiza (MGLU3). Para investidores
                focados em renda, essa faixa é pouco atrativa, mas pode ser positiva para quem busca crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < dividend_yield <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Dividend Yield <= 5%',
                'descricao': '''
                Um Dividend Yield entre 2% e 5% indica retorno aceitável em dividendos, com equilíbrio entre
                distribuição e reinvestimento. Empresas como a Vale (VALE3) frequentemente operam nessa faixa.
                Para investidores, essa faixa é adequada para quem busca renda moderada com potencial de crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < dividend_yield <= 8:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Dividend Yield <= 8%',
                'descricao': '''
                Um Dividend Yield entre 5% e 8% reflete retorno robusto em dividendos, indicando que a empresa
                distribui uma parte significativa dos lucros. Empresas como a Engie Brasil (EGIE3) frequentemente
                apresentam yield nessa faixa. Para investidores, essa faixa é atrativa, sugerindo estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif dividend_yield > 8:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dividend Yield > 8%',
                'descricao': '''
                Um Dividend Yield acima de 8% indica retorno muito alto, mas pode sugerir insustentabilidade dos
                dividendos. Empresas como a Taesa (TAEE11) podem apresentar yields elevados, mas isso exige cautela,
                pois pode comprometer o crescimento. Para investidores, a análise deve focar no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Dividend Yield: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o preço da ação for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que os dividendos por ação e o preço da ação estejam corretos e sejam valores numéricos
            válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_6.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: P/VP, ROIC, Dívida Líquida/Patrimônio, Crescimento do EBITDA.
"""


def evaluate_p_vp(p_vp):
    '''
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Fora da faixa (patrimônio líquido negativo)
    - 0 ≤ P/VP ≤ 1: Ótimo (subvalorizado, oportunidade de compra)
    - 1 < P/VP ≤ 1.5: Moderado (valuation justo)
    - 1.5 < P/VP ≤ 2: Ruim (sobrevalorizado, cautela necessária)
    - 2 < P/VP ≤ 3: Péssimo (muito caro, alto risco)
    - P/VP > 3: Crítico (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
    como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
    ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
    subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
    '''
    agrupador = 'Valuation'
    formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    try:
        if p_vp < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/VP < 0',
                'descricao': '''
                Um P/VP negativo indica que o patrimônio líquido da empresa é negativo, sugerindo sérias
                dificuldades financeiras. Isso é comum em empresas em crise, como a Oi (OIBR3). Para
                investidores, essa faixa é um alerta grave, exigindo análise detalhada da saúde financeira.Implicações:
                Um P/VP negativo reflete uma situação em que os passivos superam os ativos, sinalizando risco elevado de
                 insolvência ou falência. Pode representar uma oportunidade especulativa em casos de 
                 recuperação judicial bem-sucedida, mas é altamente arriscado.Recomendações: Analisar detalhadamente
                 a estrutura de dívida, planos de reestruturação e perspectivas de geração de caixa. 
                 Indicado apenas para investidores especulativos com alta tolerância a risco. 
                 Investidores conservadores devem evitar completamente.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Alta probabilidade de falência ou diluição acionária em reestruturações.'
                          ' Prejuízos persistentes ou má gestão podem agravar a situação. Setores em declínio ou alta competição aumentam a incerteza.',
                'referencia_cruzada': 'Avalie evaluate_debt_to_equity para saúde financeira, '
                                      'evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento em cenários de recuperação.. '

            }
        elif 0 <= p_vp <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/VP <= 1',
                'descricao': '''
                Subvalorização significativa. Exemplo: Vale (VALE3) teve P/VP ~0.8 em 2023, 
                com patrimônio robusto. Implicações: Oportunidade para investidores de valor.
                 Recomendações: Confirmar qualidade do patrimônio; ideal para longo prazo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Patrimônio pode incluir ativos obsoletos',
                'referencia_cruzada': 'AAnalise evaluate_vpa para valor patrimonial e evaluate_roe para rentabilidade.'

            }
        elif 1 < p_vp <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < P/VP <= 1.5',
                'descricao': '''
                Valuation justo, comum em empresas estáveis. Exemplo: Ambev (ABEV3) pode ter P/VP ~1.3, 
                com patrimônio consistente. Implicações: Equilíbrio para moderados.
                 Recomendações: Avaliar estabilidade de lucros e alocação de capital; ideal para portfólios diversificados.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Estagnação em setores maduros',
                'referencia_cruzada': 'Compare com evaluate_p_l para lucros e evaluate_pl_ativos para estrutura'
            }
        elif 1.5 < p_vp <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < P/VP <= 2',
                'descricao': '''
                Sobrevalorização moderada. Exemplo: Raia Drogasil (RADL3) pode ter P/VP ~1.8
                 devido a crescimento. Implicações: Cautela para conservadores; atrativo para crescimento.
                  Recomendações: Validar expansão e retorno sobre patrimônio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': ': Expectativas não realizadas podem levar a correções',
                'referencia_cruzada': 'Verifique evaluate_peg_ratio para crescimento e evaluate_evebitda para valuation'
            }
        elif 2 < p_vp <= 3:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < P/VP <= 3',
                'descricao': '''
               Valuation elevado, com prêmio significativo. Exemplo: Localiza (RENT3) pode ter P/VP ~2.5 em
                períodos de alta demanda. Implicações: Risco de correção; menos atrativo para conservadores. 
                Recomendações: Agressivos confirmar fundamentos; conservadores evitar.  .
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Sensibilidade a mudanças econômicas (ex.: aumento de juros). ',
                'referencia_cruzada': ' Combine com evaluate_psr para receita e evaluate_margem_liquida para eficiência.'
            }
        elif p_vp > 3:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/VP > 3',
                'descricao': '''
                Especulação, com preço muito acima do patrimônio. Exemplo: Nubank (NUBR33) pode ter P/VP > 3 
                devido a expectativas digitais. Implicações: Alto risco, adequado para especulativos.
                 Recomendações: Analisar projeções de mercado; conservadores evitar
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': ' Bolhas especulativas. ',
                'referencia_cruzada': 'Avalie evaluate_p_ativo para ativos e evaluate_crescimento_receita para tendências'
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/VP: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o valor patrimonial por ação for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o preço da ação e o valor patrimonial por ação
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_roic(roic):
    '''
    Avalia o Retorno sobre o Capital Investido (ROIC) com base em faixas definidas para o mercado brasileiro:
    - ROIC < 0%: Crítico (destruição de valor, risco elevado)
    - 0% ≤ ROIC ≤ 5%: Ruim (retorno baixo, ineficiência)
    - 5% < ROIC ≤ 10%: Moderado (retorno aceitável)
    - 10% < ROIC ≤ 20%: Ótimo (retorno robusto)
    - ROIC > 20%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre o Capital Investido (ROIC) mede a eficiência da empresa em gerar lucro com o capital
    total investido (dívida e patrimônio), calculado como (NOPAT / Capital Investido), onde NOPAT é
    o lucro operacional após impostos. É um indicador de rentabilidade que avalia a eficiência do uso
    do capital. Um ROIC alto sugere eficiência, enquanto um valor baixo ou negativo indica ineficiência.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROIC = NOPAT / Capital Investido'

    try:
        if roic < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROIC < 0%',
                'descricao': '''
                Um ROIC negativo indica que a empresa está destruindo valor, gerando prejuízo com o capital
                investido. Isso é comum em empresas em crise, como a Gol (GOLL4). Para investidores, essa
                faixa é um alerta grave, exigindo análise detalhada da gestão de capital e recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roic <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROIC <= 5%',
                'descricao': '''
                Um ROIC entre 0% e 5% reflete retorno baixo, indicando ineficiência no uso do capital investido.
                Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3).
                Para investidores, essa faixa sugere risco moderado, exigindo análise de estratégias de melhoria.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < roic <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < ROIC <= 10%',
                'descricao': '''
                Um ROIC entre 5% e 10% indica retorno aceitável, típico de empresas com eficiência moderada.
                No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere equilíbrio entre rentabilidade e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < roic <= 20:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < ROIC <= 20%',
                'descricao': '''
                Um ROIC entre 10% e 20% reflete retorno robusto, indicando que a empresa utiliza o capital
                investido de forma eficiente. Empresas como a Ambev (ABEV3) frequentemente apresentam ROIC
                nessa faixa. Para investidores, essa faixa é atrativa, sugerindo solidez financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roic > 20:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROIC > 20%',
                'descricao': '''
                Um ROIC acima de 20% é excepcional, indicando retornos extremamente altos com o capital
                investido. Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa
                é altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROIC: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o capital investido for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o NOPAT e o capital investido estejam corretos e sejam
            valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_liquida_patrimonio(divida_liquida_patrimonio):
    '''
    Avalia a Dívida Líquida/Patrimônio com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/Patrimônio < 0: Fora da faixa (sem dívida líquida ou patrimônio negativo)
    - 0 ≤ Dívida Líquida/Patrimônio ≤ 0.3: Ótimo (endividamento muito baixo)
    - 0.3 < Dívida Líquida/Patrimônio ≤ 0.6: Moderado (endividamento aceitável)
    - 0.6 < Dívida Líquida/Patrimônio ≤ 1: Ruim (endividamento elevado)
    - 1 < Dívida Líquida/Patrimônio ≤ 1.5: Péssimo (endividamento muito alto)
    - Dívida Líquida/Patrimônio > 1.5: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida Líquida/Patrimônio mede a proporção da dívida líquida (dívida total menos caixa e equivalentes)
    em relação ao patrimônio líquido, calculada como (Dívida Líquida / Patrimônio Líquido). É um indicador
    de alavancagem financeira que avalia o nível de endividamento líquido. Um valor baixo sugere solidez,
    enquanto um valor alto indica maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/Patrimônio = Dívida Líquida / Patrimônio Líquido'

    try:
        if divida_liquida_patrimonio < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida/Patrimônio < 0',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio negativa indica que a empresa tem mais caixa do que dívida ou
                que o patrimônio líquido é negativo. Empresas como a Totvs (TOTS3) podem apresentar valores
                negativos em períodos de alta liquidez, enquanto um patrimônio negativo (ex.: Oi - OIBR3) é
                alarmante. Para investidores, essa faixa exige análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_liquida_patrimonio <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Líquida/Patrimônio <= 0.3',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0 e 0.3 reflete endividamento muito baixo, indicando
                solidez financeira. Empresas como a Vale (VALE3) em períodos de alta geração de caixa
                frequentemente operam nessa faixa. Para investidores, essa faixa é atrativa, sugerindo
                baixo risco financeiro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < divida_liquida_patrimonio <= 0.6:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < Dívida Líquida/Patrimônio <= 0.6',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0.3 e 0.6 indica endividamento aceitável, com equilíbrio
                entre dívida líquida e capital próprio. Empresas como a Ambev (ABEV3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < divida_liquida_patrimonio <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.6 < Dívida Líquida/Patrimônio <= 1',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0.6 e 1 sugere endividamento elevado, indicando
                dependência significativa de dívidas líquidas. Isso é comum em setores intensivos em capital,
                como a Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_liquida_patrimonio <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < Dívida Líquida/Patrimônio <= 1.5',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 1 e 1.5 reflete endividamento muito alto, indicando
                risco significativo. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises.
                Para investidores, essa faixa é preocupante, exigindo análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_liquida_patrimonio > 1.5:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Líquida/Patrimônio > 1.5',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio acima de 1.5 indica endividamento excessivo, sugerindo
                dependência extrema de dívidas líquidas. Isso é típico de empresas em dificuldades, como
                a Gol (GOLL4) em crises. Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida Líquida/Patrimônio: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o patrimônio líquido for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que a dívida líquida
            e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_ebitda(crescimento_ebitda):
    '''
    Avalia o Crescimento do EBITDA com base em faixas definidas para o mercado brasileiro:
    - Crescimento EBITDA < 0%: Crítico (redução de lucratividade operacional, risco elevado)
    - 0% ≤ Crescimento EBITDA ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento EBITDA ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento EBITDA ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento EBITDA > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento do EBITDA mede a taxa anual de aumento do lucro antes de juros, impostos,
    depreciação e amortização, calculada como ((EBITDA Final / EBITDA Inicial)^(1/n) - 1),
    onde n é o número de anos. É um indicador de crescimento operacional que reflete a capacidade
    da empresa de aumentar sua lucratividade antes de encargos financeiros. Um crescimento alto
    sugere sucesso operacional, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento EBITDA = ((EBITDA Final / EBITDA Inicial)^(1/n) - 1)'

    try:
        if crescimento_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento EBITDA < 0%',
                'descricao': '''
                Um Crescimento do EBITDA negativo indica redução da lucratividade operacional, sugerindo
                dificuldades em gerar receita ou controlar custos. Isso é comum em empresas em crise,
                como a Oi (OIBR3). Para investidores, essa faixa é um alerta de risco elevado, exigindo
                análise das causas da queda.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_ebitda <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento EBITDA <= 5%',
                'descricao': '''
                Um Crescimento do EBITDA entre 0% e 5% reflete crescimento baixo ou estagnação, indicando
                que a empresa tem dificuldade em expandir sua lucratividade operacional. Isso é comum
                em setores maduros, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_ebitda <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento EBITDA <= 15%',
                'descricao': '''
                Um Crescimento do EBITDA entre 5% e 15% indica crescimento aceitável, típico de empresas
                com estabilidade operacional. No Brasil, empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio entre crescimento e
                segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_ebitda <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento EBITDA <= 25%',
                'descricao': '''
                Um Crescimento do EBITDA entre 15% e 25% reflete crescimento robusto, indicando que a
                empresa está expandindo sua lucratividade operacional de forma significativa. Empresas
                como a Magazine Luiza (MGLU3) podem apresentar crescimento nessa faixa em períodos de
                expansão. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_ebitda > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento EBITDA > 25%',
                'descricao': '''
                Um Crescimento do EBITDA acima de 25% é excepcional, indicando aumento extremamente rápido
                da lucratividade operacional. Isso pode ocorrer em empresas como o Nubank (NUBR33) em
                períodos de forte crescimento. Para investidores, essa faixa é altamente atrativa, mas
                exige cautela, pois crescimentos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento do EBITDA: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o EBITDA inicial for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que os EBITDAs
            inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_7.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Margem EBITDA, P/EBITDA, Liquidez Imediata, Crescimento da Receita.
"""


def evaluate_margem_ebitda(margem_ebitda):
    '''
    Avalia a Margem EBITDA com base em faixas definidas para o mercado brasileiro:
    - Margem EBITDA < 0%: Crítico (lucratividade operacional negativa, risco elevado)
    - 0% ≤ Margem EBITDA ≤ 10%: Ruim (lucratividade operacional baixa)
    - 10% < Margem EBITDA ≤ 20%: Moderado (lucratividade operacional aceitável)
    - 20% < Margem EBITDA ≤ 30%: Ótimo (lucratividade operacional robusta)
    - Margem EBITDA > 30%: Fora da faixa (lucratividade operacional excepcional)
    '''
    definicao = '''
    A Margem EBITDA mede a proporção do lucro antes de juros, impostos, depreciação e amortização
    em relação à receita bruta, calculada como (EBITDA / Receita Bruta). É um indicador de
    rentabilidade operacional que reflete a eficiência da empresa em gerar lucro antes de encargos
    financeiros. Uma margem alta sugere forte desempenho operacional, enquanto uma margem baixa
    indica dificuldades.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem EBITDA = EBITDA / Receita Bruta'

    try:
        if margem_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem EBITDA < 0%',
                'descricao': '''
                Uma Margem EBITDA negativa indica lucratividade operacional negativa, sugerindo que a empresa
                não consegue cobrir custos operacionais com sua receita. Isso é comum em empresas em crise,
                como a Oi (OIBR3). Para investidores, essa faixa é um alerta grave, exigindo análise detalhada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_ebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Margem EBITDA <= 10%',
                'descricao': '''
                Uma Margem EBITDA entre 0% e 10% reflete lucratividade operacional baixa, indicando desafios
                na gestão de custos operacionais. Isso é comum em setores com margens apertadas, como varejo
                (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < margem_ebitda <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '10% < Margem EBITDA <= 20%',
                'descricao': '''
                Uma Margem EBITDA entre 10% e 20% indica lucratividade operacional aceitável, típico de
                empresas com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio entre rentabilidade e
                competitividade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < margem_ebitda <= 30:
            return {
                'classificacao': 'Ótimo',
                'faixa': '20% < Margem EBITDA <= 30%',
                'descricao': '''
                Uma Margem EBITDA entre 20% e 30% reflete lucratividade operacional robusta, indicando forte
                controle de custos e eficiência. Empresas como a Ambev (ABEV3) frequentemente apresentam
                margem nessa faixa. Para investidores, essa faixa é atrativa, sugerindo solidez operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_ebitda > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem EBITDA > 30%',
                'descricao': '''
                Uma Margem EBITDA acima de 30% é excepcional, indicando altíssima eficiência operacional.
                Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa é altamente
                atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o EBITDA e a receita bruta estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_p_ebitda(p_ebitda):
    '''
    Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
    - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ P/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < P/EBITDA ≤ 8: Moderado (valuation justo)
    - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
    - 12 < P/EBITDA ≤ 16: Péssimo (muito caro, alto risco)
    - P/EBITDA > 16: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/EBITDA compara o valor da empresa (valor de mercado + dívida líquida) ao EBITDA,
    calculado como (Enterprise Value / EBITDA). É um indicador de valuation que avalia se a
    empresa está cara ou barata em relação à sua lucratividade operacional. Um P/EBITDA baixo
    sugere subvalorização, enquanto um valor alto indica sobrevalorização.
    '''
    agrupador = 'Valuation'
    formula = 'P/EBITDA = Enterprise Value / EBITDA'

    try:
        if p_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/EBITDA < 0',
                'descricao': '''
                Implicações: Um P/EBITDA negativo indica que a empresa está gerando prejuízo operacional ou 
                enfrentando eventos atípicos (como reestruturações ou impairments). Pode sinalizar dificuldades financeiras ou
                 oportunidades em empresas com potencial de recuperação, mas exige cautela extrema.
                 Recomendações: Investigar a causa do prejuízo (estrutural, cíclica ou temporária).
                 Avaliar fundamentos como fluxo de caixa livre, endividamento e perspectivas de mercado. Indicado apenas para investidores com alta tolerância a risco, focando em cenários de turnaround. Conservadores devem evitar.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Prejuízos persistentes podem indicar insustentabilidade operacional ou falhas estratégicas. Alta volatilidade e risco de diluição em aumentos de capital',
                'referencia_cruzada': 'nalise evaluate_cash_flow para geração de caixa, evaluate_debt_to_equity '
                                      'para saúde financeira e evaluate_p_vp para valuation patrimonial em cenários de recuperação.'

            }
        elif 0 <= p_ebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/EBITDA <= 4',
                'descricao': '''
                Subvalorização significativa, sugerindo que a empresa está barata em relação ao fluxo de caixa. 
                Exemplo: Vale (VALE3) teve P/EBITDA R$30 bilhões) devido a preços de minério elevados.
                 Implicações: Oportunidade para investidores de valor, com potencial de valorização.
                  Recomendações: Confirmar sustentabilidade do EBITDA e exposição a ciclos; ideal para portfólios de 
                  longo prazo focados em valor. 
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'EBITDA elevado pode ser temporário em setores cíclicos; analisar histórico e projeções setoriais',
                'referencia_cruzada': 'Analise evaluate_evebitda para valuation completo e evaluate_margem_ebitda para eficiência operacional. '

            }
        elif 4 < p_ebitda <= 8:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < P/EBITDA <= 8',
                'descricao': '''
                Valuation justo, comum em empresas estáveis. Exemplo: Ambev (ABEV3) pode ter P/EBITDA R$20 bilhões) e 
                liderança no setor de bebidas. Implicações: Equilíbrio entre preço e fluxo de caixa, adequado para 
                investidores moderados. Recomendações: Avaliar crescimento de receita e estabilidade de margens;
                ideal para portfólios diversificados.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Estagnação em setores maduros pode limitar upside; monitorar concorrência',
                'referencia_cruzada': 'Compare com evaluate_p_l para relação com lucros e evaluate_roe para rentabilidade. '

            }
        elif 8 < p_ebitda <= 12:
            return {
                'classificacao': 'Ruim',
                'faixa': '8 < P/EBITDA <= 12',
                'descricao': '''
                Sobrevalorização moderada, comum em empresas com expectativas de crescimento.
                Exemplo: Raia Drogasil (RADL3) pode ter P/EBITDA ~9 devido à expansão no varejo farmacêutico.
                Implicações: Cautela para conservadores; atrativo para crescimento se projeções forem sólidas. 
                Recomendações: Validar crescimento de EBITDA com análise de mercado e concorrentes;
                moderados monitorar expansão de lojas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Expectativas não realizadas podem levar a correções de preço; verificar relatórios trimestrais',
                'referencia_cruzada': 'Verifique evaluate_psr para relação com receita e evaluate_crescimento_ebitda para tendências '
            }
        elif 12 < p_ebitda <= 16:
            return {
                'classificacao': 'Péssimo',
                'faixa': '12 < P/EBITDA <= 16',
                'descricao': '''
                   Valuation elevado, com prêmio significativo. Exemplo: Localiza (RENT3) pode ter P/EBITDA ~12 em 
                   períodos de alta demanda por aluguel de veículos. Implicações: 
                   Risco de correção de preço; menos atrativo para conservadores. Recomendações: 
                   Agressivos devem confirmar fundamentos de crescimento (ex.: frota e receita); conservadores evitar
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Sensibilidade a mudanças macroeconômicas, como aumento de juros ou queda na demanda',
                'referencia_cruzada': 'Combine com evaluate_divida_liquida_ebitda para alavancagem e evaluate_margem_operacional para eficiência'
            }

        elif p_ebitda > 16:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBITDA > 16',
                'descricao': '''
                Especulação elevada, com preço muito acima do fluxo de caixa. Exemplo:
                 Nubank (NUBR33) pode ter P/EBITDA > 15 devido a expectativas de crescimento no setor 
                 financeiro digital. Implicações: Alto risco, adequado apenas para investidores especulativos.
                  Recomendações: Analisar projeções de mercado e concorrência; conservadores evitar completamente. .
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula,
                'riscos': 'Bolhas especulativas ou falha em entregar crescimento podem levar a quedas significativas.',
                'referencia_cruzada': 'Avalie evaluate_peg_ratio para crescimento esperado e evaluate_p_ativo para relação com ativos.'
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique
            os dados de entrada, assegurando que o enterprise value e o EBITDA estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_liquidez_imediata(liquidez_imediata):
    '''
    Avalia a Liquidez Imediata com base em faixas definidas para o mercado brasileiro:
    - Liquidez Imediata < 0.2: Crítico (dificuldade extrema em pagar obrigações imediatas)
    - 0.2 ≤ Liquidez Imediata ≤ 0.5: Ruim (capacidade limitada de pagar obrigações imediatas)
    - 0.5 < Liquidez Imediata ≤ 1: Moderado (capacidade aceitável de pagar obrigações imediatas)
    - 1 < Liquidez Imediata ≤ 1.5: Ótimo (boa capacidade de pagar obrigações imediatas)
    - Liquidez Imediata > 1.5: Fora da faixa (excesso de liquidez, possível ineficiência)
    '''
    definicao = '''
    A Liquidez Imediata mede a capacidade da empresa de pagar suas obrigações de curto prazo
    apenas com caixa e equivalentes, calculada como (Caixa e Equivalentes / Passivo Circulante).
    É um indicador de liquidez que reflete a saúde financeira imediata. Um valor alto sugere
    solidez, enquanto um valor baixo indica risco de inadimplência.
    '''
    agrupador = 'Liquidez'
    formula = 'Liquidez Imediata = Caixa e Equivalentes / Passivo Circulante'

    try:
        if liquidez_imediata < 0.2:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Liquidez Imediata < 0.2',
                'descricao': '''
                Uma Liquidez Imediata abaixo de 0.2 indica dificuldade extrema em pagar obrigações de
                curto prazo com caixa disponível, sugerindo risco elevado. Isso é comum em empresas
                em crise, como a Gol (GOLL4). Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 <= liquidez_imediata <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 <= Liquidez Imediata <= 0.5',
                'descricao': '''
                Uma Liquidez Imediata entre 0.2 e 0.5 reflete capacidade limitada de pagar obrigações
                imediatas, indicando dependência de conversão de outros ativos. Isso é comum em setores
                com margens apertadas, como varejo (ex.: Casas Bahia - BHIA3). Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < liquidez_imediata <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Liquidez Imediata <= 1',
                'descricao': '''
                Uma Liquidez Imediata entre 0.5 e 1 indica capacidade aceitável de pagar obrigações
                imediatas. Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para
                investidores, essa faixa sugere equilíbrio entre liquidez e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < liquidez_imediata <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Liquidez Imediata <= 1.5',
                'descricao': '''
                Uma Liquidez Imediata entre 1 e 1.5 reflete boa capacidade de pagar obrigações imediatas,
                indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam
                liquidez nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif liquidez_imediata > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez Imediata > 1.5',
                'descricao': '''
                Uma Liquidez Imediata acima de 1.5 indica excesso de liquidez, com caixa muito superior
                às obrigações de curto prazo. Isso pode ocorrer em empresas como a Vale (VALE3) em
                períodos de alta geração de caixa. Para investidores, essa faixa pode indicar
                ineficiência na alocação de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Liquidez Imediata: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se o passivo circulante for zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que o caixa e o passivo
            circulante estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_receita(crescimento_receita):
    '''
    Avalia o Crescimento da Receita com base em faixas definidas para o mercado brasileiro:
    - Crescimento Receita < 0%: Crítico (redução de receita, risco elevado)
    - 0% ≤ Crescimento Receita ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento Receita ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento Receita ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento Receita > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento da Receita mede a taxa anual de aumento da receita bruta, calculada como
    ((Receita Final / Receita Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador
    de crescimento que reflete a capacidade da empresa de expandir suas vendas. Um crescimento
    alto sugere sucesso comercial, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Receita = ((Receita Final / Receita Inicial)^(1/n) - 1)'

    try:
        if crescimento_receita < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Receita < 0%',
                'descricao': '''
                Um Crescimento da Receita negativo indica redução nas vendas, sugerindo dificuldades
                comerciais ou de mercado. Isso é comum em empresas em crise, como a Gol (GOLL4).
                Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_receita <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Receita <= 5%',
                'descricao': '''
                Um Crescimento da Receita entre 0% e 5% reflete crescimento baixo ou estagnação,
                indicando dificuldade em expandir as vendas. Isso é comum em setores maduros, como
                varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_receita <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento Receita <= 15%',
                'descricao': '''
                Um Crescimento da Receita entre 5% e 15% indica crescimento aceitável, típico de
                empresas com estabilidade comercial. Empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio entre crescimento
                e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_receita <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento Receita <= 25%',
                'descricao': '''
                Um Crescimento da Receita entre 15% e 25% reflete crescimento robusto, indicando
                forte expansão das vendas. Empresas como a Magazine Luiza (MGLU3) podem apresentar
                crescimento nessa faixa em períodos de expansão. Para investidores, essa faixa é
                atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_receita > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Receita > 25%',
                'descricao': '''
                Um Crescimento da Receita acima de 25% é excepcional, indicando aumento extremamente
                rápido das vendas. Isso pode ocorrer em empresas como o Nubank (NUBR33) em períodos
                de forte crescimento. Para investidores, essa faixa é altamente atrativa, mas exige
                cautela, pois crescimentos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento da Receita: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se a receita inicial for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que as receitas
            inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_8.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Margem Operacional, Dívida/Ativo, EV/EBIT, Payout Ratio.
"""


def evaluate_margem_operacional(margem_operacional):
    '''
    Avalia a Margem Operacional com base em faixas definidas para o mercado brasileiro:
    - Margem Operacional < 0%: Crítico (lucratividade operacional negativa, risco elevado)
    - 0% ≤ Margem Operacional ≤ 5%: Ruim (lucratividade operacional baixa)
    - 5% < Margem Operacional ≤ 15%: Moderado (lucratividade operacional aceitável)
    - 15% < Margem Operacional ≤ 25%: Ótimo (lucratividade operacional robusta)
    - Margem Operacional > 25%: Fora da faixa (lucratividade operacional excepcional)
    '''
    definicao = '''
    A Margem Operacional mede a proporção do lucro operacional em relação à receita bruta,
    calculada como (EBIT / Receita Bruta). É um indicador de rentabilidade que reflete a
    eficiência da empresa em gerar lucro a partir de suas operações principais. Uma margem
    alta sugere forte desempenho operacional, enquanto uma margem baixa indica dificuldades.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem Operacional = EBIT / Receita Bruta'

    try:
        if margem_operacional < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem Operacional < 0%',
                'descricao': '''
                Uma Margem Operacional negativa indica prejuízo operacional, sugerindo que a empresa
                não consegue cobrir custos operacionais com sua receita. Isso é comum em empresas em
                crise, como a Oi (OIBR3). Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_operacional <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Margem Operacional <= 5%',
                'descricao': '''
                Uma Margem Operacional entre 0% e 5% reflete lucratividade operacional baixa,
                indicando desafios na gestão de custos. Isso é comum em setores com margens apertadas,
                como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < margem_operacional <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Margem Operacional <= 15%',
                'descricao': '''
                Uma Margem Operacional entre 5% e 15% indica lucratividade operacional aceitável,
                típico de empresas com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < margem_operacional <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Margem Operacional <= 25%',
                'descricao': '''
                Uma Margem Operacional entre 15% e 25% reflete lucratividade operacional robusta,
                indicando forte controle de custos e eficiência. Empresas como a Ambev (ABEV3)
                frequentemente apresentam margem nessa faixa. Para investidores, essa faixa é
                atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_operacional > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem Operacional > 25%',
                'descricao': '''
                Uma Margem Operacional acima de 25% é excepcional, indicando altíssima eficiência
                operacional. Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores,
                essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem
                não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem Operacional: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que o EBIT e a receita bruta
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_ativo(divida_ativo):
    '''
    Avalia a Dívida/Ativo com base em faixas definidas para o mercado brasileiro:
    - Dívida/Ativo < 0: Fora da faixa (sem dívida ou ativo negativo)
    - 0 ≤ Dívida/Ativo ≤ 0.2: Ótimo (endividamento muito baixo)
    - 0.2 < Dívida/Ativo ≤ 0.4: Moderado (endividamento aceitável)
    - 0.4 < Dívida/Ativo ≤ 0.6: Ruim (endividamento elevado)
    - 0.6 < Dívida/Ativo ≤ 0.8: Péssimo (endividamento muito alto)
    - Dívida/Ativo > 0.8: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida/Ativo mede a proporção da dívida total em relação aos ativos totais, calculada
    como (Dívida Total / Ativos Totais). É um indicador de alavancagem financeira que avalia
    o nível de endividamento em relação aos ativos da empresa. Um valor baixo sugere solidez
    financeira, enquanto um valor alto indica maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida/Ativo = Dívida Total / Ativos Totais'

    try:
        if divida_ativo < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida/Ativo < 0',
                'descricao': '''
                Uma Dívida/Ativo negativa indica que a empresa não tem dívida ou que os ativos totais
                são negativos, o que é extremamente raro e alarmante. Para investidores, essa faixa
                exige análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_ativo <= 0.2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida/Ativo <= 0.2',
                'descricao': '''
                Uma Dívida/Ativo entre 0 e 0.2 reflete endividamento muito baixo, indicando solidez
                financeira. Empresas como a Vale (VALE3) em períodos de alta geração de caixa podem
                operar nessa faixa. Para investidores, essa faixa é atrativa, sugerindo baixo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < divida_ativo <= 0.4:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < Dívida/Ativo <= 0.4',
                'descricao': '''
                Uma Dívida/Ativo entre 0.2 e 0.4 indica endividamento aceitável, com equilíbrio entre
                dívida e ativos. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.4 < divida_ativo <= 0.6:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.4 < Dívida/Ativo <= 0.6',
                'descricao': '''
                Uma Dívida/Ativo entre 0.4 e 0.6 sugere endividamento elevado, indicando dependência
                significativa de dívidas. Isso é comum em setores intensivos em capital, como a
                Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < divida_ativo <= 0.8:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0.6 < Dívida/Ativo <= 0.8',
                'descricao': '''
                Uma Dívida/Ativo entre 0.6 e 0.8 reflete endividamento muito alto, indicando risco
                significativo. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises.
                Para investidores, essa faixa é preocupante.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_ativo > 0.8:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida/Ativo > 0.8',
                'descricao': '''
                Uma Dívida/Ativo acima de 0.8 indica endividamento excessivo, sugerindo dependência
                extrema de dívidas. Isso é típico de empresas em dificuldades, como a Gol (GOLL4)
                em crises. Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida/Ativo: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se os ativos totais forem zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a dívida total
            e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_ev_ebit(ev_ebit):
    '''
    Avalia o Enterprise Value/EBIT com base em faixas definidas para o mercado brasileiro:
    - EV/EBIT < 0: Crítico (EBIT negativo, risco elevado)
    - 0 ≤ EV/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < EV/EBIT ≤ 10: Moderado (valuation justo)
    - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < EV/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Enterprise Value/EBIT compara o valor da empresa (valor de mercado + dívida líquida)
    ao lucro operacional antes de juros e impostos, calculado como (Enterprise Value / EBIT).
    É um indicador de valuation que avalia se a empresa está cara ou barata em relação à sua
    lucratividade operacional. Um EV/EBIT baixo sugere subvalorização, enquanto um valor alto
    indica sobrevalorização.
    '''
    agrupador = 'Valuation'
    formula = 'EV/EBIT = Enterprise Value / EBIT'

    try:
        if ev_ebit < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'EV/EBIT < 0',
                'descricao': '''
                Um EV/EBIT negativo indica que a empresa tem EBIT negativo, sugerindo prejuízo
                operacional. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ev_ebit <= 5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= EV/EBIT <= 5',
                'descricao': '''
                Um EV/EBIT entre 0 e 5 sugere que a empresa está subvalorizada, sendo uma potencial
                oportunidade de compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em
                períodos de baixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ev_ebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < EV/EBIT <= 10',
                'descricao': '''
                Um EV/EBIT entre 5 e 10 reflete um valuation justo, típico de empresas com
                lucratividade estável. Empresas como a Ambev (ABEV3) frequentemente operam nessa
                faixa. Para investidores, essa faixa sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < ev_ebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < EV/EBIT <= 15',
                'descricao': '''
                Um EV/EBIT entre 10 e 15 sugere que a empresa está sobrevalorizada, indicando
                que o mercado espera crescimento significativo. Empresas como a Raia Drogasil
                (RADL3) podem atingir essa faixa. Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < ev_ebit <= 20:
            return {
                'classificacao': 'Péssimo',
                'faixa': '15 < EV/EBIT <= 20',
                'descricao': '''
                Um EV/EBIT entre 15 e 20 indica que a empresa é muito cara, sugerindo que o
                mercado está pagando um prêmio elevado. Empresas como a Localiza (RENT3) podem
                apresentar EV/EBIT nessa faixa em momentos de otimismo. Para investidores, essa
                faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif ev_ebit > 20:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBIT > 20',
                'descricao': '''
                Um EV/EBIT acima de 20 é extremamente elevado, geralmente associado a empresas com
                altíssimas expectativas de crescimento, como o Nubank (NUBR33). Para investidores,
                essa faixa reflete especulação e alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o EV/EBIT: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique
            os dados de entrada, assegurando que o enterprise value e o EBIT estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_payout_ratio(payout_ratio):
    '''
    Avalia o Payout Ratio com base em faixas definidas para o mercado brasileiro:
    - Payout Ratio < 0%: Fora da faixa (sem dividendos ou prejuízo)
    - 0% ≤ Payout Ratio ≤ 30%: Ruim (baixa distribuição de dividendos)
    - 30% < Payout Ratio ≤ 60%: Moderado (distribuição equilibrada de dividendos)
    - 60% < Payout Ratio ≤ 80%: Ótimo (alta distribuição de dividendos)
    - Payout Ratio > 80%: Crítico (distribuição muito alta, risco de insustentabilidade)
    '''
    definicao = '''
    O Payout Ratio mede a proporção do lucro líquido distribuído como dividendos, calculada
    como (Dividendos / Lucro Líquido). É um indicador que reflete a política de dividendos da
    empresa. Um payout alto é atrativo para investidores focados em renda, mas pode indicar
    risco se for insustentável.
    '''
    agrupador = 'Dividendos'
    formula = 'Payout Ratio = Dividendos / Lucro Líquido'

    try:
        if payout_ratio < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Payout Ratio < 0%',
                'descricao': '''
                Um Payout Ratio negativo ou zero indica que a empresa não paga dividendos, seja por
                prejuízo ou reinvestimento total dos lucros. Isso é comum em empresas em crescimento,
                como o Nubank (NUBR33). Para investidores focados em renda, essa faixa é desvantajosa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= payout_ratio <= 30:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Payout Ratio <= 30%',
                'descricao': '''
                Um Payout Ratio entre 0% e 30% reflete baixa distribuição de dividendos, indicando que
                a empresa prioriza reinvestimento. Isso é comum em empresas como a Magazine Luiza
                (MGLU3). Para investidores focados em renda, essa faixa é pouco atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 30 < payout_ratio <= 60:
            return {
                'classificacao': 'Moderado',
                'faixa': '30% < Payout Ratio <= 60%',
                'descricao': '''
                Um Payout Ratio entre 30% e 60% indica distribuição equilibrada de dividendos, com
                equilíbrio entre distribuição e reinvestimento. Empresas como a Vale (VALE3)
                frequentemente operam nessa faixa. Para investidores, essa faixa é adequada para
                quem busca renda moderada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 60 < payout_ratio <= 80:
            return {
                'classificacao': 'Ótimo',
                'faixa': '60% < Payout Ratio <= 80%',
                'descricao': '''
                Um Payout Ratio entre 60% e 80% reflete alta distribuição de dividendos, indicando
                que a empresa distribui uma parte significativa dos lucros. Empresas como a Engie
                Brasil (EGIE3) frequentemente apresentam payout nessa faixa. Para investidores,
                essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif payout_ratio > 80:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Payout Ratio > 80%',
                'descricao': '''
                Um Payout Ratio acima de 80% indica distribuição muito alta, sugerindo risco de
                insustentabilidade dos dividendos. Empresas como a Taesa (TAEE11) podem apresentar
                payouts elevados, mas isso exige cautela, pois pode comprometer o crescimento.
                Para investidores, a análise deve focar no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Payout Ratio: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se o lucro líquido for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que os dividendos e o lucro
            líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_9.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: ROA, CAPEX/Receita, Dívida Bruta/EBITDA, Crescimento da Margem de Lucro Bruto.
"""


def evaluate_roa(roa):
    '''
    Avalia o Retorno sobre Ativos (ROA) com base em faixas definidas para o mercado brasileiro:
    - ROA < 0%: Crítico (prejuízo, destruição de valor)
    - 0% ≤ ROA ≤ 3%: Ruim (retorno baixo, ineficiência)
    - 3% < ROA ≤ 8%: Moderado (retorno aceitável)
    - 8% < ROA ≤ 15%: Ótimo (retorno robusto)
    - ROA > 15%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre Ativos (ROA) mede a rentabilidade dos ativos totais, calculado como
    (Lucro Líquido / Ativos Totais). É um indicador de eficiência que mostra quanto a empresa
    gera de lucro com seus ativos. Um ROA alto sugere eficiência, enquanto um valor baixo ou
    negativo indica ineficiência ou prejuízo.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROA = Lucro Líquido / Ativos Totais'

    try:
        if roa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROA < 0%',
                'descricao': '''
                Um ROA negativo indica que a empresa está gerando prejuízo, destruindo valor com
                seus ativos. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave, exigindo análise detalhada da gestão de ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roa <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROA <= 3%',
                'descricao': '''
                Um ROA entre 0% e 3% reflete retorno baixo, indicando ineficiência no uso dos ativos.
                Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3).
                Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < roa <= 8:
            return {
                'classificacao': 'Moderado',
                'faixa': '3% < ROA <= 8%',
                'descricao': '''
                Um ROA entre 3% e 8% indica retorno aceitável, típico de empresas com eficiência
                moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre rentabilidade e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 8 < roa <= 15:
            return {
                'classificacao': 'Ótimo',
                'faixa': '8% < ROA <= 15%',
                'descricao': '''
                Um ROA entre 8% e 15% reflete retorno robusto, indicando que a empresa utiliza seus
                ativos de forma eficiente. Empresas como a Ambev (ABEV3) frequentemente apresentam
                ROA nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roa > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROA > 15%',
                'descricao': '''
                Um ROA acima de 15% é excepcional, indicando retornos extremamente altos com os ativos.
                Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa é
                altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o lucro líquido e os ativos totais
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_capex_receita(capex_receita):
    '''
    Avalia o CAPEX/Receita com base em faixas definidas para o mercado brasileiro:
    - CAPEX/Receita < 5%: Ruim (baixo investimento em ativos fixos)
    - 5% ≤ CAPEX/Receita ≤ 10%: Moderado (investimento equilibrado)
    - 10% < CAPEX/Receita ≤ 20%: Ótimo (investimento robusto)
    - 20% < CAPEX/Receita ≤ 30%: Crítico (investimento elevado, risco de alavancagem)
    - CAPEX/Receita > 30%: Fora da faixa (investimento excessivo, alto risco)
    '''
    definicao = '''
    O CAPEX/Receita mede a proporção dos gastos de capital (CAPEX) em relação à receita bruta,
    calculada como (CAPEX / Receita Bruta). É um indicador de investimento que reflete quanto a
    empresa está investindo em ativos fixos para crescimento futuro. Um valor equilibrado sugere
    planejamento estratégico, enquanto valores muito altos ou baixos podem indicar problemas.
    '''
    agrupador = 'Investimento'
    formula = 'CAPEX/Receita = CAPEX / Receita Bruta'

    try:
        if capex_receita < 5:
            return {
                'classificacao': 'Ruim',
                'faixa': 'CAPEX/Receita < 5%',
                'descricao': '''
                Um CAPEX/Receita abaixo de 5% indica baixo investimento em ativos fixos, sugerindo
                que a empresa pode estar negligenciando crescimento futuro. Isso é comum em empresas
                maduras com baixa necessidade de expansão, como a Engie Brasil (EGIE3). Para
                investidores, essa faixa pode indicar estagnação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 <= capex_receita <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% <= CAPEX/Receita <= 10%',
                'descricao': '''
                Um CAPEX/Receita entre 5% e 10% reflete investimento equilibrado, indicando que a
                empresa está mantendo ativos sem comprometer a liquidez. Empresas como a Ambev (ABEV3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < capex_receita <= 20:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < CAPEX/Receita <= 20%',
                'descricao': '''
                Um CAPEX/Receita entre 10% e 20% indica investimento robusto, sugerindo que a empresa
                está focada em crescimento futuro sem comprometer a saúde financeira. Empresas como a
                Vale (VALE3) podem apresentar CAPEX nessa faixa em períodos de expansão. Para
                investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < capex_receita <= 30:
            return {
                'classificacao': 'Crítico',
                'faixa': '20% < CAPEX/Receita <= 30%',
                'descricao': '''
                Um CAPEX/Receita entre 20% e 30% reflete investimento elevado, indicando risco de
                alavancagem financeira para sustentar expansões. Isso é comum em setores intensivos
                em capital, como a Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif capex_receita > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'CAPEX/Receita > 30%',
                'descricao': '''
                Um CAPEX/Receita acima de 30% indica investimento excessivo, sugerindo que a empresa
                pode estar comprometendo sua saúde financeira. Isso pode ocorrer em empresas como a
                CSN (CSNA3) em grandes projetos. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o CAPEX/Receita: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que o CAPEX e a receita bruta
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_bruta_ebitda(divida_bruta_ebitda):
    '''
    Avalia a Dívida Bruta/EBITDA com base em faixas definidas para o mercado brasileiro:
    - Dívida Bruta/EBITDA < 0: Fora da faixa (sem dívida ou EBITDA negativo)
    - 0 ≤ Dívida Bruta/EBITDA ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida Bruta/EBITDA ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida Bruta/EBITDA ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida Bruta/EBITDA ≤ 4: Péssimo (endividamento muito alto)
    - Dívida Bruta/EBITDA > 4: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida Bruta/EBITDA mede a proporção da dívida bruta em relação ao lucro antes de juros,
    impostos, depreciação e amortização, calculada como (Dívida Bruta / EBITDA). É um indicador
    de alavancagem financeira que avalia a capacidade da empresa de pagar sua dívida com base em
    sua geração de caixa operacional. Um valor baixo sugere solidez, enquanto um valor alto indica
    maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Bruta/EBITDA = Dívida Bruta / EBITDA'

    try:
        if divida_bruta_ebitda < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Bruta/EBITDA < 0',
                'descricao': '''
                Uma Dívida Bruta/EBITDA negativa indica que a empresa não tem dívida ou que o EBITDA
                é negativo, o que é alarmante. Empresas como a Oi (OIBR3) podem apresentar EBITDA
                negativo em crises. Para investidores, essa faixa exige análise detalhada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_bruta_ebitda <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Bruta/EBITDA <= 1',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 0 e 1 reflete endividamento muito baixo, indicando
                forte capacidade de pagamento da dívida. Empresas como a Vale (VALE3) em períodos
                de alta geração de caixa operam nessa faixa. Para investidores, essa faixa é
                atrativa, sugerindo baixo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_bruta_ebitda <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida Bruta/EBITDA <= 2',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 1 e 2 indica endividamento aceitável, com equilíbrio
                entre dívida e geração de caixa. Empresas como a Ambev (ABEV3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_bruta_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Bruta/EBITDA <= 3',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 2 e 3 sugere endividamento elevado, indicando maior
                dependência de dívidas. Isso é comum em setores intensivos em capital, como a
                Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_bruta_ebitda <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida Bruta/EBITDA <= 4',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 3 e 4 reflete endividamento muito alto, indicando
                risco significativo. Empresas como a Gol (GOLL4) já estiveram nessa faixa durante
                crises. Para investidores, essa faixa é preocupante.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_bruta_ebitda > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Bruta/EBITDA > 4',
                'descricao': '''
                Uma Dívida Bruta/EBITDA acima de 4 indica endividamento excessivo, sugerindo
                dificuldades em pagar dívidas com a geração de caixa. Isso é típico de empresas em
                dificuldades, como a Oi (OIBR3). Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida Bruta/EBITDA: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o EBITDA for zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a dívida bruta
            e o EBITDA estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_margem_lucro_bruto(crescimento_margem_lucro_bruto):
    '''
    Avalia o Crescimento da Margem de Lucro Bruto com base em faixas definidas para o mercado brasileiro:
    - Crescimento Margem Bruta < 0%: Crítico (redução da margem, risco elevado)
    - 0% ≤ Crescimento Margem Bruta ≤ 2%: Ruim (crescimento baixo ou estagnação)
    - 2% < Crescimento Margem Bruta ≤ 5%: Moderado (crescimento aceitável)
    - 5% < Crescimento Margem Bruta ≤ 10%: Ótimo (crescimento robusto)
    - Crescimento Margem Bruta > 10%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento da Margem de Lucro Bruto mede a taxa anual de aumento da margem de lucro bruto,
    calculada como ((Margem Bruta Final / Margem Bruta Inicial)^(1/n) - 1), onde n é o número
    de anos. É um indicador de eficiência operacional que reflete a capacidade da empresa de
    melhorar a relação entre receita e custo dos bens vendidos. Um crescimento alto sugere
    melhoria na eficiência, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Margem Bruta = ((Margem Bruta Final / Margem Bruta Inicial)^(1/n) - 1)'

    try:
        if crescimento_margem_lucro_bruto < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Margem Bruta < 0%',
                'descricao': '''
                Um Crescimento da Margem Bruta negativo indica redução na margem de lucro bruto,
                sugerindo aumento nos custos ou queda nos preços de venda. Isso é comum em empresas
                em setores competitivos, como a Casas Bahia (BHIA3). Para investidores, essa faixa
                é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_margem_lucro_bruto <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Margem Bruta <= 2%',
                'descricao': '''
                Um Crescimento da Margem Bruta entre 0% e 2% reflete crescimento baixo ou estagnação,
                indicando dificuldade em melhorar a eficiência operacional. Isso é comum em setores
                maduros, como o varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa
                faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < crescimento_margem_lucro_bruto <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Crescimento Margem Bruta <= 5%',
                'descricao': '''
                Um Crescimento da Margem Bruta entre 2% e 5% indica crescimento aceitável, típico
                de empresas com melhorias graduais na eficiência. Empresas como a Suzano (SUZB3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_margem_lucro_bruto <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Crescimento Margem Bruta <= 10%',
                'descricao': '''
                Um Crescimento da Margem Bruta entre 5% e 10% reflete crescimento robusto, indicando
                forte melhoria na eficiência operacional. Empresas como a Magazine Luiza (MGLU3)
                podem apresentar crescimento nessa faixa em períodos de expansão. Para investidores,
                essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_margem_lucro_bruto > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Margem Bruta > 10%',
                'descricao': '''
                Um Crescimento da Margem Bruta acima de 10% é excepcional, indicando aumento
                extremamente rápido na eficiência operacional. Isso pode ocorrer em empresas como
                o Nubank (NUBR33) em períodos de forte otimização. Para investidores, essa faixa
                é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não
                ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento da Margem Bruta: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se a margem bruta inicial for
            zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que as
            margens brutas inicial e final estejam corretas e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Dividend Yield, Free Cash Flow Yield, Giro de Ativos, Crescimento do Lucro Líquido.
"""


def evaluate_dividend_yield(dividend_yield):
    '''
    Avalia o Dividend Yield com base em faixas definidas para o mercado brasileiro:
    - Dividend Yield < 0%: Fora da faixa (sem dividendos)
    - 0% ≤ Dividend Yield ≤ 2%: Ruim (retorno baixo com dividendos)
    - 2% < Dividend Yield ≤ 5%: Moderado (retorno aceitável com dividendos)
    - 5% < Dividend Yield ≤ 8%: Ótimo (retorno robusto com dividendos)
    - Dividend Yield > 8%: Crítico (retorno muito alto, risco de insustentabilidade)
    '''
    definicao = '''
    O Dividend Yield mede o retorno anual dos dividendos em relação ao preço da ação, calculado
    como (Dividendos por Ação / Preço da Ação). É um indicador que reflete a atratividade da
    empresa para investidores focados em renda passiva. Um yield alto é atrativo, mas pode indicar
    risco se for insustentável.
    '''
    agrupador = 'Dividendos'
    formula = 'Dividend Yield = Dividendos por Ação / Preço da Ação'

    try:
        if dividend_yield < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dividend Yield < 0%',
                'descricao': '''
                Um Dividend Yield negativo ou zero indica que a empresa não paga dividendos, seja
                por prejuízo ou reinvestimento total dos lucros. Isso é comum em empresas em
                crescimento, como o Nubank (NUBR33). Para investidores focados em renda, essa faixa
                é desvantajosa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dividend_yield <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Dividend Yield <= 2%',
                'descricao': '''
                Um Dividend Yield entre 0% e 2% reflete retorno baixo com dividendos, indicando que
                a empresa prioriza reinvestimento. Isso é comum em empresas como a Magazine Luiza
                (MGLU3). Para investidores focados em renda, essa faixa é pouco atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < dividend_yield <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Dividend Yield <= 5%',
                'descricao': '''
                Um Dividend Yield entre 2% e 5% indica retorno aceitável com dividendos, com equilíbrio
                entre distribuição e reinvestimento. Empresas como a Vale (VALE3) frequentemente
                operam nessa faixa. Para investidores, essa faixa é adequada para quem busca renda
                moderada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < dividend_yield <= 8:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Dividend Yield <= 8%',
                'descricao': '''
                Um Dividend Yield entre 5% e 8% reflete retorno robusto com dividendos, indicando
                que a empresa distribui uma parte significativa dos lucros. Empresas como a Engie
                Brasil (EGIE3) frequentemente apresentam yield nessa faixa. Para investidores, essa
                faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif dividend_yield > 8:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dividend Yield > 8%',
                'descricao': '''
                Um Dividend Yield acima de 8% indica retorno muito alto, mas pode sugerir risco de
                insustentabilidade dos dividendos. Empresas como a Taesa (TAEE11) podem apresentar
                yields elevados, mas isso exige cautela, pois pode comprometer o crescimento. Para
                investidores, a análise deve focar no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Dividend Yield: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se o preço da ação for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que os dividendos por ação
            e o preço da ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_free_cash_flow_yield(free_cash_flow_yield):
    '''
    Avalia o Free Cash Flow Yield com base em faixas definidas para o mercado brasileiro:
    - Free Cash Flow Yield < 0%: Crítico (fluxo de caixa livre negativo, risco elevado)
    - 0% ≤ Free Cash Flow Yield ≤ 3%: Ruim (geração de caixa baixa)
    - 3% < Free Cash Flow Yield ≤ 6%: Moderado (geração de caixa aceitável)
    - 6% < Free Cash Flow Yield ≤ 10%: Ótimo (geração de caixa robusta)
    - Free Cash Flow Yield > 10%: Fora da faixa (geração de caixa excepcional)
    '''
    definicao = '''
    O Free Cash Flow Yield mede o fluxo de caixa livre por ação em relação ao preço da ação,
    calculado como (Fluxo de Caixa Livre por Ação / Preço da Ação). É um indicador que reflete
    a capacidade da empresa de gerar caixa disponível após despesas operacionais e investimentos.
    Um yield alto sugere solidez financeira, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Fluxo de Caixa'
    formula = 'Free Cash Flow Yield = Fluxo de Caixa Livre por Ação / Preço da Ação'

    try:
        if free_cash_flow_yield < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Free Cash Flow Yield < 0%',
                'descricao': '''
                Um Free Cash Flow Yield negativo indica que a empresa não gera fluxo de caixa livre,
                sugerindo dificuldades financeiras. Isso é comum em empresas em crise, como a Gol
                (GOLL4). Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= free_cash_flow_yield <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Free Cash Flow Yield <= 3%',
                'descricao': '''
                Um Free Cash Flow Yield entre 0% e 3% reflete geração de caixa baixa, indicando
                desafios na geração de fluxo de caixa livre. Isso é comum em setores com altos
                investimentos, como a Petrobras (PETR4). Para investidores, essa faixa sugere
                risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < free_cash_flow_yield <= 6:
            return {
                'classificacao': 'Moderado',
                'faixa': '3% < Free Cash Flow Yield <= 6%',
                'descricao': '''
                Um Free Cash Flow Yield entre 3% e 6% indica geração de caixa aceitável, típico
                de empresas com eficiência moderada. Empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 6 < free_cash_flow_yield <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '6% < Free Cash Flow Yield <= 10%',
                'descricao': '''
                Um Free Cash Flow Yield entre 6% e 10% reflete geração de caixa robusta, indicando
                forte saúde financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam
                yield nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif free_cash_flow_yield > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Free Cash Flow Yield > 10%',
                'descricao': '''
                Um Free Cash Flow Yield acima de 10% é excepcional, indicando geração de caixa
                extremamente alta. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos
                de alta lucratividade. Para investidores, essa faixa é altamente atrativa, mas
                exige cautela, pois yields tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Free Cash Flow Yield: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o preço da ação for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que o fluxo
            de caixa livre por ação e o preço da ação estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_giro_ativos(giro_ativos):
    '''
    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
    - Giro de Ativos < 0.3: Crítico (baixa eficiência no uso de ativos)
    - 0.3 ≤ Giro de Ativos ≤ 0.6: Ruim (eficiência baixa)
    - 0.6 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável)
    - 1 < Giro de Ativos ≤ 1.5: Ótimo (eficiência robusta)
    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional)
    '''
    definicao = '''
    O Giro de Ativos mede a eficiência com que a empresa utiliza seus ativos para gerar receita,
    calculado como (Receita Bruta / Ativos Totais). É um indicador de eficiência operacional
    que reflete a capacidade da empresa de maximizar o uso de seus ativos. Um giro alto sugere
    eficiência, enquanto um giro baixo indica subutilização.
    '''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

    try:
        if giro_ativos < 0.3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Giro de Ativos < 0.3',
                'descricao': '''
                Um Giro de Ativos abaixo de 0.3 indica baixa eficiência no uso dos ativos, sugerindo
                subutilização ou ativos ociosos. Isso é comum em empresas em crise, como a Oi (OIBR3).
                Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 <= giro_ativos <= 0.6:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.3 <= Giro de Ativos <= 0.6',
                'descricao': '''
                Um Giro de Ativos entre 0.3 e 0.6 reflete eficiência baixa, indicando que a empresa
                tem dificuldade em gerar receita com seus ativos. Isso é comum em setores intensivos
                em capital, como a Petrobras (PETR4). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < giro_ativos <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.6 < Giro de Ativos <= 1',
                'descricao': '''
                Um Giro de Ativos entre 0.6 e 1 indica eficiência aceitável, típico de empresas com
                utilização moderada de ativos. Empresas como a Suzano (SUZB3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < giro_ativos <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Giro de Ativos <= 1.5',
                'descricao': '''
                Um Giro de Ativos entre 1 e 1.5 reflete eficiência robusta, indicando que a empresa
                utiliza seus ativos de forma eficaz. Empresas como a Ambev (ABEV3) frequentemente
                apresentam giro nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif giro_ativos > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro de Ativos > 1.5',
                'descricao': '''
                Um Giro de Ativos acima de 1.5 é excepcional, indicando eficiência extremamente alta
                no uso dos ativos. Isso pode ocorrer em empresas como a Magazine Luiza (MGLU3) em
                períodos de alta rotatividade. Para investidores, essa faixa é altamente atrativa,
                mas exige análise da sustentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se os ativos totais forem zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta
            e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_lucro_liquido(crescimento_lucro_liquido):
    '''
    Avalia o Crescimento do Lucro Líquido com base em faixas definidas para o mercado brasileiro:
    - Crescimento Lucro Líquido < 0%: Crítico (redução do lucro, risco elevado)
    - 0% ≤ Crescimento Lucro Líquido ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento Lucro Líquido ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento Lucro Líquido ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento Lucro Líquido > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento do Lucro Líquido mede a taxa anual de aumento do lucro líquido, calculada
    como ((Lucro Líquido Final / Lucro Líquido Inicial)^(1/n) - 1), onde n é o número de anos.
    É um indicador de crescimento que reflete a capacidade da empresa de aumentar sua
    lucratividade final. Um crescimento alto sugere sucesso financeiro, enquanto um valor baixo
    ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Lucro Líquido = ((Lucro Líquido Final / Lucro Líquido Inicial)^(1/n) - 1)'

    try:
        if crescimento_lucro_liquido < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Lucro Líquido < 0%',
                'descricao': '''
                Um Crescimento do Lucro Líquido negativo indica redução nos lucros, sugerindo
                dificuldades financeiras ou operacionais. Isso é comum em empresas em crise, como
                a Gol (GOLL4). Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_lucro_liquido <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Lucro Líquido <= 5%',
                'descricao': '''
                Um Crescimento do Lucro Líquido entre 0% e 5% reflete crescimento baixo ou
                estagnação, indicando dificuldade em expandir a lucratividade. Isso é comum em
                setores maduros, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_lucro_liquido <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento Lucro Líquido <= 15%',
                'descricao': '''
                Um Crescimento do Lucro Líquido entre 5% e 15% indica crescimento aceitável,
                típico de empresas com estabilidade financeira. Empresas como a Suzano (SUZB3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_lucro_liquido <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento Lucro Líquido <= 25%',
                'descricao': '''
                Um Crescimento do Lucro Líquido entre 15% e 25% reflete crescimento robusto,
                indicando forte expansão da lucratividade. Empresas como a Magazine Luiza (MGLU3)
                podem apresentar crescimento nessa faixa em períodos de expansão. Para investidores,
                essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_lucro_liquido > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Lucro Líquido > 25%',
                'descricao': '''
                Um Crescimento do Lucro Líquido acima de 25% é excepcional, indicando aumento
                extremamente rápido da lucratividade. Isso pode ocorrer em empresas como o Nubank
                (NUBR33) em períodos de forte crescimento. Para investidores, essa faixa é
                altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não
                ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento do Lucro Líquido: {str(e)}. Isso pode
            ter acontecido se o valor fornecido não for numérico ou se o lucro líquido inicial
            for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que
            os lucros líquidos inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }
    """
    analisefundamentalista_10.py
    Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
    e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
    Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
    Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
    Indicadores incluídos: P/EBIT, Margem EBITDA, Liquidez Corrente, Crescimento da Receita.
    """

def evaluate_pebit(pebit):
        '''
        Avalia o Preço/EBIT com base em faixas definidas para o mercado brasileiro:
        - P/EBIT < 0: Crítico (EBIT negativo, risco elevado)
        - 0 ≤ P/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
        - 5 < P/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
        - 10 < P/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
        - 15 < P/EBIT ≤ 20: Péssimo (muito caro, alto risco)
        - P/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)
        '''
        definicao = '''
        Indicador que relaciona o preço da ação ao EBIT, medindo a capacidade da empresa de gerar
        lucro operacional em relação ao seu valor de mercado. É útil para avaliar a lucratividade
        antes de impostos e juros.
        '''
        agrupador = 'Valuation'
        formula = 'P/EBIT = Preço da Ação / EBIT por Ação'

        try:
            if pebit < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'P/EBIT < 0',
                    'descricao': '''
                    P/EBIT negativo indica EBIT negativo, sugerindo ineficiência operacional ou prejuízo.
                    Comum em setores com alta depreciação (ex.: siderurgia, como CSNA3). Exige análise
                    de fluxo de caixa.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= pebit <= 5:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '0 <= P/EBIT <= 5',
                    'descricao': '''
                    P/EBIT baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores
                    cíclicos (ex.: mineração como VALE3) ou empresas com desafios temporários.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < pebit <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5 < P/EBIT <= 10',
                    'descricao': '''
                    P/EBIT indica valuation justo, típico de empresas com geração de lucro operacional
                    estável (ex.: energia como ELET3). Equilíbrio entre risco e retorno.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < pebit <= 15:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '10 < P/EBIT <= 15',
                    'descricao': '''
                    P/EBIT elevado sugere sobrevalorização moderada, comum em setores de crescimento
                    (ex.: varejo como MGLU3). Exige análise de margens e crescimento futuro.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 15 < pebit <= 20:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '15 < P/EBIT <= 20',
                    'descricao': '''
                    P/EBIT muito alto indica ação cara, com expectativas de crescimento elevadas. Risco
                    de correção em setores como tecnologia (ex.: TOTS3).
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            else:  # pebit > 20
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'P/EBIT > 20',
                    'descricao': '''
                    P/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas
                    especulativas (ex.: startups listadas como NUBR33). Análise detalhada do crescimento
                    é essencial.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Erro ao processar P/EBIT: {str(e)}. Verifique se o valor fornecido é um número válido
                e se o EBIT por ação não é zero.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: EV/EBITDA.
"""


def evaluate_evebitda(evebitda):
    '''
    Avalia o EV/EBITDA com base em faixas definidas para o mercado brasileiro:
    - EV/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ EV/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < EV/EBITDA ≤ 7: Moderado (valuation justo, crescimento moderado)
    - 7 < EV/EBITDA ≤ 10: Ruim (sobrevalorizado, cautela necessária)
    - 10 < EV/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - EV/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    Indicador que relaciona o valor da empresa (valor de mercado + dívida líquida) ao EBITDA,
    avaliando a capacidade de geração de caixa em relação ao valor total da companhia. É útil
    para comparar empresas com diferentes estruturas de capital.
    '''
    agrupador = 'Valuation'
    formula = 'EV/EBITDA = (Valor de Mercado + Dívida Líquida) / EBITDA'

    try:
        if evebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'EV/EBITDA < 0',
                'descricao': '''
                EV/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais graves.
                Comum em empresas em crise ou setores cíclicos (ex.: mineração como CSNA3). Exige
                análise de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= evebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= EV/EBITDA <= 4',
                'descricao': '''
                EV/EBITDA baixo sugere subvalorização, indicando oportunidade de compra. Comum em
                setores com ativos pesados (ex.: mineração como VALE3). Confirme com análise de
                endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < evebitda <= 7:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < EV/EBITDA <= 7',
                'descricao': '''
                EV/EBITDA indica valuation justo, típico de empresas com geração de caixa estável
                (ex.: utilities como ELET3). Equilíbrio entre risco e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 7 < evebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '7 < EV/EBITDA <= 10',
                'descricao': '''
                EV/EBITDA elevado sugere sobrevalorização moderada, comum em setores de crescimento
                (ex.: consumo como ABEV3). Exige análise de crescimento futuro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < evebitda <= 15:
            return {
                'classificacao': 'Péssimo',
                'faixa': '10 < EV/EBITDA <= 15',
                'descricao': '''
                EV/EBITDA muito alto indica empresa cara, com expectativas de crescimento elevadas.
                Risco de correção em setores como tecnologia (ex.: TOTS3).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # evebitda > 15
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBITDA > 15',
                'descricao': '''
                EV/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas (ex.: startups como NUBR33). Análise detalhada é essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar EV/EBITDA: {str(e)}. Verifique se o valor fornecido é um número
            válido e se o EBITDA não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Patrimônio Líquido/Ativos.
"""


def evaluate_pl_ativos(pl_ativos):
    '''
    Avalia o Patrimônio Líquido/Ativos com base em faixas definidas:
    - PL/Ativos < 0: Crítico (patrimônio negativo, risco elevado)
    - 0 ≤ PL/Ativos ≤ 0.1: Péssimo (alta alavancagem)
    - 0.1 < PL/Ativos ≤ 0.3: Ruim (alavancagem moderada)
    - 0.3 < PL/Ativos ≤ 0.5: Moderado (estrutura equilibrada)
    - 0.5 < PL/Ativos ≤ 0.7: Ótimo (patrimônio sólido)
    - PL/Ativos > 0.7: Fora da faixa (pouco endividamento)
    '''
    definicao = '''
    Indicador que mede a proporção do patrimônio líquido em relação aos ativos totais, avaliando
    o grau de alavancagem financeira da empresa. Um valor alto indica baixa dependência de dívidas,
    enquanto um valor baixo sugere maior alavancagem.
    '''
    agrupador = 'Estrutura de Capital'
    formula = 'PL/Ativos = Patrimônio Líquido / Ativos Totais'

    try:
        if pl_ativos < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'PL/Ativos < 0',
                'descricao': '''
                PL/Ativos negativo indica patrimônio líquido negativo, sugerindo insolvência. Comum
                em empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave,
                exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pl_ativos <= 0.1:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= PL/Ativos <= 0.1',
                'descricao': '''
                PL/Ativos muito baixo sugere alta alavancagem, comum em bancos (ex.: Itaú - ITUB4).
                Risco financeiro elevado, requerendo atenção ao fluxo de caixa e endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.1 < pl_ativos <= 0.3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.1 < PL/Ativos <= 0.3',
                'descricao': '''
                PL/Ativos baixo indica alavancagem moderada, comum em utilities (ex.: Engie Brasil - EGIE3).
                Exige monitoramento da capacidade de pagamento de dívidas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < pl_ativos <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < PL/Ativos <= 0.5',
                'descricao': '''
                PL/Ativos equilibrado sugere estrutura financeira saudável, comum em indústrias
                (ex.: Suzano - SUZB3). Para investidores, indica equilíbrio entre risco e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < pl_ativos <= 0.7:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0.5 < PL/Ativos <= 0.7',
                'descricao': '''
                PL/Ativos alto indica patrimônio sólido, comum em consumo (ex.: Ambev - ABEV3).
                Sinal de baixa alavancagem, atrativo para investidores conservadores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pl_ativos > 0.7
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL/Ativos > 0.7',
                'descricao': '''
                PL/Ativos extremamente alto sugere pouco endividamento, comum em tecnologia
                (ex.: Totvs - TOTS3). Pode indicar subvalorização, mas exige análise de eficiência
                no uso de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar PL/Ativos: {str(e)}. Verifique se o valor fornecido é um número
            válido e se os ativos totais não são zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: PEG Ratio, Preço/Ativo Total.
"""


def evaluate_peg_ratio(peg):
    '''
    Avalia o PEG Ratio com base em faixas definidas:
    - PEG < 0: Crítico (crescimento negativo, risco elevado)
    - 0 ≤ PEG ≤ 0.5: Ótimo (subvalorizado com alto crescimento)
    - 0.5 < PEG ≤ 1: Moderado (valuation justo)
    - 1 < PEG ≤ 1.5: Ruim (sobrevalorizado, cautela necessária)
    - 1.5 < PEG ≤ 2: Péssimo (muito caro, alto risco)
    - PEG > 2: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que relaciona o P/L com a taxa de crescimento esperada dos lucros, avaliando se
    o preço da ação é justificado pelo seu potencial de crescimento. Um PEG baixo sugere
    subvalorização em relação ao crescimento esperado.
    '''
    agrupador = 'Valuation'
    formula = 'PEG = (Preço/Lucro) / Crescimento Anual Esperado do Lucro (%)'

    try:
        if peg < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'PEG < 0',
                'descricao': '''
                PEG negativo indica crescimento esperado negativo ou P/L negativo, sugerindo
                problemas financeiros ou de mercado. Comum em empresas em crise (ex.: Oi - OIBR3).
                Para investidores, é um alerta grave, exigindo análise detalhada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= peg <= 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= PEG <= 0.5',
                'descricao': '''
                PEG baixo sugere subvalorização com alto potencial de crescimento, comum em
                tecnologia (ex.: Totvs - TOTS3). Oportunidade de compra para investidores focados
                em crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < peg <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < PEG <= 1',
                'descricao': '''
                PEG indica valuation justo, equilibrando preço e crescimento, comum em varejo
                (ex.: Magazine Luiza - MGLU3). Para investidores, sugere equilíbrio entre risco
                e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < peg <= 1.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < PEG <= 1.5',
                'descricao': '''
                PEG elevado sugere sobrevalorização moderada, indicando expectativas de crescimento
                moderadas. Comum em setores competitivos (ex.: consumo como LREN3). Exige análise
                de perspectivas futuras.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < peg <= 2:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1.5 < PEG <= 2',
                'descricao': '''
                PEG muito alto indica ação cara em relação ao crescimento, comum em setores
                especulativos (ex.: tecnologia como NUBR33). Risco de correção elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # peg > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PEG > 2',
                'descricao': '''
                PEG extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas (ex.: startups como NUBR33). Análise detalhada do crescimento é
                essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar PEG Ratio: {str(e)}. Verifique se o valor fornecido é um número
            válido e se o crescimento anual esperado do lucro não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_p_ativo(p_ativo):
    '''
    Avalia o Preço/Ativo Total com base em faixas definidas:
    - P/Ativo < 0: Crítico (impossível)
    - 0 ≤ P/Ativo ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/Ativo ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/Ativo ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/Ativo ≤ 1.5: Péssimo (muito caro)
    - P/Ativo > 1.5: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que compara o preço da ação com os ativos totais por ação, avaliando se a empresa
    está sendo negociada acima ou abaixo do valor de seus ativos. É útil para identificar
    subvalorização em empresas com muitos ativos.
    '''
    agrupador = 'Valuation'
    formula = 'P/Ativo = Preço da Ação / Ativos Totais por Ação'

    try:
        if p_ativo < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/Ativo < 0',
                'descricao': '''
                P/Ativo negativo é impossível, indicando erro nos dados financeiros ou cálculo
                incorreto. Verifique os dados de preço da ação e ativos totais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_ativo <= 0.2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/Ativo <= 0.2',
                'descricao': '''
                P/Ativo baixo sugere subvalorização, comum em mineração (ex.: Vale - VALE3).
                Oportunidade de compra para investidores focados em valor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < p_ativo <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/Ativo <= 0.5',
                'descricao': '''
                P/Ativo indica valuation justo, típico de energia (ex.: Eletrobras - ELET3).
                Equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < p_ativo <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/Ativo <= 1',
                'descricao': '''
                P/Ativo elevado sugere sobrevalorização, comum em consumo (ex.: Ambev - ABEV3).
                Exige análise detalhada do valor dos ativos e perspectivas de crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_ativo <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < P/Ativo <= 1.5',
                'descricao': '''
                P/Ativo muito alto indica ação cara, comum em tecnologia (ex.: Totvs - TOTS3).
                Risco de correção elevado, exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # p_ativo > 1.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/Ativo > 1.5',
                'descricao': '''
                P/Ativo extremamente elevado sugere sobrevalorização severa, indicando alto risco.
                Típico de empresas especulativas (ex.: Nubank - NUBR33). Análise detalhada é
                essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/Ativo: {str(e)}. Verifique se o valor fornecido é um número
            válido e se os ativos totais por ação não são zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: VPA/Preço.
"""


def evaluate_vpa(vpa_preco):
    '''
    Avalia o VPA/Preço com base em faixas definidas:
    - VPA/Preço < 0: Crítico (patrimônio negativo)
    - 0 ≤ VPA/Preço ≤ 0.5: Fora da faixa (sobrevalorizado)
    - 0.5 < VPA/Preço ≤ 0.8: Péssimo (muito caro)
    - 0.8 < VPA/Preço ≤ 1: Ruim (sobrevalorizado)
    - 1 < VPA/Preço ≤ 1.5: Moderado (valuation justo)
    - VPA/Preço > 1.5: Ótimo (subvalorizado)
    '''
    definicao = '''
    Indicador que compara o valor patrimonial por ação com o preço da ação, avaliando se a
    empresa está subvalorizada ou sobrevalorizada em relação ao seu patrimônio líquido. Um valor
    alto sugere subvalorização.
    '''
    agrupador = 'Valuation'
    formula = 'VPA/Preço = Valor Patrimonial por Ação / Preço da Ação'

    try:
        if vpa_preco < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'VPA/Preço < 0',
                'descricao': '''
                VPA/Preço negativo indica patrimônio líquido negativo, sugerindo insolvência.
                Comum em empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave,
                exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= vpa_preco <= 0.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': '0 <= VPA/Preço <= 0.5',
                'descricao': '''
                VPA/Preço muito baixo indica sobrevalorização severa, comum em tecnologia
                (ex.: Totvs - TOTS3). Para investidores, sugere risco elevado de correção.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < vpa_preco <= 0.8:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0.5 < VPA/Preço <= 0.8',
                'descricao': '''
                VPA/Preço baixo sugere ação cara, comum em varejo (ex.: Magazine Luiza - MGLU3).
                Exige cautela e análise de outros indicadores de valuation.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < vpa_preco <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.8 < VPA/Preço <= 1',
                'descricao': '''
                VPA/Preço indica sobrevalorização moderada, comum em consumo (ex.: Ambev - ABEV3).
                Para investidores, sugere necessidade de análise de crescimento e rentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < vpa_preco <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < VPA/Preço <= 1.5',
                'descricao': '''
                VPA/Preço indica valuation justo, típico de indústrias (ex.: Suzano - SUZB3).
                Equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # vpa_preco > 1.5
            return {
                'classificacao': 'Ótimo',
                'faixa': 'VPA/Preço > 1.5',
                'descricao': '''
                VPA/Preço alto sugere subvalorização, comum em setores maduros (ex.: bancos como
                Bradesco - BBDC4). Oportunidade de compra para investidores focados em valor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar VPA/Preço: {str(e)}. Verifique se o valor fornecido é um número
            válido e se o preço da ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula

        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Lucro por Ação (LPA).
"""


def evaluate_lpa(lpa):
    '''
    Avalia o Lucro por Ação (LPA) com base em faixas definidas:
    - LPA < 0: Crítico (prejuízo)
    - 0 ≤ LPA ≤ 0.2: Péssimo (lucro muito baixo)
    - 0.2 < LPA ≤ 0.5: Ruim (lucro limitado)
    - 0.5 < LPA ≤ 1: Moderado (lucro adequado)
    - 1 < LPA ≤ 2: Ótimo (lucro alto)
    - LPA > 2: Fora da faixa (lucro excepcional)
    '''
    definicao = '''
    Indicador que mede o lucro líquido por ação, refletindo a lucratividade da empresa por ação
    emitida. É útil para avaliar a capacidade da empresa de gerar retorno aos acionistas.
    '''
    agrupador = 'Lucratividade'
    formula = 'LPA = Lucro Líquido / Número de Ações'

    try:
        if lpa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'LPA < 0',
                'descricao': '''
                LPA negativo indica prejuízo por ação, sugerindo problemas financeiros. Comum em
                empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave, exigindo
                análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= lpa <= 0.2:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= LPA <= 0.2',
                'descricao': '''
                LPA muito baixo sugere lucratividade insuficiente, comum em empresas em crise ou com
                margens apertadas (ex.: varejo como PCAR3). Para investidores, indica alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < lpa <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < LPA <= 0.5',
                'descricao': '''
                LPA limitado indica lucratividade moderada, comum em setores cíclicos (ex.: Gerdau - GGBR4).
                Para investidores, sugere necessidade de monitoramento de tendências de lucro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < lpa <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < LPA <= 1',
                'descricao': '''
                LPA adequado sugere lucratividade equilibrada, comum em consumo (ex.: Ambev - ABEV3).
                Para investidores, indica equilíbrio entre risco e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < lpa <= 2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < LPA <= 2',
                'descricao': '''
                LPA alto indica forte lucratividade, comum em tecnologia (ex.: Totvs - TOTS3).
                Oportunidade atrativa para investidores focados em crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # lpa > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'LPA > 2',
                'descricao': '''
                LPA extremamente alto sugere lucratividade excepcional, comum em empresas líderes
                (ex.: Vale - VALE3). Para investidores, é atrativo, mas exige análise de
                sustentabilidade dos lucros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar LPA: {str(e)}. Verifique se o valor fornecido é um número válido
            e se o número de ações não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Passivos/Ativos.
"""


def evaluate_passivos_ativos(passivos_ativos):
    '''
    Avalia o Passivos/Ativos com base em faixas definidas:
    - Passivos/Ativos < 0: Crítico (impossível)
    - 0 ≤ Passivos/Ativos ≤ 0.3: Ótimo (baixo endividamento)
    - 0.3 < Passivos/Ativos ≤ 0.5: Moderado (endividamento controlado)
    - 0.5 < Passivos/Ativos ≤ 0.7: Ruim (endividamento moderado)
    - 0.7 < Passivos/Ativos ≤ 0.9: Péssimo (endividamento alto)
    - Passivos/Ativos > 0.9: Fora da faixa (endividamento excessivo)
    '''
    definicao = '''
    Indicador que mede a proporção dos passivos totais em relação aos ativos totais, avaliando
    o nível de endividamento da empresa. Um valor alto indica maior dependência de dívidas,
    enquanto um valor baixo sugere maior solidez financeira.
    '''
    agrupador = 'Endividamento'
    formula = 'Passivos/Ativos = Passivos Totais / Ativos Totais'

    try:
        if passivos_ativos < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Passivos/Ativos < 0',
                'descricao': '''
                Passivos/Ativos negativo é impossível, indicando erro nos dados financeiros ou
                cálculo incorreto. Verifique os dados de passivos e ativos totais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= passivos_ativos <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Passivos/Ativos <= 0.3',
                'descricao': '''
                Passivos/Ativos baixo indica baixo endividamento, comum em tecnologia
                (ex.: Totvs - TOTS3). Sinal de saúde financeira, atrativo para investidores
                conservadores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < passivos_ativos <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < Passivos/Ativos <= 0.5',
                'descricao': '''
                Passivos/Ativos moderado sugere endividamento controlado, comum em consumo
                (ex.: Ambev - ABEV3). Para investidores, indica equilíbrio entre risco e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < passivos_ativos <= 0.7:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < Passivos/Ativos <= 0.7',
                'descricao': '''
                Passivos/Ativos elevado indica endividamento moderado, comum em indústrias
                (ex.: Suzano - SUZB3). Exige monitoramento da capacidade de pagamento de dívidas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.7 < passivos_ativos <= 0.9:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0.7 < Passivos/Ativos <= 0.9',
                'descricao': '''
                Passivos/Ativos alto sugere endividamento elevado, comum em utilities
                (ex.: Engie Brasil - EGIE3). Risco financeiro elevado, requer atenção ao fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # passivos_ativos > 0.9
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Passivos/Ativos > 0.9',
                'descricao': '''
                Passivos/Ativos extremamente alto indica endividamento excessivo, comum em bancos
                (ex.: Itaú - ITUB4). Alto risco para investidores, exige análise detalhada de solvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Passivos/Ativos: {str(e)}. Verifique se o valor fornecido é um número
            válido e se os ativos totais não são zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Preço/Receita (P/SR).
"""


def evaluate_psr(psr):
    '''
    Avalia o Preço/Receita (P/SR) com base em faixas definidas:
    - P/SR < 0: Crítico (receita negativa)
    - 0 ≤ P/SR ≤ 0.3: Ótimo (subvalorizado)
    - 0.3 < P/SR ≤ 0.8: Moderado (valuation justo)
    - 0.8 < P/SR ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < P/SR ≤ 2.5: Péssimo (muito caro)
    - P/SR > 2.5: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que relaciona o preço da ação à receita líquida por ação, avaliando o valor de
    mercado em relação às vendas. É útil para empresas com lucros baixos ou negativos.
    '''
    agrupador = 'Valuation'
    formula = 'P/SR = Preço da Ação / Receita Líquida por Ação'

    try:
        if psr < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/SR < 0',
                'descricao': '''
                P/SR negativo indica receita negativa, sugerindo graves problemas operacionais.
                Comum em empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave,
                exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= psr <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/SR <= 0.3',
                'descricao': '''
                P/SR baixo sugere subvalorização, comum em mineração (ex.: Vale - VALE3).
                Oportunidade de compra para investidores focados em valor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < psr <= 0.8:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < P/SR <= 0.8',
                'descricao': '''
                P/SR indica valuation justo, típico de energia (ex.: Eletrobras - ELET3).
                Equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < psr <= 1.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.8 < P/SR <= 1.5',
                'descricao': '''
                P/SR elevado sugere sobrevalorização, comum em consumo (ex.: Ambev - ABEV3).
                Exige análise detalhada de margens e crescimento de receita.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < psr <= 2.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1.5 < P/SR <= 2.5',
                'descricao': '''
                P/SR muito alto indica ação cara, comum em tecnologia (ex.: Totvs - TOTS3).
                Risco de correção elevado, exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # psr > 2.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/SR > 2.5',
                'descricao': '''
                P/SR extremamente elevado sugere sobrevalorização severa, indicando alto risco.
                Típico de empresas especulativas (ex.: Nubank - NUBR33). Análise detalhada é
                essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/SR: {str(e)}. Verifique se o valor fornecido é um número válido
            e se a receita líquida por ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Preço/Ativo Circulante Líquido (P/ACL).
"""


def evaluate_p_ativo_circ_liq(p_acl):
    '''
    Avalia o Preço/Ativo Circulante Líquido com base em faixas definidas:
    - P/ACL < 0: Crítico (ativo circulante líquido negativo)
    - 0 ≤ P/ACL ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/ACL ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/ACL ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/ACL ≤ 1.5: Péssimo (muito caro)
    - P/ACL > 1.5: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que compara o preço da ação com o ativo circulante líquido por ação (ativo circulante
    menos passivo circulante), avaliando a liquidez imediata da empresa em relação ao seu valor
    de mercado.
    '''
    agrupador = 'Valuation'
    formula = 'P/ACL = Preço da Ação / (Ativo Circulante - Passivo Circulante) por Ação'

    try:
        if p_acl < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/ACL < 0',
                'descricao': '''
                P/ACL negativo indica ativo circulante líquido negativo, sugerindo problemas de
                liquidez ou passivo circulante maior que ativo circulante (ex.: Oi - OIBR3). Para
                investidores, é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_acl <= 0.2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/ACL <= 0.2',
                'descricao': '''
                P/ACL baixo sugere subvalorização em relação à liquidez, comum em mineração
                (ex.: Vale - VALE3). Oportunidade de compra, especialmente em setores com ativos
                circulantes robustos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < p_acl <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/ACL <= 0.5',
                'descricao': '''
                P/ACL indica valuation justo, comum em energia (ex.: Eletrobras - ELET3).
                Oferece equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < p_acl <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/ACL <= 1',
                'descricao': '''
                P/ACL elevado sugere sobrevalorização, comum em consumo (ex.: Ambev - ABEV3).
                Exige análise detalhada de liquidez e endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_acl <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < P/ACL <= 1.5',
                'descricao': '''
                P/ACL muito alto indica ação cara, comum em tecnologia (ex.: Totvs - TOTS3).
                Risco de correção elevado devido a expectativas de mercado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # p_acl > 1.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/ACL > 1.5',
                'descricao': '''
                P/ACL extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas ou com baixa liquidez relativa (ex.: Weg - WEGE3). Análise detalhada
                é essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/ACL: {str(e)}. Verifique se o valor fornecido é um número válido
            e se o ativo circulante líquido por ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Disponibilidade (Caixa e Equivalentes).
"""


def evaluate_disponibilidade(disponibilidade):
    '''
    Avalia a Disponibilidade (caixa e equivalentes, em R$ bilhões):
    - Disponibilidade < 0: Crítico
    - 0 ≤ Disponibilidade ≤ 0.05: Péssimo
    - 0.05 < Disponibilidade ≤ 0.2: Ruim
    - 0.2 < Disponibilidade ≤ 1: Moderado
    - 1 < Disponibilidade ≤ 10: Ótimo
    - Disponibilidade > 10: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o caixa e equivalentes de caixa da empresa, refletindo a liquidez
    imediata disponível para cobrir obrigações ou investir.
    '''
    agrupador = 'Liquidez'
    formula = 'Disponibilidade = Caixa + Equivalentes de Caixa'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(disponibilidade, str):
            # Remove "R$" e espaços
            disponibilidade = disponibilidade.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            disponibilidade = disponibilidade.replace('.', '').replace(',', '.')
            disponibilidade = float(disponibilidade) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            disponibilidade = float(disponibilidade) / 1_000_000_000 if disponibilidade >= 1_000_000 else float(
                disponibilidade)

        if disponibilidade < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Disponibilidade < 0',
                'descricao': '''
                Disponibilidade negativa é impossível, indicando erro nos dados financeiros ou
                cálculo incorreto. Verifique os dados de caixa e equivalentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= disponibilidade <= 0.05:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= Disponibilidade <= 0.05',
                'descricao': '''
                Caixa muito baixo indica alto risco de liquidez, comum em empresas em crise
                (ex.: Oi - OIBR3). Para investidores, sugere dificuldades em cumprir obrigações
                de curto prazo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.05 < disponibilidade <= 0.2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.05 < Disponibilidade <= 0.2',
                'descricao': '''
                Caixa limitado indica liquidez restrita, comum em small caps (ex.: Enauta - ENAT3).
                Exige monitoramento da gestão de caixa para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < disponibilidade <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < Disponibilidade <= 1',
                'descricao': '''
                Caixa adequado sugere liquidez equilibrada, típico de mid caps (ex.: Ambev - ABEV3).
                Oferece segurança moderada para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < disponibilidade <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Disponibilidade <= 10',
                'descricao': '''
                Caixa robusto indica forte liquidez, comum em large caps (ex.: Itaú - ITUB4).
                Atraente para investidores que priorizam segurança financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # disponibilidade > 10
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Disponibilidade > 10',
                'descricao': '''
                Caixa excepcional sugere liquidez extremamente alta, típico de blue chips
                (ex.: Vale - VALE3). Para investidores, indica forte capacidade de investimento ou
                distribuição de dividendos, mas exige análise de eficiência no uso do caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Disponibilidade: {str(e)}. Verifique se o valor é um número válido
            ou está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Preço/Lucro (P/L).
"""


def evaluate_pl(pl):
    '''
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (prejuízo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo, crescimento moderado)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 30: Péssimo (muito caro, alto risco)
    - P/L > 30: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    Indicador que relaciona o preço da ação ao lucro por ação, medindo quantos anos seriam
    necessários para recuperar o investimento com base nos lucros atuais. É amplamente usado
    para avaliar se uma ação está cara ou barata em relação aos lucros gerados.
    '''
    agrupador = 'Valuation'
    formula = 'P/L = Preço da Ação / Lucro por Ação'

    try:
        if pl < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/L < 0',
                'descricao': '''
                P/L negativo indica que a empresa está com prejuízo, sugerindo riscos como problemas
                operacionais, má gestão ou dificuldades de mercado. Comum em setores cíclicos
                (ex.: CSN - CSNA3). Exige análise de fundamentos como EBITDA e fluxo de caixa para
                avaliar recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pl <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/L <= 10',
                'descricao': '''
                P/L baixo sugere que a ação está subvalorizada ou que o mercado tem perspectiva
                negativa sobre o futuro da empresa. Comum em setores maduros (ex.: bancos como
                Itaú - ITUB4 ou utilities como Engie Brasil - EGIE3). Pode representar uma
                oportunidade de valor se o mercado estiver subestimando o potencial de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pl <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '10 < P/L <= 15',
                'descricao': '''
                P/L indica valuation justo, típico de empresas com crescimento estável e fundamentos
                sólidos. Comum em setores consolidados com margens previsíveis (ex.: varejo como
                Lojas Renner - LREN3 ou energia como Eletrobras - ELET3). Oferece equilíbrio entre
                risco e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < pl <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < P/L <= 20',
                'descricao': '''
                P/L elevado sugere sobrevalorização moderada, indicando que o mercado espera
                crescimento, mas com riscos crescentes. Comum em setores dinâmicos (ex.: varejo
                tech como Magazine Luiza - MGLU3). Exige análise de perspectivas de lucro e
                comparação com pares do setor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < pl <= 30:
            return {
                'classificacao': 'Péssimo',
                'faixa': '20 < P/L <= 30',
                'descricao': '''
                P/L muito alto indica que a ação está cara, com expectativas de crescimento elevadas
                que podem não se concretizar. Comum em setores de alto crescimento (ex.: tecnologia
                como Totvs - TOTS3). Risco significativo de correção se os resultados desapontarem.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pl > 30
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/L > 30',
                'descricao': '''
                P/L extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas ou em bolhas de mercado. Comum em setores de crescimento excepcional
                (ex.: tecnologia como Nubank - NUBR33). O risco de correção é alto, exigindo análise
                detalhada do crescimento futuro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/L: {str(e)}. Verifique se o valor fornecido é um número válido
            e se o lucro por ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Patrimônio Líquido.
"""


def evaluate_patrimonio_liquido(pl):
    '''
    Avalia o Patrimônio Líquido (em R$ bilhões):
    - PL < 0: Crítico
    - 0 ≤ PL ≤ 0.5: Péssimo
    - 0.5 < PL ≤ 2: Ruim
    - 2 < PL ≤ 10: Moderado
    - 10 < PL ≤ 50: Ótimo
    - PL > 50: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o valor contábil da empresa pertencente aos acionistas, calculado
    como ativos totais menos passivos totais. Valores altos indicam maior solidez financeira.
    '''
    agrupador = 'Estrutura de Capital'
    formula = 'PL = Ativos Totais - Passivos Totais'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(pl, str):
            # Remove "R$" e espaços
            pl = pl.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            pl = pl.replace('.', '').replace(',', '.')
            pl = float(pl) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            pl = float(pl) / 1_000_000_000 if pl >= 1_000_000 else float(pl)

        if pl < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'PL < 0',
                'descricao': '''
                Patrimônio líquido negativo indica que os passivos superam os ativos, sugerindo
                alto risco financeiro. Comum em empresas em crise (ex.: Oi - OIBR3). Para
                investidores, é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pl <= 0.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= PL <= 0.5',
                'descricao': '''
                Patrimônio muito baixo indica fragilidade financeira, típico de small caps
                (ex.: Enauta - ENAT3). Para investidores, sugere alto risco e necessidade de
                monitoramento de endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < pl <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < PL <= 2',
                'descricao': '''
                Patrimônio limitado sugere estrutura financeira modesta, comum em empresas menores
                (ex.: Cyrela - CYRE3). Para investidores, indica necessidade de avaliar crescimento
                e solvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < pl <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '2 < PL <= 10',
                'descricao': '''
                Patrimônio sólido indica estrutura financeira equilibrada, típico de mid caps
                (ex.: Ambev - ABEV3). Oferece segurança moderada para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pl <= 50:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10 < PL <= 50',
                'descricao': '''
                Patrimônio robusto sugere forte solidez financeira, comum em large caps
                (ex.: Itaú - ITUB4). Atraente para investidores que priorizam estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pl > 50
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL > 50',
                'descricao': '''
                Patrimônio excepcional indica altíssima solidez financeira, típico de blue chips
                (ex.: Vale - VALE3). Para investidores, sugere forte capacidade de resistência a
                crises, mas exige análise de eficiência no uso do capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Patrimônio Líquido: {str(e)}. Verifique se o valor é um número
            válido ou está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Dívida Bruta.
"""


def evaluate_divida_bruta(divida_bruta):
    '''
    Avalia a Dívida Bruta (em R$ bilhões):
    - Dívida Bruta < 0: Crítico
    - 0 ≤ Dívida Bruta ≤ 0.5: Ótimo
    - 0.5 < Dívida Bruta ≤ 2: Moderado
    - 2 < Dívida Bruta ≤ 10: Ruim
    - 10 < Dívida Bruta ≤ 20: Péssimo
    - Dívida Bruta > 20: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o total de obrigações financeiras da empresa, incluindo empréstimos
    e financiamentos de curto e longo prazo.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Bruta = Total de Empréstimos e Financiamentos'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(divida_bruta, str):
            # Remove "R$" e espaços
            divida_bruta = divida_bruta.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            divida_bruta = divida_bruta.replace('.', '').replace(',', '.')
            divida_bruta = float(divida_bruta) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            divida_bruta = float(divida_bruta) / 1_000_000_000 if divida_bruta >= 1_000_000 else float(divida_bruta)

        if divida_bruta < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Bruta < 0',
                'descricao': '''
                Dívida bruta negativa é impossível, indicando erro nos dados financeiros ou cálculo
                incorreto. Verifique os dados de empréstimos e financiamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_bruta <= 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Bruta <= 0.5',
                'descricao': '''
                Dívida bruta muito baixa indica baixo risco financeiro, comum em empresas com pouca
                alavancagem (ex.: Totvs - TOTS3). Atraente para investidores que priorizam segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < divida_bruta <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Dívida Bruta <= 2',
                'descricao': '''
                Dívida bruta controlada sugere equilíbrio financeiro, típico de mid caps
                (ex.: Ambev - ABEV3). Oferece risco moderado para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_bruta <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Bruta <= 10',
                'descricao': '''
                Dívida bruta moderada indica maior dependência de financiamentos, comum em indústrias
                (ex.: Suzano - SUZB3). Exige atenção à capacidade de pagamento para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < divida_bruta <= 20:
            return {
                'classificacao': 'Péssimo',
                'faixa': '10 < Dívida Bruta <= 20',
                'descricao': '''
                Dívida bruta alta sugere risco financeiro elevado, comum em utilities
                (ex.: Engie Brasil - EGIE3). Para investidores, requer análise detalhada de fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # divida_bruta > 20
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Bruta > 20',
                'descricao': '''
                Dívida bruta excessiva indica alta alavancagem, típico de empresas intensivas em
                capital (ex.: Vale - VALE3). Para investidores, é de alto risco, exigindo análise
                da sustentabilidade da dívida.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Dívida Bruta: {str(e)}. Verifique se o valor é um número válido ou
            está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Dívida Líquida.
"""


def evaluate_divida_liquida(divida_liquida):
    '''
    Avalia a Dívida Líquida (em R$ bilhões):
    - Dívida Líquida ≤ -0.5: Ótimo
    - -0.5 < Dívida Líquida ≤ 0: Moderado
    - 0 < Dívida Líquida ≤ 2: Ruim
    - 2 < Dívida Líquida ≤ 10: Péssimo
    - Dívida Líquida > 10: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa a dívida bruta da empresa menos seu caixa e equivalentes, refletindo
    o endividamento real. Valores negativos indicam mais caixa que dívidas.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida = Dívida Bruta - Caixa e Equivalentes'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(divida_liquida, str):
            # Remove "R$" e espaços
            divida_liquida = divida_liquida.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            divida_liquida = divida_liquida.replace('.', '').replace(',', '.')
            divida_liquida = float(divida_liquida) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            divida_liquida = float(divida_liquida) / 1_000_000_000 if abs(divida_liquida) >= 1_000_000 else float(
                divida_liquida)

        if divida_liquida <= -0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': 'Dívida Líquida <= -0.5',
                'descricao': '''
                Dívida líquida negativa (caixa líquido) indica excelente saúde financeira, com mais
                caixa que dívidas. Comum em empresas com baixa alavancagem (ex.: Totvs - TOTS3).
                Atraente para investidores que priorizam segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif -0.5 < divida_liquida <= 0:
            return {
                'classificacao': 'Moderado',
                'faixa': '-0.5 < Dívida Líquida <= 0',
                'descricao': '''
                Dívida líquida próxima de zero sugere situação financeira equilibrada, com dívidas
                compensadas pelo caixa. Comum em empresas estáveis (ex.: Ambev - ABEV3). Oferece
                risco moderado para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 < divida_liquida <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0 < Dívida Líquida <= 2',
                'descricao': '''
                Dívida líquida moderada indica dependência de financiamentos, exigindo atenção.
                Comum em empresas de porte médio (ex.: Cyrela - CYRE3). Para investidores, sugere
                análise da capacidade de geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_liquida <= 10:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < Dívida Líquida <= 10',
                'descricao': '''
                Dívida líquida alta reflete risco financeiro elevado, comum em indústrias intensivas
                em capital (ex.: Suzano - SUZB3). Para investidores, exige cautela e análise detalhada
                de fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # divida_liquida > 10
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida > 10',
                'descricao': '''
                Dívida líquida excessiva indica alto risco financeiro, típico de empresas altamente
                alavancadas (ex.: Vale - VALE3). Para investidores, é essencial avaliar a
                sustentabilidade da dívida e a geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Dívida Líquida: {str(e)}. Verifique se o valor é um número válido
            ou está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicador incluído: Ativos Totais.
"""


def evaluate_ativos(ativos):
    '''
    Avalia os Ativos Totais (em R$ bilhões):
    - Ativos < 0: Crítico
    - 0 ≤ Ativos ≤ 1: Péssimo
    - 1 < Ativos ≤ 5: Ruim
    - 5 < Ativos ≤ 20: Moderado
    - 20 < Ativos ≤ 100: Ótimo
    - Ativos > 100: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o total de ativos da empresa, incluindo circulantes e não circulantes.
    Valores altos indicam maior porte e capacidade de investimento.
    '''
    agrupador = 'Estrutura de Capital'
    formula = 'Ativos = Ativo Circulante + Ativo Não Circulante'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(ativos, str):
            # Remove "R$" e espaços
            ativos = ativos.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            ativos = ativos.replace('.', '').replace(',', '.')
            ativos = float(ativos) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            ativos = float(ativos) / 1_000_000_000 if ativos >= 1_000_000 else float(ativos)

        if ativos < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Ativos < 0',
                'descricao': '''
                Ativos negativos são impossíveis, indicando erro nos dados financeiros ou cálculo
                incorreto. Verifique os dados de ativos circulantes e não circulantes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ativos <= 1:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= Ativos <= 1',
                'descricao': '''
                Ativos muito baixos indicam porte financeiro limitado, típico de small caps
                (ex.: Enauta - ENAT3). Para investidores, sugere alto risco e baixa capacidade de
                investimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < ativos <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < Ativos <= 5',
                'descricao': '''
                Ativos limitados sugerem estrutura financeira modesta, comum em empresas menores
                (ex.: Cyrela - CYRE3). Para investidores, indica necessidade de avaliar crescimento
                e solvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ativos <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < Ativos <= 20',
                'descricao': '''
                Ativos sólidos indicam estrutura financeira equilibrada, típico de mid caps
                (ex.: Ambev - ABEV3). Oferece segurança moderada para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < ativos <= 100:
            return {
                'classificacao': 'Ótimo',
                'faixa': '20 < Ativos <= 100',
                'descricao': '''
                Ativos robustos sugerem forte solidez financeira, comum em large caps
                (ex.: Itaú - ITUB4). Atraente para investidores que priorizam estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # ativos > 100
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Ativos > 100',
                'descricao': '''
                Ativos excepcionais indicam altíssimo porte financeiro, típico de blue chips
                (ex.: Vale - VALE3). Para investidores, sugere forte capacidade de investimento,
                mas exige análise de eficiência no uso do capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Ativos: {str(e)}. Verifique se o valor é um número válido ou
            está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }
    """
    analisefundamentalista_10.py
    Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
    e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
    Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
    Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
    Indicador incluído: Ativo Circulante.
    """

    def evaluate_ativo_circulante(ativo_circulante):
        '''
        Avalia o Ativo Circulante (em R$ bilhões):
        - Ativo Circulante < 0: Crítico
        - 0 ≤ Ativo Circulante ≤ 0.2: Péssimo
        - 0.2 < Ativo Circulante ≤ 1: Ruim
        - 1 < Ativo Circulante ≤ 5: Moderado
        - 5 < Ativo Circulante ≤ 20: Ótimo
        - Ativo Circulante > 20: Fora da faixa
        Aceita valores no formato R$ 112.714.000 (converte para bilhões).
        '''
        definicao = '''
        Indicador que representa os ativos de curto prazo da empresa, como caixa, contas a receber
        e estoques, disponíveis para cobrir obrigações de curto prazo.
        '''
        agrupador = 'Liquidez'
        formula = 'Ativo Circulante = Caixa + Contas a Receber + Estoques + Outros Ativos de Curto Prazo'

        try:
            # Se for string, processar formato monetário brasileiro
            if isinstance(ativo_circulante, str):
                # Remove "R$" e espaços
                ativo_circulante = ativo_circulante.replace('R$', '').replace(' ', '')
                # Substitui ponto (milhares) e vírgula (decimal)
                ativo_circulante = ativo_circulante.replace('.', '').replace(',', '.')
                ativo_circulante = float(ativo_circulante) / 1_000_000_000  # Converte para bilhões
            else:
                # Garante que é float
                ativo_circulante = float(ativo_circulante) / 1_000_000_000 if ativo_circulante >= 1_000_000 else float(
                    ativo_circulante)

            if ativo_circulante < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Ativo Circulante < 0',
                    'descricao': '''
                    Ativo circulante negativo é impossível, indicando erro nos dados financeiros ou
                    cálculo incorreto. Verifique os dados de caixa, contas a receber e estoques.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= ativo_circulante <= 0.2:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '0 <= Ativo Circulante <= 0.2',
                    'descricao': '''
                    Ativo circulante muito baixo indica alto risco de liquidez, comum em empresas em
                    crise (ex.: Oi - OIBR3). Para investidores, sugere dificuldades em cumprir obrigações
                    de curto prazo.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.2 < ativo_circulante <= 1:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0.2 < Ativo Circulante <= 1',
                    'descricao': '''
                    Ativo circulante limitado sugere liquidez restrita, comum em small caps
                    (ex.: Enauta - ENAT3). Exige monitoramento da gestão de caixa para investidores.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 1 < ativo_circulante <= 5:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '1 < Ativo Circulante <= 5',
                    'descricao': '''
                    Ativo circulante adequado sugere liquidez equilibrada, típico de mid caps
                    (ex.: Ambev - ABEV3). Oferece segurança moderada para investidores.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < ativo_circulante <= 20:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '5 < Ativo Circulante <= 20',
                    'descricao': '''
                    Ativo circulante robusto indica forte liquidez, comum em large caps
                    (ex.: Itaú - ITUB4). Atraente para investidores que priorizam segurança financeira.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            else:  # ativo_circulante > 20
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Ativo Circulante > 20',
                    'descricao': '''
                    Ativo circulante excepcional sugere liquidez extremamente alta, típico de blue chips
                    (ex.: Vale - VALE3). Para investidores, indica forte capacidade de cumprir obrigações
                    de curto prazo, mas exige análise de eficiência no uso do capital.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Erro ao processar Ativo Circulante: {str(e)}. Verifique se o valor é um número válido
                ou está no formato correto (ex.: R$ 112.714.000).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
def evaluate_liquidez_media_diaria(liquidez):
    '''Avalia a Liquidez Média Diária (em R$ milhões):
    - Liquidez < 0: Crítico
    - 0 ≤ Liquidez ≤ 0.5: Péssimo
    - 0.5 < Liquidez ≤ 5: Ruim
    - 5 < Liquidez ≤ 20: Moderado
    - 20 < Liquidez ≤ 100: Ótimo
    - Liquidez > 100: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para milhões).'''
    definicao = '''Indicador que mede o volume médio diário de negociação da ação, refletindo a facilidade de compra e venda no mercado. Valores altos indicam maior liquidez e menor risco de negociação.'''
    agrupador = 'Liquidez'
    formula = 'Liquidez Média Diária = Volume Médio Diário de Negociação (em R$)'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(liquidez, str):
            # Remove "R$" e espaços
            liquidez = liquidez.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            liquidez = liquidez.replace('.', '').replace(',', '.')
            liquidez = float(liquidez) / 1_000_000  # Converte para milhões
        else:
            # Garante que é float
            liquidez = float(liquidez) / 1_000_000 if liquidez >= 1_000_000 else float(liquidez)

        if liquidez < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Liquidez < 0',
                'descricao': 'Liquidez média diária negativa, erro nos dados.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= liquidez <= 0.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Liquidez <= 0.5',
                'descricao': 'Liquidez muito baixa, ação ilíquida, risco elevado (ex.: small caps pouco negociadas).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < liquidez <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < Liquidez <= 5',
                'descricao': 'Liquidez limitada, comum em small caps (ex.: ENAT3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < liquidez <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < Liquidez <= 20',
                'descricao': 'Liquidez adequada, típica de mid caps (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < liquidez <= 100:
            return {
                'classificacao': 'Otimo',
                'faixa': '20 < Liquidez <= 100',
                'descricao': 'Liquidez robusta, comum em large caps (ex.: ITUB4).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez > 100',
                'descricao': 'Liquidez excepcional, típica de blue chips (ex.: VALE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Liquidez Média Diária: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }
def evaluate_ativo_circulante(ativo_circulante):
    '''Avalia o Ativo Circulante (em R$ bilhões):
    - Ativo Circulante < 0: Crítico
    - 0 ≤ Ativo Circulante ≤ 0.2: Péssimo
    - 0.2 < Ativo Circulante ≤ 1: Ruim
    - 1 < Ativo Circulante ≤ 5: Moderado
    - 5 < Ativo Circulante ≤ 20: Ótimo
    - Ativo Circulante > 20: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = '''Indicador que representa os ativos de curto prazo da empresa, como caixa, contas a receber e estoques, disponíveis para cobrir obrigações de curto prazo.'''
    agrupador = 'Liquidez'
    formula = 'Ativo Circulante = Caixa + Contas a Receber + Estoques + Outros Ativos de Curto Prazo'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(ativo_circulante, str):
            # Remove "R$" e espaços
            ativo_circulante = ativo_circulante.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            ativo_circulante = ativo_circulante.replace('.', '').replace(',', '.')
            ativo_circulante = float(ativo_circulante) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            ativo_circulante = float(ativo_circulante) / 1_000_000_000 if ativo_circulante >= 1_000_000 else float(ativo_circulante)

        if ativo_circulante < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Ativo Circulante < 0',
                'descricao': 'Ativo circulante negativo, erro nos dados.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ativo_circulante <= 0.2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Ativo Circulante <= 0.2',
                'descricao': 'Ativo circulante muito baixo, risco de liquidez (ex.: OI).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < ativo_circulante <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < Ativo Circulante <= 1',
                'descricao': 'Ativo circulante limitado, comum em small caps (ex.: ENAT3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < ativo_circulante <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Ativo Circulante <= 5',
                'descricao': 'Ativo circulante adequado, típico de mid caps (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ativo_circulante <= 20:
            return {
                'classificacao': 'Otimo',
                'faixa': '5 < Ativo Circulante <= 20',
                'descricao': 'Ativo circulante robusto, comum em large caps (ex.: ITUB4).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Ativo Circulante > 20',
                'descricao': 'Ativo circulante excepcional, típico de blue chips (ex.: VALE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Ativo Circulante: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }