# Define a classe LucroLiquidoEvaluator para avaliar o indicador Lucro Líquido
class LucroLiquidoEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do Lucro Líquido
    def __init__(self):
        # Define string multilinha explicando o índice Lucro Líquido
        self.definicao = '''
        O Lucro Líquido representa o resultado final da empresa após todas as receitas, custos, despesas, juros, impostos e outros ajustes,
        calculado como Receita Líquida menos todas as despesas (operacionais, financeiras e tributárias). É um indicador de lucratividade líquida
        que reflete a capacidade da empresa de gerar lucro para os acionistas. Valores altos sugerem eficiência e saúde financeira, enquanto valores
        baixos ou negativos indicam fragilidade ou ineficiência.
        '''
        # Define a categoria de agrupamento como "Lucratividade"
        self.agrupador = 'Lucratividade'
        # Define a fórmula do Lucro Líquido
        self.formula = 'Lucro Líquido = Receita Líquida - (Custos Operacionais + Despesas Operacionais + Juros + Impostos + Outros Ajustes)'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor do Lucro Líquido em relação à Receita Líquida e retorna um objeto ResultadoIND
    def avaliar(self, lucro_liquido, receita_liquida):
        # Tenta processar o valor do Lucro Líquido e Receita Líquida
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(lucro_liquido, "Lucro Líquido"), (receita_liquida, "Receita Líquida")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Lucro Líquido e Receita Líquida para float
            lucro_liquido = float(lucro_liquido)
            receita_liquida = float(receita_liquida)
            # Calcula a margem líquida (Lucro Líquido / Receita Líquida)
            if receita_liquida == 0:
                raise ValueError("A Receita Líquida não pode ser zero para calcular a margem líquida.")
            margem_liquida = lucro_liquido / receita_liquida
            # Verifica se Lucro Líquido é negativo, indicando prejuízo
            if margem_liquida < 0:
                # Retorna ResultadoIND para Lucro Líquido negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Lucro Líquido < 0',
                    descricao='Um Lucro Líquido negativo indica prejuízo, sugerindo que as despesas totais superam as receitas. Comum em empresas em crise, startups ou setores com margens pressionadas, reflete fragilidade financeira e risco elevado para acionistas.',
                    riscos='Risco de insolvência, diluição acionária ou necessidade de reestruturação. Pode haver má gestão ou baixa competitividade de mercado.',
                    referencia='Avalie evaluate_ebit para lucratividade operacional, evaluate_cash_flow para geração de caixa e evaluate_debt_to_equity para alavancagem.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação financeira. Priorize análise de custos e estratégias de turnaround.'
                )
            # Verifica se a margem líquida está entre 0 e 5%, indicando lucratividade baixa
            elif 0 <= margem_liquida <= 0.05:
                # Retorna ResultadoIND para lucratividade baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem Líquida <= 5%',
                    descricao='A margem líquida é baixa, indicando lucratividade limitada após todas as despesas. Comum em setores competitivos ou com altos custos, como varejo ou indústria pesada, sugere eficiência reduzida e capacidade limitada de gerar valor para acionistas.',
                    riscos='Risco de margens comprimidas por concorrência ou aumento de custos. Pode haver dificuldades em financiar dividendos ou investimentos.',
                    referencia='Analise evaluate_margem_ebit para lucratividade operacional, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir com cautela, avaliando estratégias de redução de custos e competitividade. Priorize empresas com planos de melhoria financeira.'
                )
            # Verifica se a margem líquida está entre 5% e 10%, indicando lucratividade moderada
            elif 0.05 < margem_liquida <= 0.10:
                # Retorna ResultadoIND para lucratividade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5% < Margem Líquida <= 10%',
                    descricao='A margem líquida está em uma faixa moderada, indicando eficiência razoável na geração de lucro após todas as despesas. Comum em empresas estáveis, como manufatura ou serviços, sugere capacidade de cobrir custos, mas com espaço para melhorias.',
                    riscos='Risco de estagnação na lucratividade em cenários de aumento de custos ou impostos. Pode haver dependência de mercados específicos.',
                    referencia='Compare com evaluate_margem_ebitda para lucratividade operacional, evaluate_giro_ativo para eficiência e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade dos lucros e estratégias de crescimento. Boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se a margem líquida está entre 10% e 20%, indicando boa lucratividade
            elif 0.10 < margem_liquida <= 0.20:
                # Retorna ResultadoIND para boa lucratividade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10% < Margem Líquida <= 20%',
                    descricao='A margem líquida é alta, indicando boa lucratividade após todas as despesas. Comum em empresas com operações eficientes, como bens de consumo ou tecnologia, sugere forte capacidade de gerar valor para acionistas e financiar investimentos.',
                    riscos='Risco de dependência de mercados específicos ou sazonalidade. Pode haver vulnerabilidade a choques econômicos ou aumento de despesas.',
                    referencia='Verifique evaluate_roe para rentabilidade patrimonial, evaluate_cash_flow para geração de caixa e evaluate_p_l para valuation.',
                    recomendacao='Considere investir, mas monitore a consistência dos lucros e exposição a riscos de mercado. Boa opção para investidores que buscam eficiência.'
                )
            # Verifica se a margem líquida excede 20%, indicando lucratividade excepcional
            elif margem_liquida > 0.20:
                # Retorna ResultadoIND para lucratividade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem Líquida > 20%',
                    descricao='A margem líquida é extremamente alta, indicando lucratividade excepcional. Típico de empresas com modelos de negócios eficientes, como tecnologia ou serviços especializados, sugere forte competitividade e capacidade de financiar crescimento ou dividendos.',
                    riscos='Risco de margens insustentáveis em mercados saturados ou com alta concorrência. Pode haver dependência de receitas voláteis.',
                    referencia='Combine com evaluate_margem_ebitda para lucratividade operacional, evaluate_roe para rentabilidade patrimonial e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas diversifique para mitigar riscos de mercado. Considere empresas com crescimento sustentável.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o Lucro Líquido: {mensagem}.
                Verifique os dados de entrada (Lucro Líquido e Receita Líquida) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe EBITDAEvaluator para avaliar o indicador EBITDA
class EBITDAEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do EBITDA
    def __init__(self):
        # Define string multilinha explicando o índice EBITDA
        self.definicao = '''
        O EBITDA (Earnings Before Interest, Taxes, Depreciation and Amortization) representa o lucro antes de juros, impostos,
        depreciação e amortização, calculado como Receita Líquida menos Custos e Despesas Operacionais (excluindo juros, impostos,
        depreciação e amortização). É um indicador de lucratividade operacional que avalia a capacidade da empresa de gerar caixa
        a partir de suas operações principais, sem os efeitos de estrutura de capital ou políticas contábeis. Valores altos sugerem
        eficiência operacional, enquanto valores baixos ou negativos indicam fragilidade.
        '''
        # Define a categoria de agrupamento como "Lucratividade Operacional"
        self.agrupador = 'Lucratividade Operacional'
        # Define a fórmula do EBITDA
        self.formula = 'EBITDA = Receita Líquida - Custos Operacionais - Despesas Operacionais (excluindo Depreciação e Amortização)'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor do EBITDA em relação à Receita Líquida e retorna um objeto ResultadoIND
    def avaliar(self, ebitda, receita_liquida):
        # Tenta processar o valor do EBITDA e Receita Líquida
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(ebitda, "EBITDA"), (receita_liquida, "Receita Líquida")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte EBITDA e Receita Líquida para float
            ebitda = float(ebitda)
            receita_liquida = float(receita_liquida)
            # Calcula a margem EBITDA (EBITDA / Receita Líquida)
            if receita_liquida == 0:
                raise ValueError("A Receita Líquida não pode ser zero para calcular a margem EBITDA.")
            margem_ebitda = ebitda / receita_liquida
            # Verifica se EBITDA é negativo, indicando prejuízo operacional
            if margem_ebitda < 0:
                # Retorna ResultadoIND para EBITDA negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='EBITDA < 0',
                    descricao='Um EBITDA negativo indica prejuízo operacional antes de depreciação e amortização, sugerindo que os custos operacionais superam a receita. Comum em empresas em crise ou setores com margens pressionadas, reflete ineficiência operacional e alto risco financeiro.',
                    riscos='Risco de insolvência, má gestão operacional ou baixa competitividade. Pode haver necessidade de reestruturação ou cortes de custos.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade líquida, evaluate_cash_flow para geração de caixa e evaluate_giro_ativo para eficiência.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação operacional. Priorize análise de custos e estratégias de turnaround.'
                )
            # Verifica se a margem EBITDA está entre 0 e 10%, indicando lucratividade operacional baixa
            elif 0 <= margem_ebitda <= 0.10:
                # Retorna ResultadoIND para lucratividade baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem EBITDA <= 10%',
                    descricao='A margem EBITDA é baixa, indicando lucratividade operacional limitada. Comum em setores competitivos ou com altos custos, como varejo ou indústria pesada, sugere eficiência reduzida na geração de caixa operacional, com margens apertadas.',
                    riscos='Risco de margens comprimidas por concorrência ou aumento de custos. Pode haver dificuldades em financiar investimentos ou pagar dívidas.',
                    referencia='Analise evaluate_margem_bruta para eficiência de custos, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir com cautela, avaliando estratégias de redução de custos e competitividade. Priorize empresas com planos de melhoria operacional.'
                )
            # Verifica se a margem EBITDA está entre 10% e 20%, indicando lucratividade moderada
            elif 0.10 < margem_ebitda <= 0.20:
                # Retorna ResultadoIND para lucratividade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='10% < Margem EBITDA <= 20%',
                    descricao='A margem EBITDA está em uma faixa moderada, indicando eficiência razoável na geração de caixa operacional. Comum em empresas estáveis, como manufatura ou serviços, sugere capacidade de cobrir custos operacionais, mas com espaço para melhorias.',
                    riscos='Risco de estagnação na lucratividade em cenários de aumento de custos ou concorrência. Pode haver dependência de mercados específicos.',
                    referencia='Compare com evaluate_margem_liquida para lucratividade líquida, evaluate_giro_ativo para eficiência e evaluate_debt_to_ebitda para alavancagem.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade dos lucros e estratégias de crescimento. Boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se a margem EBITDA está entre 20% e 30%, indicando boa lucratividade
            elif 0.20 < margem_ebitda <= 0.30:
                # Retorna ResultadoIND para boa lucratividade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='20% < Margem EBITDA <= 30%',
                    descricao='A margem EBITDA é alta, indicando boa lucratividade operacional. Comum em empresas com operações eficientes, como bens de consumo ou tecnologia, sugere forte capacidade de gerar caixa a partir das atividades principais, com folga para investimentos.',
                    riscos='Risco de dependência de mercados específicos ou sazonalidade. Pode haver vulnerabilidade a choques econômicos ou aumento de custos.',
                    referencia='Verifique evaluate_roic para retorno sobre capital, evaluate_cash_flow para geração de caixa e evaluate_p_ebitda para valuation.',
                    recomendacao='Considere investir, mas monitore a consistência dos lucros e exposição a riscos de mercado. Boa opção para investidores que buscam eficiência.'
                )
            # Verifica se a margem EBITDA excede 30%, indicando lucratividade excepcional
            elif margem_ebitda > 0.30:
                # Retorna ResultadoIND para lucratividade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem EBITDA > 30%',
                    descricao='A margem EBITDA é extremamente alta, indicando lucratividade operacional excepcional. Típico de empresas com modelos de negócios eficientes, como tecnologia ou serviços especializados, sugere forte competitividade e capacidade de financiar crescimento ou dividendos.',
                    riscos='Risco de margens insustentáveis em mercados saturados ou com alta concorrência. Pode haver dependência de receitas voláteis.',
                    referencia='Combine com evaluate_margem_liquida para lucratividade líquida, evaluate_roe para rentabilidade patrimonial e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a robustez operacional, mas diversifique para mitigar riscos de mercado. Considere empresas com crescimento sustentável.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o EBITDA: {mensagem}.
                Verifique os dados de entrada (EBITDA e Receita Líquida) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
class DividaBrutaEvaluator:
    # Construtor que inicializa definição, agrupador e descrição da Dívida Bruta
    def __init__(self):
        # Define string multilinha explicando o índice Dívida Bruta
        self.definicao = '''
        A Dívida Bruta representa o total de obrigações financeiras da empresa, incluindo empréstimos, financiamentos e outros passivos
        com custo financeiro, de curto e longo prazo. É um indicador de alavancagem que avalia o montante absoluto de dívida, sem considerar
        a disponibilidade de caixa. Um valor alto sugere maior risco financeiro, enquanto valores baixos indicam menor dependência de dívida.
        '''
        # Define a categoria de agrupamento como "Alavancagem"
        self.agrupador = 'Alavancagem'
        # Define a fórmula da Dívida Bruta (não é uma razão, mas um valor absoluto)
        self.formula = 'Dívida Bruta = Total de Empréstimos e Financiamentos (Curto e Longo Prazo)'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor da Dívida Bruta em relação aos Ativos Totais e retorna um objeto ResultadoIND
    def avaliar(self, divida_bruta, ativos_totais):
        # Tenta processar o valor da Dívida Bruta e Ativos Totais
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(divida_bruta, "Dívida Bruta"), (ativos_totais, "Ativos Totais")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Dívida Bruta e Ativos Totais para float
            divida_bruta = float(divida_bruta)
            ativos_totais = float(ativos_totais)
            # Calcula a proporção da Dívida Bruta em relação aos Ativos Totais
            if ativos_totais == 0:
                raise ValueError("Os Ativos Totais não podem ser zero para calcular a proporção.")
            proporcao_divida_ativos = divida_bruta / ativos_totais
            # Verifica se Dívida Bruta é negativa, indicando erro nos dados
            if divida_bruta < 0:
                # Retorna ResultadoIND para Dívida Bruta negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dívida Bruta < 0',
                    descricao='Uma Dívida Bruta negativa é inválida, indicando erros nos dados financeiros ou relatórios contábeis. Isso pode refletir falhas na consolidação de dívidas ou manipulação de informações, tornando a análise de alavancagem inviável.',
                    riscos='Risco de manipulação contábil ou baixa confiabilidade nos dados financeiros. Pode haver ausência de transparência ou erros graves nos relatórios.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou falta de transparência. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se Dívida Bruta é zero, indicando ausência de dívida
            elif divida_bruta == 0:
                # Retorna ResultadoIND para ausência de dívida
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dívida Bruta = 0',
                    descricao='A Dívida Bruta é zero, indicando que a empresa não possui obrigações financeiras. Comum em empresas com forte geração de caixa ou baixa necessidade de capital, como tecnologia ou serviços, isso sugere robustez financeira e mínima alavancagem.',
                    riscos='Risco de subalavancagem, perdendo oportunidades de crescimento com dívida barata. Pode haver ineficiência na alocação de capital próprio.',
                    referencia='Analise evaluate_roe para rentabilidade patrimonial, evaluate_cash_flow para geração de caixa e evaluate_psr para receita.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de capital. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se a proporção está entre 0 e 0.3, indicando baixa alavancagem
            elif 0 < proporcao_divida_ativos <= 0.3:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0 < Dívida Bruta / Ativos <= 0.3',
                    descricao='A Dívida Bruta é baixa em relação aos ativos, indicando alavancagem moderada e boa saúde financeira. Comum em empresas com gestão financeira sólida, como bens de consumo ou tecnologia, sugere capacidade de gerenciar dívidas sem comprometer a estabilidade.',
                    riscos='Risco de subalavancagem, limitando crescimento em setores competitivos. Pode haver dependência de capital próprio, reduzindo retornos potenciais.',
                    referencia='Compare com evaluate_debt_to_ebitda para alavancagem operacional, evaluate_liquidez_corrente para liquidez e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas verifique a estratégia de crescimento e uso de capital. Boa opção para investidores que priorizam estabilidade.'
                )
            # Verifica se a proporção está entre 0.3 e 0.6, indicando alavancagem moderada
            elif 0.3 < proporcao_divida_ativos <= 0.6:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.3 < Dívida Bruta / Ativos <= 0.6',
                    descricao='A Dívida Bruta está em uma faixa moderada em relação aos ativos, indicando equilíbrio entre dívida e capital próprio. Comum em empresas estáveis, como varejo ou manufatura, mas reflete dependência de financiamento externo que pode aumentar em cenários adversos.',
                    riscos='Risco de pressão financeira se os lucros caírem ou taxas de juros subirem. Pode haver limitações para novos investimentos ou pagamento de dividendos.',
                    referencia='Verifique evaluate_div_liquida_pl para alavancagem líquida, evaluate_margem_liquida para lucratividade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir com cautela, avaliando a capacidade de pagamento de dívidas e estabilidade dos lucros. Priorize empresas com fluxo de caixa robusto.'
                )
            # Verifica se a proporção está entre 0.6 e 1.0, indicando alta alavancagem
            elif 0.6 < proporcao_divida_ativos <= 1.0:
                # Retorna ResultadoIND para alta alavancagem
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0.6 < Dívida Bruta / Ativos <= 1.0',
                    descricao='A Dívida Bruta é alta em relação aos ativos, indicando elevada alavancagem. Comum em setores intensivos em capital, como infraestrutura ou energia, mas sugere risco financeiro significativo devido à forte dependência de dívidas para financiar operações.',
                    riscos='Risco de insolvência em cenários de queda na receita ou aumento de juros. Pode haver restrições de credores ou necessidade de venda de ativos.',
                    referencia='Analise evaluate_debt_to_equity para estrutura de dívida, evaluate_ebit_margin para eficiência operacional e evaluate_liquidez_imediata para liquidez.',
                    recomendacao='Evite investir a menos que haja forte geração de caixa ou planos de desalavancagem. Monitore a capacidade de pagamento de dívidas.'
                )
            # Verifica se a proporção excede 1.0, indicando alavancagem crítica
            elif proporcao_divida_ativos > 1.0:
                # Retorna ResultadoIND para alavancagem crítica
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dívida Bruta / Ativos > 1.0',
                    descricao='A Dívida Bruta excede os ativos totais, indicando alavancagem extrema e fragilidade financeira grave. Comum em empresas em crise ou com má gestão financeira, isso sugere risco elevado de insolvência e dificuldade em honrar obrigações financeiras.',
                    riscos='Risco de falência, reestruturação forçada ou diluição acionária. Pode haver incapacidade de cobrir dívidas ou restrições severas de credores.',
                    referencia='Avalie evaluate_cash_flow para geração de caixa, evaluate_liquidez_corrente para liquidez e evaluate_p_vp para valuation patrimonial.',
                    recomendacao='Evite investir devido ao alto risco de perdas. Priorize análise de recuperação financeira e estratégias de redução de dívida.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar a Dívida Bruta: {mensagem}.
                Verifique os dados de entrada (Dívida Bruta e Ativos Totais) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe VPAEvaluator para avaliar o indicador Valor Patrimonial por Ação (VPA)
class VPAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do VPA
    def __init__(self):
        # Define string multilinha explicando o índice VPA
        self.definicao = '''
        O VPA (Valor Patrimonial por Ação) mede o valor contábil do patrimônio líquido da empresa por ação, calculado
        como (Patrimônio Líquido / Número Total de Ações). É um indicador de valuation que avalia o valor intrínseco
        de cada ação com base nos ativos líquidos da empresa. Um VPA alto sugere maior respaldo patrimonial por ação,
        enquanto valores baixos ou negativos indicam fragilidade financeira ou patrimônio reduzido.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do VPA
        self.formula = 'VPA = Patrimônio Líquido / Número Total de Ações'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor do VPA em relação ao preço da ação (P/VPA) e retorna um objeto ResultadoIND
    def avaliar(self, vpa, preco_acao=None):
        # Tenta processar o valor do VPA e preço da ação
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(vpa, "VPA"), (preco_acao, "preço da ação")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte VPA e preço da ação para float
            #vpa = float(vpa)
            p_vpa = float(vpa)
            #preco_acao = float(preco_acao)
            # Calcula o P/VPA (Preço / Valor Patrimonial por Ação)
            #if vpa == 0:
            #    raise ValueError("O VPA não pode ser zero para calcular P/VPA.")
            #p_vpa = preco_acao / vpa
            # Verifica se P/VPA é negativo, indicando patrimônio líquido negativo
            if p_vpa < 0:
                # Retorna ResultadoIND para P/VPA negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/VPA < 0',
                    descricao='Um P/VPA negativo indica que o patrimônio líquido é negativo, sugerindo prejuízos acumulados ou problemas financeiros graves. Isso pode ocorrer em empresas em crise, com alta alavancagem ou ativos desvalorizados, tornando o VPA irrelevante e indicando instabilidade.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver baixa atratividade para investidores devido à fragilidade patrimonial.',
                    referencia='Avalie evaluate_roe para rentabilidade patrimonial, evaluate_div_liquida_pl para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação patrimonial. Priorize análise de turnaround e saúde financeira.'
                )
            # Verifica se P/VPA está entre 0 e 0.8, indicando forte subvalorização
            elif 0 <= p_vpa <= 0.8:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/VPA <= 0.8',
                    descricao='O P/VPA está muito baixo, sugerindo que a ação está fortemente subvalorizada em relação ao patrimônio líquido por ação. Essa faixa indica oportunidades de compra, comum em empresas com ativos sólidos, mas preço de mercado deprimido devido a ciclos econômicos ou baixa percepção de mercado.',
                    riscos='Risco de ativos obsoletos ou baixa rentabilidade patrimonial. Pode haver desafios setoriais ou problemas operacionais que justifiquem o desconto no preço.',
                    referencia='Analise evaluate_p_l para comparação de lucros, evaluate_roe para rentabilidade e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Considere investir, mas verifique a qualidade dos ativos e a rentabilidade patrimonial. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/VPA está entre 0.8 e 1.2, indicando valuation equilibrado
            elif 0.8 < p_vpa <= 1.2:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.8 < P/VPA <= 1.2',
                    descricao='O P/VPA está em uma faixa equilibrada, sugerindo que o preço da ação está alinhado com o valor patrimonial por ação. Essa faixa é comum em empresas estáveis com patrimônio sólido e rentabilidade moderada, refletindo confiança do mercado sem prêmios excessivos.',
                    riscos='Risco de estagnação no preço se a rentabilidade patrimonial não melhorar. Pode haver dependência de fatores macroeconômicos que afetem o valor de mercado.',
                    referencia='Compare com evaluate_p_l para valuation de lucros, evaluate_margem_liquida para eficiência e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de rentabilidade e estratégias de crescimento antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se P/VPA está entre 1.2 e 1.8, indicando valuation moderado
            elif 1.2 < p_vpa <= 1.8:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1.2 < P/VPA <= 1.8',
                    descricao='O P/VPA está moderadamente elevado, indicando que o mercado atribui um prêmio ao valor patrimonial por ação. Essa faixa sugere expectativas de crescimento ou confiança nos ativos, comum em empresas com potencial moderado ou em setores com margens estáveis.',
                    riscos='Risco de correção no preço se a rentabilidade patrimonial não atender às expectativas. Pode haver sobrevalorização de ativos intangíveis ou dependência de setores cíclicos.',
                    referencia='Verifique evaluate_p_ebitda para valuation operacional, evaluate_roe para retorno patrimonial e evaluate_beta para volatilidade.',
                    recomendacao='Considere esperar por sinais de crescimento ou redução no valuation antes de investir. Combine com análise de fluxo de caixa e qualidade dos ativos.'
                )
            # Verifica se P/VPA está entre 1.8 e 2.5, indicando sobrevalorização
            elif 1.8 < p_vpa <= 2.5:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='1.8 < P/VPA <= 2.5',
                    descricao='O P/VPA está consideravelmente elevado, indicando sobrevalorização em relação ao valor patrimonial por ação. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se os ativos não gerarem retornos esperados. Pode haver sobrevalorização de intangíveis ou bolhas setoriais impulsionadas por hype de mercado.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para eficiência e evaluate_cash_conversion_cycle para ciclo de caixa.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com ativos produtivos e rentabilidade sólida.'
                )
            # Verifica se P/VPA excede 2.5, indicando sobrevalorização extrema
            elif p_vpa > 2.5:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='P/VPA > 2.5',
                    descricao='O P/VPA é extremamente elevado, sugerindo forte sobrevalorização em relação ao valor patrimonial por ação. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço da ação desconecta significativamente do patrimônio líquido.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de ativos intangíveis ou expectativas irreais de crescimento.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_growth_rate para taxas de crescimento.',
                    recomendacao='Não invista devido ao risco elevado de perdas. Considere vender posições existentes e buscar alternativas com valuation mais razoável.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o VPA: {mensagem}.
                Verifique os dados de entrada (VPA e preço da ação) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


# Define a classe PLEvaluator para avaliar o indicador Preço sobre Lucro (P/L)
class PLEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/L
    def __init__(self):
        # Define string multilinha explicando o índice P/L
        self.definicao = '''
        O P/L (Preço sobre Lucro) mede o valor de mercado da empresa em relação ao seu lucro líquido, calculado
        como (Valor de Mercado / Lucro Líquido). É um indicador de valuation que avalia se a empresa está cara ou barata
        com base em sua lucratividade final. Um P/L baixo sugere subvalorização, enquanto valores altos indicam sobrevalorização
        ou expectativas de crescimento futuro.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/L
        self.formula = 'P/L = Valor de Mercado / Lucro Líquido'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor do P/L e retorna um objeto ResultadoIND
    def avaliar(self, p_l):
        # Tenta processar o valor do P/L
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_l, (int, float)) and not (isinstance(p_l, str) and p_l.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do P/L deve ser numérico.")
            # Converte o P/L para float para garantir que é numérico
            p_l = float(p_l)
            # Verifica se P/L é negativo, indicando prejuízo líquido
            if p_l < 0:
                # Retorna ResultadoIND para P/L negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/L < 0',
                    descricao='Um P/L negativo indica que a empresa está gerando prejuízo líquido, tornando a valuation irrelevante. Isso pode refletir ineficiência operacional, altos custos ou perdas extraordinárias, comum em empresas em crise ou setores com margens apertadas, apontando para instabilidade financeira.',
                    riscos='Risco de falência, reestruturação ou diluição acionária devido a prejuízos. Pode haver endividamento crescente ou perda de competitividade no mercado.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_roe para rentabilidade patrimonial e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação de lucros. Priorize análise de custos, eficiência operacional e estratégias de turnaround.'
                )
            # Verifica se P/L está entre 0 e 10, indicando forte subvalorização
            elif 0 <= p_l <= 10:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/L <= 10',
                    descricao='O P/L está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação ao seu lucro líquido. Essa faixa indica oportunidades de compra, comum em empresas com lucros sólidos, mas preço de mercado deprimido devido a ciclos econômicos, baixa visibilidade ou setores menos atrativos.',
                    riscos='Risco de lucros instáveis ou manipulação contábil. Pode haver desafios setoriais ou baixa percepção de crescimento que justifiquem o desconto no valuation.',
                    referencia='Analise evaluate_p_ebit para comparação operacional, evaluate_roe para rentabilidade e evaluate_debt_to_equity para alavancagem.',
                    recomendacao='Considere investir, mas verifique a sustentabilidade dos lucros e a composição do valor de mercado. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/L está entre 10 e 15, indicando valuation equilibrado
            elif 10 < p_l <= 15:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10 < P/L <= 15',
                    descricao='O P/L está em uma faixa equilibrada, sugerindo que o valor de mercado está alinhado com o lucro líquido da empresa. Essa faixa é comum em empresas estáveis com lucros consistentes e crescimento moderado, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação nos lucros devido a concorrência ou custos crescentes. Pode haver dependência de fatores macroeconômicos que afetem o lucro ou o preço de mercado.',
                    referencia='Compare com evaluate_p_ebitda para valuation ajustado, evaluate_margem_liquida para eficiência e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de lucros e planos de expansão antes de investir. Pode ser uma boa opção para investidores de longo prazo com foco em estabilidade.'
                )
            # Verifica se P/L está entre 15 e 20, indicando valuation moderado
            elif 15 < p_l <= 20:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='15 < P/L <= 20',
                    descricao='O P/L está moderadamente elevado, indicando que o mercado atribui um prêmio ao lucro líquido da empresa. Essa faixa sugere expectativas de crescimento futuro ou confiança na gestão, comum em empresas com potencial moderado ou em setores com margens estáveis.',
                    riscos='Risco de correção no preço se os lucros não crescerem conforme esperado. Pode haver sobrevalorização devido a otimismo de mercado ou dependência de setores cíclicos.',
                    referencia='Verifique evaluate_p_vp para valuation patrimonial, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Considere esperar por sinais de crescimento ou redução no valuation antes de investir. Combine com análise de margens e fluxo de caixa para validar o prêmio.'
                )
            # Verifica se P/L está entre 20 e 25, indicando sobrevalorização
            elif 20 < p_l <= 25:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='20 < P/L <= 25',
                    descricao='O P/L está consideravelmente elevado, indicando sobrevalorização em relação ao lucro líquido. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se os lucros declinarem ou expectativas não se realizarem. Pode haver bolhas setoriais ou dependência de fatores intangíveis no valuation.',
                    referencia='Combine com evaluate_psr para receita, evaluate_roic para retorno sobre capital e evaluate_current_ratio para liquidez operacional.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com lucros crescentes e fundamentos sólidos.'
                )
            # Verifica se P/L excede 25, indicando sobrevalorização extrema
            elif p_l > 25:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='P/L > 25',
                    descricao='O P/L é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de crescimento. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço de mercado desconecta dos fundamentos financeiros.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de fatores intangíveis, risco de fraudes em valuation ou lucros inflados.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_growth_rate para taxas de crescimento.',
                    recomendacao='Não invista devido ao risco elevado de perdas. Considere vender posições existentes e buscar alternativas com valuation mais razoável.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o P/L: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


class MargemBrutaEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula da Margem Bruta
    def __init__(self):
        # Define string multilinha explicando o índice Margem Bruta
        self.definicao = '''
        A Margem Bruta mede a rentabilidade bruta da empresa, calculada como
        ((Receita Líquida - Custo dos Produtos Vendidos) / Receita Líquida) * 100.
        É um indicador de eficiência operacional que mostra a porcentagem da receita que resta após os custos diretos de produção. Uma margem bruta alta sugere eficiência na gestão de custos, enquanto valores baixos indicam pressão sobre custos ou baixa precificação.
        '''
        # Define a categoria de agrupamento como "Eficiência Operacional"
        self.agrupador = 'Eficiência Operacional'
        # Define a fórmula da Margem Bruta
        self.formula = 'Margem Bruta (%) = ((Receita Líquida - Custo dos Produtos Vendidos) / Receita Líquida) * 100'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor da Margem Bruta e retorna um objeto ResultadoIND
    def avaliar(self, margem_bruta):
        # Tenta processar o valor da Margem Bruta
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(margem_bruta, (int, float)) and not (isinstance(margem_bruta, str) and margem_bruta.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Margem Bruta deve ser numérico.")
            # Converte a Margem Bruta para float para garantir que é numérico
            margem_bruta = float(margem_bruta)
            # Verifica se Margem Bruta é negativa, indicando prejuízo bruto
            if margem_bruta < 0:
                # Retorna ResultadoIND para Margem Bruta negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Margem Bruta < 0%',
                    descricao='Uma Margem Bruta negativa indica que os custos diretos de produção excedem a receita líquida, sugerindo ineficiência grave ou precificação inadequada. Isso pode ocorrer em empresas com problemas operacionais, alta concorrência ou custos descontrolados, indicando risco financeiro elevado.',
                    riscos='Risco de insustentabilidade operacional, com potencial para prejuízos contínuos ou falência. Pode haver necessidade de reestruturação ou dependência de subsídios externos.',
                    referencia='Avalie evaluate_cogs para custos de produção, evaluate_cash_flow para geração de caixa e evaluate_competitive_position para concorrência.',
                    recomendacao='Evite investir até que a empresa demonstre controle de custos ou melhoria na precificação. Priorize análise de eficiência operacional e estratégias de mercado.'
                )
            # Verifica se Margem Bruta está entre 0 e 20, indicando eficiência baixa
            elif 0 <= margem_bruta <= 20:
                # Retorna ResultadoIND para eficiência baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem Bruta <= 20%',
                    descricao='A Margem Bruta está baixa, sugerindo eficiência operacional limitada. Isso é comum em setores com alta concorrência, custos elevados ou baixa diferenciação de produtos, como varejo ou indústrias de commodities, onde a precificação é pressionada.',
                    riscos='Risco de margens comprimidas por aumento de custos ou queda na receita. Pode haver dependência de economias de escala ou vulnerabilidade a choques de mercado.',
                    referencia='Analise evaluate_margem_liquida para lucratividade final, evaluate_cost_structure para composição de custos e evaluate_pricing_power para precificação.',
                    recomendacao='Considere investir apenas se houver estratégias claras para redução de custos ou aumento de preços. Verifique tendências de receita e competitividade.'
                )
            # Verifica se Margem Bruta está entre 20 e 40, indicando eficiência moderada
            elif 20 < margem_bruta <= 40:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='20 < Margem Bruta <= 40%',
                    descricao='A Margem Bruta está em uma faixa moderada, indicando eficiência operacional razoável. Essa faixa é comum em empresas com controle de custos decente, mas sem grande poder de precificação, como manufatura ou serviços com margens estáveis.',
                    riscos='Risco de volatilidade nas margens devido a flutuações nos custos de insumos ou concorrência agressiva. Pode haver limitações em investir em crescimento sem comprometer lucros.',
                    referencia='Compare com evaluate_ebitda_margin para lucro operacional, evaluate_roe para rentabilidade e evaluate_market_share para posição de mercado.',
                    recomendacao='Avalie o histórico de margens e estratégias de diferenciação antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade operacional.'
                )
            # Verifica se Margem Bruta está entre 40 e 60, indicando boa eficiência
            elif 40 < margem_bruta <= 60:
                # Retorna ResultadoIND para boa eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='40 < Margem Bruta <= 60%',
                    descricao='A Margem Bruta está em uma faixa alta, sugerindo boa eficiência operacional e controle de custos diretos. Essa faixa é comum em empresas com forte poder de precificação ou operações otimizadas, como tecnologia ou bens de consumo de marca.',
                    riscos='Risco de dependência de produtos premium ou mercados específicos. Aumento de custos ou perda de poder de precificação pode reduzir margens no futuro.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão de receita.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade das margens e a força competitiva da empresa.'
                )
            # Verifica se Margem Bruta excede 60, indicando eficiência excepcional
            elif margem_bruta > 60:
                # Retorna ResultadoIND para eficiência excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem Bruta > 60%',
                    descricao='A Margem Bruta é extremamente alta, indicando eficiência operacional excepcional e forte poder de precificação. Essa faixa é típica de empresas com marcas premium, baixa concorrência ou modelos de negócios escaláveis, como software ou bens de luxo.',
                    riscos='Risco de sobredependência de nichos de mercado ou produtos específicos. Mudanças regulatórias, entrada de concorrentes ou saturação podem impactar margens.',
                    referencia='Combine com evaluate_psr para receita, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem margens sustentáveis, mas diversifique para mitigar riscos de concentração ou mudanças de mercado.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar a Margem Bruta: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )





# Define a classe ResultadoIND para armazenar resultados da avaliação P/VP


class ResultadoIND:
    # Construtor que inicializa os atributos do resultado da avaliação P/VP
    def __init__(self, classificacao, faixa, descricao, definicao, agrupador, formula, riscos, referencia_cruzada, recomendacao):
        # Atribui a classificação (ex.: "Ótimo", "Crítico") à variável de instância
        self.classificacao = classificacao
        # Atribui a faixa de P/VP (ex.: "0 <= P/VP <= 0.8") à variável de instância
        self.faixa = faixa
        # Atribui a descrição, removendo espaços em branco no início/fim
        self.descricao = descricao.strip()
        # Atribui a definição do P/VP, removendo espaços em branco
        self.definicao = definicao.strip()
        # Atribui a categoria de agrupamento (ex.: "Valuation")
        self.agrupador = agrupador
        # Atribui a fórmula do P/VP
        self.formula = formula
        # Atribui os riscos, removendo espaços em branco
        self.riscos = riscos.strip()
        # Atribui as referências cruzadas, removendo espaços em branco
        self.referencia_cruzada = referencia_cruzada.strip()
        # Atribui a recomendação, removendo espaços em branco
        self.recomendacao = recomendacao.strip()

    # Define a representação em string do objeto para depuração/impressão
    def __repr__(self):
        # Retorna string formatada com classificação e faixa
        return f"<ResultadoIND: {self.classificacao} | Faixa: {self.faixa}>"

    # Converte o objeto em dicionário para serialização
    def to_dict(self):
        # Retorna dicionário com todos os atributos da instância
        return {
            'classificacao': self.classificacao,
            'faixa': self.faixa,
            'descricao': self.descricao,
            'definicao': self.definicao,
            'agrupador': self.agrupador,
            'formula': self.formula,
            'riscos': self.riscos,
            'referencia_cruzada': self.referencia_cruzada,
            'recomendacao': self.recomendacao
        }

# Define a classe PVPEvaluator para avaliar índices P/VP
class PVPEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/VP
    def __init__(self):
        # Define string multilinha explicando o índice P/VP
        self.definicao = '''
        O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
        como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
        ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
        subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/VP
        self.formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)
        return wrapper

    # Avalia o valor P/VP e retorna um objeto ResultadoIND
    def avaliar(self, p_vp):
        # Tenta processar o valor P/VP
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_vp, (int, float)) and not (isinstance(p_vp, str) and p_vp.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de P/VP deve ser numérico.")
            # Converte o P/VP para float para garantir que é numérico
            p_vp = float(p_vp)
            # Verifica se P/VP é negativo, indicando problemas críticos
            if p_vp < 0:
                # Retorna ResultadoIND para P/VP negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/VP < 0',
                    descricao='Um P/VP negativo indica que o valor patrimonial por ação é negativo, geralmente devido a prejuízos acumulados que excedem o capital próprio. Isso sugere problemas financeiros graves, como endividamento excessivo, falência iminente ou distorções contábeis.',
                    riscos='Risco de falência, diluição acionária em reestruturações, baixa liquidez das ações ou manipulação contábil. Ativos registrados podem ser de baixa qualidade ou superavaliados.',
                    referencia='Avalie evaluate_debt_to_equity para saúde financeira, evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação financeira. Priorize a análise de indicadores de endividamento (Dívida/EBITDA) e fluxo de caixa.'
                )
            # Verifica se P/VP está entre 0 e 0.8, indicando forte subvalorização
            elif 0 <= p_vp <= 0.8:
                # Retorna ResultadoIND para ação fortemente subvalorizada
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/VP <= 0.8',
                    descricao='A ação está sendo negociada significativamente abaixo de seu valor patrimonial, indicando forte subvalorização. Isso pode ocorrer em empresas com ativos sólidos, mas subavaliadas pelo mercado devido a condições setoriais, baixa visibilidade ou ciclos econômicos desfavoráveis.',
                    riscos='Ativos registrados podem ser obsoletos ou superavaliados (ex.: estoques desatualizados, imóveis depreciados). Há risco de baixa rentabilidade (ROE baixo) ou desafios operacionais que justificam o desconto.',
                    referencia='Analise evaluate_vpa para valor patrimonial, evaluate_roe para rentabilidade e evaluate_cash_flow para sustentabilidade financeira.',
                    recomendacao='Considere investir, mas conduza uma análise detalhada da qualidade dos ativos e da rentabilidade (ROE, ROIC). Verifique se a subvalorização é justificada por fundamentos sólidos.'
                )
            # Verifica se P/VP está entre 0.8 e 1.2, indicando valuation atrativo
            elif 0.8 < p_vp <= 1.2:
                # Retorna ResultadoIND para ação com valuation atrativo
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.8 < P/VP <= 1.2',
                    descricao='O preço da ação está próximo ao seu valor patrimonial, sugerindo um valuation equilibrado com potencial de valorização moderado. Essa faixa é comum em empresas estáveis com fundamentos sólidos, mas sem grandes expectativas de crescimento explosivo.',
                    riscos='Possibilidade de estagnação em setores maduros, baixa geração de lucros ou crescimento limitado. A empresa pode enfrentar concorrência intensa ou desafios setoriais.',
                    referencia='Compare com evaluate_p_l para lucros, evaluate_pl_ativos para estrutura de capital e evaluate_margem_liquida para eficiência operacional.',
                    recomendacao='Avalie o potencial de crescimento da empresa (ex.: receita, lucros) e a saúde financeira. Pode ser uma boa oportunidade para investidores de valor.'
                )
            # Verifica se P/VP está entre 1.2 e 1.8, indicando valuation moderada
            elif 1.2 < p_vp <= 1.8:
                # Retorna ResultadoIND para valuation moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1.2 < P/VP <= 1.8',
                    descricao='O preço da ação está ligeiramente acima do valor patrimonial, refletindo um prêmio moderado pago pelo mercado. Isso pode indicar expectativas de crescimento futuro ou confiança na gestão, mas também uma avaliação cautelosa.',
                    riscos='Risco de estagnação se o crescimento esperado não se materializar. Setores maduros ou cíclicos podem enfrentar volatilidade, e o prêmio pode não ser justificado por fundamentos fracos.',
                    referencia='Verifique evaluate_peg_ratio para crescimento, evaluate_evebitda para valuation e evaluate_beta para volatilidade.',
                    recomendacao='Considere esperar por melhores condições de mercado ou sinais de crescimento sustentável. Combine com indicadores de lucro e crescimento.'
                )
            # Verifica se P/VP está entre 1.8 e 2.5, indicando sobrevalorização
            elif 1.8 < p_vp <= 2.5:
                # Retorna ResultadoIND para ação sobrevalorizada
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='1.8 < P/VP <= 2.5',
                    descricao='O preço da ação está consideravelmente acima do valor patrimonial, indicando sobrevalorização moderada. Essa faixa é comum em empresas com expectativas de crescimento ou em setores de alto potencial, mas o preço já reflete otimismo significativo.',
                    riscos='Risco de correção de preço se as expectativas de crescimento não se concretizarem. A empresa pode estar exposta a volatilidade de mercado ou mudanças macroeconômicas.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para eficiência e evaluate_cash_flow para sustentabilidade.',
                    recomendacao='Monitore de perto o desempenho financeiro e catalisadores de crescimento (ex.: novos produtos, expansão). Invista apenas com fundamentos robustos.'
                )
            # Verifica se P/VP está entre 2.5 e 4, indicando alta sobrevalorização
            elif 2.5 < p_vp <= 4:
                # Retorna ResultadoIND para ação muito sobrevalorizada
                return self.gerar_resultado(
                    classificacao='Alto',
                    faixa='2.5 < P/VP <= 4',
                    descricao='O preço da ação está significativamente elevado em relação ao patrimônio, sugerindo uma valuation arriscada. Essa faixa é típica de empresas em setores de alto crescimento, mas o preço reflete expectativas agressivas.',
                    riscos='Alta sensibilidade a mudanças econômicas, como aumento de juros ou desaceleração setorial. Falhas em atingir metas de crescimento podem levar a quedas acentuadas.',
                    referencia='Avalie evaluate_p_ativo para ativos, evaluate_crescimento_receita para tendências e evaluate_evebitda para valuation.',
                    recomendacao='Evite investir a menos que haja evidências claras de crescimento excepcional e margens elevadas. Priorize indicadores de receita e eficiência.'
                )
            # Verifica se P/VP excede 4, indicando sobrevalorização extrema
            elif p_vp > 4:
                # Retorna ResultadoIND para ação extremamente sobrevalorizada
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='P/VP > 4',
                    descricao='O preço da ação é extremamente elevado em relação ao patrimônio, indicando forte especulação ou expectativas irreais de crescimento. Essa faixa é comum em bolhas de mercado ou empresas com narrativas especulativas.',
                    riscos='Alto risco de bolhas especulativas, com potencial para quedas significativas no preço. A empresa pode estar sobrevalorizada devido a hype ou baixa liquidez patrimonial.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_p_l para lucros.',
                    recomendacao='Não invista devido ao risco elevado de perdas. Considere alternativas com valuation mais razoável.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoIND com mensagem de erro
            return self._erro(mensagem=str(e))

    # Cria objeto ResultadoIND com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Instancia e retorna ResultadoIND com atributos da instância
        return ResultadoIND(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia,
            recomendacao=recomendacao
        )

    # Trata erros criando um ResultadoIND de erro
    def _erro(self, mensagem):
        # Retorna ResultadoIND com detalhes de erro
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o P/VP: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Exibe os atributos de um ResultadoIND formatados
def exibir_resultado(resultado):
    # Imprime cabeçalho do resultado da avaliação
    print("📊 Resultado da Avaliação P/VP")
    # Imprime a classificação
    print(f"Classificação: {resultado.classificacao}")
    # Imprime a faixa de P/VP
    print(f"Faixa: {resultado.faixa}")
    # Imprime a descrição
    print(f"Descrição: {resultado.descricao}")
    # Imprime a definição do P/VP
    print(f"Definição: {resultado.definicao}")
    # Imprime a categoria de agrupamento
    print(f"Agrupador: {resultado.agrupador}")
    # Imprime a fórmula
    print(f"Fórmula: {resultado.formula}")
    # Imprime os riscos
    print(f"Riscos: {resultado.riscos}")
    # Imprime as referências cruzadas
    print(f"Referência Cruzada: {resultado.referencia_cruzada}")
    # Imprime a recomendação
    print(f"Recomendação: {resultado.recomendacao}")
    # Imprime linha separadora
    print("-" * 60)

# Bloco principal para testes
if __name__ == "__main__":
    # Cria instância de PVPEvaluator
    avaliador = VPAEvaluator()

    # Teste 1: Avaliação automática com P/VP = 1.2
    # Avalia o valor P/VP 1.2
    resultado_avaliacao = avaliador.avaliar(1.2)
    # Imprime cabeçalho do teste
    print("🔍 Teste de avaliação automática:")
    # Imprime o objeto ResultadoIND
    print(resultado_avaliacao)
    # Imprime a representação em dicionário
    print(resultado_avaliacao.to_dict())
    # Imprime linha em branco
    print()

    # Teste 2: Geração manual de resultado
    # Gera ResultadoIND com entradas manuais
    resultado_manual = avaliador.gerar_resultado(
        classificacao='Teste',
        faixa='1.0 - 2.0',
        descricao='Exemplo de uso externo',
        riscos='Risco moderado',
        referencia='Referência fictícia',
        recomendacao='Recomendação de teste'
    )
    # Imprime cabeçalho do teste
    print("🧪 Teste de geração manual de resultado:")
    # Imprime o objeto ResultadoIND
    print(resultado_manual)
    # Imprime a representação em dicionário
    print(resultado_manual.to_dict())
    # Imprime linha em branco
    print()

    # Teste 3: Simulação de erro
    # Avalia entrada inválida para disparar erro
    resultado_erro = avaliador.avaliar("valor_invalido")
    # Imprime cabeçalho do teste
    print("⚠️ Teste de erro:")
    # Imprime o ResultadoIND de erro
    print(resultado_erro)
    # Imprime a representação em dicionário
    print(resultado_erro.to_dict())
    # Imprime linha em branco
    print()

    # Teste adicional: Exibição formatada
    # Define valor de teste P/VP
    valor_pvp = 1.2
    # Avalia o valor P/VP
    resultado = avaliador.avaliar(valor_pvp)
    # Exibe resultado formatado
    exibir_resultado(resultado)
    # Imprime cabeçalho do dicionário
    print("📦 Resultado como dicionário:")
    # Converte resultado em dicionário e imprime
    print(resultado.to_dict())