# Define a classe ROEEvaluator, que é responsável por avaliar o indicador financeiro conhecido como ROE (Retorno sobre Patrimônio Líquido).
# Essa classe encapsula a lógica para calcular, classificar e fornecer análises detalhadas sobre o ROE de uma empresa,
# ajudando investidores a entender a eficiência da empresa em gerar lucros a partir do capital próprio dos acionistas.
class ROEEvaluator:

    # Método construtor da classe, chamado automaticamente ao instanciar um objeto ROEEvaluator.
    # Ele inicializa atributos fixos da classe: a definição do ROE, o agrupador de categoria e a fórmula de cálculo.
    # Esses atributos são comuns a todas as avaliações e não mudam durante a execução.
    def __init__(self):
        # Atribui uma string multilinha à variável 'definicao'. Essa string fornece uma explicação detalhada do que é o ROE,
        # incluindo sua fórmula de cálculo ((Lucro Líquido / Patrimônio Líquido) * 100), seu propósito como indicador de eficiência,
        # e interpretações de valores altos (eficiência alta) versus baixos ou negativos (ineficiência ou prejuízos).
        # A string usa aspas triplas para permitir quebras de linha, tornando-a mais legível.
        self.definicao = '''
        O ROE (Retorno sobre Patrimônio Líquido) mede a rentabilidade da empresa em relação ao capital próprio dos acionistas, calculado
        como (Lucro Líquido / Patrimônio Líquido) * 100. É um indicador de eficiência que avalia a capacidade da empresa de gerar lucros
        com o patrimônio investido pelos acionistas. Um ROE alto sugere alta eficiência, enquanto valores baixos ou negativos indicam ineficiência ou prejuízos.
        '''

        # Atribui a string 'Rentabilidade' ao atributo 'agrupador'. Isso categoriza o ROE dentro de um grupo de indicadores financeiros
        # relacionados à rentabilidade, facilitando a organização em relatórios ou dashboards de análise financeira.
        self.agrupador = 'Rentabilidade'

        # Atribui a fórmula do ROE como uma string ao atributo 'formula'. Essa string representa a expressão matemática exata
        # para calcular o ROE, servindo como referência para usuários ou para exibição em resultados.
        self.formula = 'ROE (%) = (Lucro Líquido / Patrimônio Líquido) * 100'

    # Aqui começa a definição do decorator 'validar_strings'.
    # Essa é a função externa do decorator. Ela recebe como argumento a função que será decorada (no caso, 'gerar_resultado').
    # Note que 'funcao' é um parâmetro que representa a função original a ser modificada.
    def validar_strings(funcao):

        # Dentro do decorator, definimos a função interna 'wrapper' (embrulhadora).
        # Essa é a função que será executada no lugar da original quando chamarmos o método decorado.
        # Ela recebe 'self' (a instância da classe, pois é um método de classe) e os mesmos argumentos da função original.
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):

            # Aqui começa a lógica de validação adicionada pelo decorator.
            # Criamos uma lista de tuplas, cada uma contendo um parâmetro e seu nome correspondente.
            # Isso permite uma iteração genérica sobre todos os argumentos, evitando repetir código para cada um.
            # Exemplo: Se classificacao="Crítico", a tupla será ("Crítico", "classificacao").
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia"),
                (recomendacao, "recomendacao")
            ]:

                # Para cada parâmetro, verificamos duas condições:
                # 1. Se NÃO é uma instância de string (usando isinstance(param, str)).
                # 2. OU se, mesmo sendo string, após remover espaços em branco com strip(), fica vazia (not param.strip()).
                # Se qualquer uma for verdadeira, o parâmetro é inválido.
                # Exemplo: Se classificacao=123 (inteiro), isinstance(123, str) é False → erro.
                # Se classificacao="   " (só espaços), strip() resulta em "" vazio → erro.
                # Se classificacao="Crítico", passa (é string e não vazia após strip).
                if not isinstance(param, str) or not param.strip():
                    # Levanta uma exceção ValueError com uma mensagem personalizada, incluindo o nome do parâmetro problemático.
                    # Isso para a execução e informa o usuário exatamente qual argumento falhou.
                    # Exemplo de erro: ValueError("O parâmetro 'classificacao' deve ser uma string não vazia.")
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")

            # Se TODOS os parâmetros passarem na validação (nenhuma exceção levantada),
            # o wrapper chama a função original ('funcao') com os mesmos argumentos.
            # Isso executa o código real de 'gerar_resultado', passando 'self' e os params validados.
            # O retorno da função original é então retornado pelo wrapper, como se nada tivesse mudado.
            # Exemplo: Se tudo ok, executa gerar_resultado(...) e retorna o ResultadoIND.
            return funcao(self, classificacao, faixa, descricao, riscos, referencia, recomendacao)

        # Após definir o wrapper, o decorator retorna ESSA função wrapper.
        # Isso é o que "substitui" a função original na definição da classe.
        # Quando Python vê @validar_strings sobre gerar_resultado, ele faz: gerar_resultado = validar_strings(gerar_resultado)
        return wrapper

    # Método principal para avaliar o valor do ROE. Recebe um parâmetro 'roe' que pode ser int, float ou string numérica.
    # Ele classifica o ROE em faixas predefinidas e retorna um objeto ResultadoIND com análise detalhada.
    # Usa um bloco try-except para lidar com entradas inválidas de forma graciosa.
    def avaliar(self, roe):
        # Inicia um bloco try para capturar exceções durante o processamento do ROE.
        try:
            # Verifica se 'roe' não é int/float E não é uma string que pode ser convertida para float (removendo no máximo um ponto decimal).
            # Se não for numérico válido, levanta ValueError para indicar que a entrada deve ser numérica.
            if not isinstance(roe, (int, float)) and not (isinstance(roe, str) and roe.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do ROE deve ser numérico.")
            # Converte explicitamente 'roe' para float, garantindo que o valor seja numérico para comparações subsequentes.
            roe = float(roe)
            # Inicia uma série de condições if-elif para classificar o ROE em faixas baseadas em seu valor.
            # Primeira condição: Se ROE for negativo (< 0), indica problemas graves como prejuízos ou patrimônio negativo.
            if roe < 0:
                # Chama o método 'gerar_resultado' com parâmetros específicos para ROE negativo, incluindo classificação 'Crítico',
                # descrição detalhada dos motivos, riscos associados, referências a outros indicadores e recomendações.
                # Isso retorna um objeto ResultadoIND personalizado para essa faixa.
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='ROE < 0%',
                    descricao='Um ROE negativo indica que a empresa está gerando prejuízo líquido ou possui patrimônio líquido negativo, sugerindo ineficiência grave ou problemas estruturais. Isso pode ocorrer em empresas em crise, com perdas acumuladas ou alta alavancagem, apontando para instabilidade financeira.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver endividamento excessivo ou incapacidade de gerar lucros sustentáveis.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_div_liquida_pl para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação de lucros ou estabilização do patrimônio. Priorize análise de turnaround e saúde financeira.'
                )
            # Segunda condição: Se ROE estiver entre 0 e 5 (inclusive), indica rentabilidade muito baixa.
            elif 0 <= roe <= 5:
                # Similar ao anterior, chama 'gerar_resultado' com parâmetros adaptados para essa faixa baixa,
                # descrevendo contextos comuns (setores com margens apertadas), riscos e recomendações.
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= ROE <= 5%',
                    descricao='O ROE está muito baixo, sugerindo rentabilidade limitada sobre o patrimônio dos acionistas. Isso é comum em setores com margens apertadas, alta concorrência ou baixa eficiência operacional, como varejo ou indústrias de commodities, onde os lucros são insuficientes para remunerar o capital investido.',
                    riscos='Risco de baixa atratividade para investidores devido a retornos insuficientes. Pode haver dependência de fatores externos ou incapacidade de reinvestir lucros de forma eficaz.',
                    referencia='Analise evaluate_margem_ebit para eficiência operacional, evaluate_p_l para lucros e evaluate_debt_to_equity para estrutura de capital.',
                    recomendacao='Considere investir apenas se houver planos claros para melhoria de lucros ou eficiência. Verifique tendências de mercado e estratégias de crescimento.'
                )
            # Terceira condição: Se ROE estiver entre 5 (exclusivo) e 15 (inclusive), indica rentabilidade moderada.
            elif 5 < roe <= 15:
                # Chama 'gerar_resultado' com detalhes para faixa moderada, enfatizando estabilidade mas sem alta eficiência.
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5 < ROE <= 15%',
                    descricao='O ROE está em uma faixa moderada, indicando rentabilidade razoável sobre o patrimônio líquido. Essa faixa é comum em empresas com operações estáveis, mas sem alta eficiência, como manufatura ou serviços com margens moderadas, refletindo um equilíbrio entre lucros e capital próprio.',
                    riscos='Risco de estagnação nos lucros devido a concorrência ou custos crescentes. Pode haver limitações em financiar crescimento sem aumentar a alavancagem.',
                    referencia='Compare com evaluate_margem_liquida para eficiência final, evaluate_p_vp para valuation patrimonial e evaluate_market_share para competitividade.',
                    recomendacao='Avalie o histórico de lucros e estratégias de crescimento antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade com retorno moderado.'
                )
            # Quarta condição: Se ROE estiver entre 15 (exclusivo) e 25 (inclusive), indica boa rentabilidade.
            elif 15 < roe <= 25:
                # Chama 'gerar_resultado' para faixa boa, destacando eficiência operacional forte.
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='15 < ROE <= 25%',
                    descricao='O ROE está em uma faixa alta, sugerindo boa rentabilidade sobre o patrimônio líquido. Essa faixa é comum em empresas com forte eficiência operacional, poder de precificação ou operações otimizadas, como tecnologia ou bens de consumo de marca, indicando capacidade de gerar retornos robustos.',
                    riscos='Risco de dependência de mercados premium ou alta alavancagem para impulsionar o ROE. Pode haver volatilidade se os lucros não forem sustentáveis.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade dos lucros e o nível de endividamento da empresa.'
                )
            # Quinta condição: Se ROE for maior que 25, indica rentabilidade excepcional.
            elif roe > 25:
                # Chama 'gerar_resultado' para faixa ótima, alertando sobre possíveis riscos de sustentabilidade.
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='ROE > 25%',
                    descricao='O ROE é extremamente alto, indicando rentabilidade excepcional sobre o patrimônio líquido. Essa faixa é típica de empresas com modelos de negócios escaláveis, baixa concorrência ou marcas premium, como software ou bens de luxo, refletindo eficiência superior e forte retorno para acionistas.',
                    riscos='Risco de sobredependência de nichos de mercado ou alavancagem excessiva para inflar o ROE. Mudanças regulatórias ou entrada de concorrentes podem impactar lucros.',
                    referencia='Combine com evaluate_psr para receita, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem lucros sustentáveis, mas diversifique para mitigar riscos de concentração ou mudanças de mercado.'
                )
        # Bloco except para capturar qualquer exceção (como ValueError de conversão ou outras inesperadas).
        # Chama o método privado '_erro' passando a mensagem da exceção para criar um resultado de erro.
        except Exception as e:
            return self._erro(mensagem=str(e))

    # Aplica o decorator 'validar_strings' ao método 'gerar_resultado'. Isso garante que todos os argumentos sejam strings não vazias
    # antes de prosseguir com a criação do objeto ResultadoIND.
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia, recomendacao):
        # Este é o código original do método. Ele só executa SE o wrapper validar tudo.
        # Cria e retorna uma instância da classe ResultadoIND (assumidamente definida em outro lugar do código),
        # passando os parâmetros validados e os atributos fixos da instância (definicao, agrupador, formula).
        # Isso encapsula todos os dados de análise em um objeto estruturado para fácil uso ou exibição.
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

    # Método privado (indicado pelo underscore inicial) para tratar erros. Recebe uma mensagem de erro e cria um objeto ResultadoIND
    # com classificação 'Erro' e campos preenchidos com informações sobre o erro, usando 'N/A' para campos irrelevantes.
    # Isso permite que erros sejam tratados de forma consistente, retornando um objeto similar aos resultados normais.
    def _erro(self, mensagem):
        return ResultadoIND(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o ROE: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )