# Define a classe TagAlongEvaluator para avaliar o indicador Tag Along
class TagAlongEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do Tag Along
    def __init__(self):
        # Define string multilinha explicando o índice Tag Along
        self.definicao = '''
        O Tag Along é um mecanismo de proteção aos acionistas minoritários que garante o direito de vender suas ações nas mesmas condições
        (preço e termos) oferecidas ao controlador em caso de venda do controle acionário. Expresso como percentual do preço pago por ação ao
        controlador, é previsto no estatuto da empresa ou na legislação (ex.: Lei das S.A. no Brasil, que exige 80% para empresas listadas em
        alguns segmentos). Um Tag Along alto reflete maior proteção aos minoritários, enquanto um Tag Along baixo ou inexistente indica maior risco.
        '''
        # Define a categoria de agrupamento como "Governança Corporativa"
        self.agrupador = 'Governança Corporativa'
        # Define a fórmula do Tag Along
        self.formula = '''
        Tag Along (%) = Percentual do preço por ação pago ao controlador garantido aos minoritários
        Observação: O Tag Along é uma informação estatutária ou regulatória, geralmente definida como 0%, 80%, 100% ou outro percentual específico.
        '''

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

    # Valida o percentual de Tag Along
    def validar_tag_along(self, tag_along):
        try:
            # Verifica se o Tag Along é numérico
            if not isinstance(tag_along, (int, float)) and not (isinstance(tag_along, str) and tag_along.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do Tag Along deve ser numérico.")
            # Converte para float
            tag_along = float(tag_along)
            # Verifica se o Tag Along está entre 0% e 100%
            if tag_along < 0 or tag_along > 100:
                raise ValueError("O Tag Along deve estar entre 0% e 100%.")
            return tag_along
        except Exception as e:
            raise ValueError(f"Erro ao validar o Tag Along: {str(e)}")

    # Avalia o valor do Tag Along e retorna um objeto ResultadoIND
    def avaliar(self, tag_along):
        # Tenta processar a avaliação do Tag Along
        try:
            # Valida o Tag Along
            tag_along = self.validar_tag_along(tag_along)
            # Verifica se Tag Along é 0%, indicando ausência de proteção
            if tag_along == 0:
                # Retorna ResultadoIND para ausência de Tag Along
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Tag Along = 0%',
                    descricao='A ausência de Tag Along indica nenhuma proteção aos acionistas minoritários em caso de venda do controle acionário. Comum em empresas com baixa governança ou fora de segmentos regulados, sugere alto risco para investidores minoritários.',
                    riscos='Risco de perda significativa em cenários de venda de controle, com minoritários recebendo preços inferiores ou nenhum pagamento. Pode indicar má governança corporativa.',
                    referencia='Avalie evaluate_free_float para liquidez, evaluate_div_liquida_pl para alavancagem e evaluate_roe para rentabilidade.',
                    recomendacao='Evite investir devido à falta de proteção aos minoritários. Priorize empresas com melhores práticas de governança.'
                )
            # Verifica se Tag Along está entre 1% e 79%, indicando proteção parcial insuficiente
            elif 1 <= tag_along < 80:
                # Retorna ResultadoIND para proteção parcial insuficiente
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='1% <= Tag Along < 80%',
                    descricao='O Tag Along oferece proteção parcial, mas abaixo do padrão de mercado (ex.: 80% exigido pela B3 para o Novo Mercado). Sugere proteção limitada aos minoritários, com risco de desvalorização em caso de venda de controle.',
                    riscos='Risco de receber preços significativamente inferiores em uma venda de controle. Pode indicar governança corporativa fraca ou controle concentrado.',
                    referencia='Compare com evaluate_free_float para liquidez, evaluate_beta para risco e evaluate_p_vpa para valuation.',
                    recomendacao='Considere investir com cautela, priorizando empresas com Tag Along mais alto ou melhores práticas de governança.'
                )
            # Verifica se Tag Along está entre 80% e 99%, indicando proteção padrão
            elif 80 <= tag_along <= 99:
                # Retorna ResultadoIND para proteção padrão
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='80% <= Tag Along <= 99%',
                    descricao='O Tag Along oferece proteção padrão aos minoritários, alinhado com exigências de mercados como o Novo Mercado da B3. Comum em empresas com governança sólida, sugere segurança razoável em cenários de venda de controle.',
                    riscos='Risco de proteção não total, com possíveis diferenças nos termos oferecidos aos minoritários. Pode haver dependência de outros fatores de governança.',
                    referencia='Analise evaluate_free_float para liquidez, evaluate_p_ebitda para valuation e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir, mas avalie outros aspectos de governança e liquidez. Boa opção para investidores moderados.'
                )
            # Verifica se Tag Along é 100%, indicando proteção total
            elif tag_along == 100:
                # Retorna ResultadoIND para proteção total
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Tag Along = 100%',
                    descricao='O Tag Along de 100% oferece proteção total aos acionistas minoritários, garantindo as mesmas condições do controlador em uma venda de controle. Típico de empresas com governança exemplar, sugere alta segurança para investidores minoritários.',
                    riscos='Risco mínimo relacionado ao Tag Along, mas outros fatores de governança ou mercado podem impactar o investimento.',
                    referencia='Verifique evaluate_free_float para liquidez, evaluate_fcd para valuation e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, especialmente para portfólios que valorizam governança sólida. Boa opção para investidores que buscam segurança.'
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
                Ocorreu um erro ao processar o Tag Along: {mensagem}.
                Verifique o dado de entrada (percentual de Tag Along) e assegure que seja um valor numérico válido entre 0% e 100%.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe FreeFloatEvaluator para avaliar o indicador Free Float
class FreeFloatEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do Free Float
    def __init__(self):
        # Define string multilinha explicando o índice Free Float
        self.definicao = '''
        O Free Float é a proporção de ações de uma empresa disponíveis para negociação pública no mercado, excluindo ações detidas por
        controladores, acionistas estratégicos, diretores ou bloqueadas (ex.: lock-up). Expresso em percentual, é um indicador de liquidez
        de mercado, refletindo a facilidade de compra e venda da ação. Um Free Float alto sugere maior liquidez e atratividade para investidores,
        enquanto um Free Float baixo indica menor negociação e maior controle por poucos acionistas, podendo limitar a volatilidade ou o interesse.
        '''
        # Define a categoria de agrupamento como "Liquidez de Mercado"
        self.agrupador = 'Liquidez de Mercado'
        # Define a fórmula do Free Float
        self.formula = '''
        Free Float (%) = (Ações em Circulação - Ações Restritas) / Total de Ações × 100
        Onde:
        - Ações em Circulação: Total de ações emitidas disponíveis no mercado
        - Ações Restritas: Ações detidas por controladores, insiders ou bloqueadas
        - Total de Ações: Soma de todas as ações emitidas pela empresa
        '''

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


    # Avalia o valor do Free Float e retorna um objeto ResultadoIND
    def avaliar(self, total_acoes):
        # Tenta processar o cálculo do Free Float e a avaliação
        try:
            # Calcula o Free Float
            free_float = self. total_acoes
            # Verifica se Free Float é menor que 0%, indicando erro nos dados
            if free_float < 0:
                # Retorna ResultadoIND para Free Float inválido
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Free Float < 0%',
                    descricao='Um Free Float negativo é inválido e indica erro nos dados de entrada, como ações restritas maiores que as ações em circulação. Isso compromete a análise de liquidez da ação.',
                    riscos='Risco de dados inconsistentes ou má estrutura acionária. Pode haver dificuldades em avaliar a liquidez de mercado.',
                    referencia='Avalie evaluate_liquidez_media_diaria para liquidez, evaluate_beta para risco e evaluate_p_vpa para valuation.',
                    recomendacao='Revise os dados de entrada antes de prosseguir com a análise. Evite decisões de investimento até corrigir os dados.'
                )
            # Verifica se Free Float está entre 0 e 20%, indicando baixa liquidez
            elif 0 <= free_float < 20:
                # Retorna ResultadoIND para baixa liquidez
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Free Float < 20%',
                    descricao='O Free Float é baixo, indicando liquidez limitada no mercado. Comum em empresas com forte controle acionário ou pequena capitalização, sugere dificuldade para negociar grandes volumes e menor atratividade para investidores institucionais.',
                    riscos='Risco de baixa liquidez, dificultando entrada e saída de posições. Pode haver maior volatilidade em preços ou manipulação por poucos acionistas.',
                    referencia='Compare com evaluate_liquidez_media_diaria para liquidez, evaluate_beta para risco e evaluate_div_liquida_pl para alavancagem.',
                    recomendacao='Evite investir devido à baixa liquidez, a menos que tolere riscos elevados. Priorize empresas com maior Free Float ou volume de negociação.'
                )
            # Verifica se Free Float está entre 20% e 50%, indicando liquidez moderada
            elif 20 <= free_float <= 50:
                # Retorna ResultadoIND para liquidez moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='20 <= Free Float <= 50%',
                    descricao='O Free Float indica liquidez moderada, típico de empresas com equilíbrio entre controle acionário e negociação pública. Sugere capacidade razoável de negociação, mas pode não atrair grandes investidores institucionais.',
                    riscos='Risco de volatilidade moderada ou dificuldade em negociar grandes volumes. Pode haver influência de acionistas controladores nas decisões.',
                    referencia='Analise evaluate_liquidez_media_diaria para liquidez, evaluate_p_ebitda para valuation e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas avalie o volume de negociação e a governança corporativa. Boa opção para investidores moderados.'
                )
            # Verifica se Free Float está entre 50% e 80%, indicando alta liquidez
            elif 50 < free_float <= 80:
                # Retorna ResultadoIND para alta liquidez
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='50 < Free Float <= 80%',
                    descricao='O Free Float é alto, indicando boa liquidez no mercado. Comum em empresas bem estabelecidas ou de grande capitalização, sugere facilidade de negociação e atratividade para investidores institucionais.',
                    riscos='Risco de maior exposição a flutuações de mercado devido à alta negociação. Pode haver menor controle acionário, impactando decisões estratégicas.',
                    referencia='Verifique evaluate_beta para risco, evaluate_fcd para valuation e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir, especialmente para portfólios diversificados. Boa opção para investidores que buscam liquidez e estabilidade.'
                )
            # Verifica se Free Float excede 80%, indicando liquidez excepcional
            elif free_float > 80:
                # Retorna ResultadoIND para liquidez excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Free Float > 80%',
                    descricao='O Free Float é extremamente alto, indicando liquidez excepcional. Típico de empresas de grande capitalização ou com ampla dispersão acionária, sugere alta facilidade de negociação e forte interesse de investidores institucionais.',
                    riscos='Risco de alta volatilidade em cenários de mercado turbulentos. Pode haver menor influência de acionistas estratégicos, afetando a governança.',
                    referencia='Avalie evaluate_liquidez_media_diaria para liquidez, evaluate_wacc para custo de capital e evaluate_p_vpa para valuation.',
                    recomendacao='Considere investir, mas diversifique para mitigar riscos de mercado. Priorize empresas com fundamentos sólidos e boa governança.'
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
                Ocorreu um erro ao processar o Free Float: {mensagem}.
                Verifique os dados de entrada (ações em circulação, ações restritas, total de ações) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe FreeFloatEvaluator para avaliar o indicador Free Float
class FreeFloatEvaluatororiginal:
    # Construtor que inicializa definição, agrupador e descrição do Free Float
    def __init__(self):
        # Define string multilinha explicando o índice Free Float
        self.definicao = '''
        O Free Float é a proporção de ações de uma empresa disponíveis para negociação pública no mercado, excluindo ações detidas por
        controladores, acionistas estratégicos, diretores ou bloqueadas (ex.: lock-up). Expresso em percentual, é um indicador de liquidez
        de mercado, refletindo a facilidade de compra e venda da ação. Um Free Float alto sugere maior liquidez e atratividade para investidores,
        enquanto um Free Float baixo indica menor negociação e maior controle por poucos acionistas, podendo limitar a volatilidade ou o interesse.
        '''
        # Define a categoria de agrupamento como "Liquidez de Mercado"
        self.agrupador = 'Liquidez de Mercado'
        # Define a fórmula do Free Float
        self.formula = '''
        Free Float (%) = (Ações em Circulação - Ações Restritas) / Total de Ações × 100
        Onde:
        - Ações em Circulação: Total de ações emitidas disponíveis no mercado
        - Ações Restritas: Ações detidas por controladores, insiders ou bloqueadas
        - Total de Ações: Soma de todas as ações emitidas pela empresa
        '''

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

    # Calcula o Free Float com base no número de ações
    def calcular_free_float(self, acoes_em_circulacao, acoes_restritas, total_acoes):
        try:
            # Verifica se as entradas são numéricas
            for param, nome in [
                (acoes_em_circulacao, "Ações em Circulação"),
                (acoes_restritas, "Ações Restritas"),
                (total_acoes, "Total de Ações")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte parâmetros para float
            acoes_em_circulacao = float(acoes_em_circulacao)
            acoes_restritas = float(acoes_restritas)
            total_acoes = float(total_acoes)
            # Verifica se o total de ações é maior que zero
            if total_acoes <= 0:
                raise ValueError("O total de ações deve ser maior que zero.")
            # Verifica se as ações restritas são menores ou iguais às ações em circulação
            if acoes_restritas > acoes_em_circulacao:
                raise ValueError("As ações restritas não podem exceder as ações em circulação.")
            # Calcula o Free Float
            free_float = ((acoes_em_circulacao - acoes_restritas) / total_acoes) * 100
            return free_float
        except Exception as e:
            raise ValueError(f"Erro ao calcular o Free Float: {str(e)}")

    # Avalia o valor do Free Float e retorna um objeto ResultadoIND
    def avaliar(self, acoes_em_circulacao, acoes_restritas, total_acoes):
        # Tenta processar o cálculo do Free Float e a avaliação
        try:
            # Calcula o Free Float
            free_float = self.calcular_free_float(acoes_em_circulacao, acoes_restritas, total_acoes)
            # Verifica se Free Float é menor que 0%, indicando erro nos dados
            if free_float < 0:
                # Retorna ResultadoIND para Free Float inválido
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Free Float < 0%',
                    descricao='Um Free Float negativo é inválido e indica erro nos dados de entrada, como ações restritas maiores que as ações em circulação. Isso compromete a análise de liquidez da ação.',
                    riscos='Risco de dados inconsistentes ou má estrutura acionária. Pode haver dificuldades em avaliar a liquidez de mercado.',
                    referencia='Avalie evaluate_liquidez_media_diaria para liquidez, evaluate_beta para risco e evaluate_p_vpa para valuation.',
                    recomendacao='Revise os dados de entrada antes de prosseguir com a análise. Evite decisões de investimento até corrigir os dados.'
                )
            # Verifica se Free Float está entre 0 e 20%, indicando baixa liquidez
            elif 0 <= free_float < 20:
                # Retorna ResultadoIND para baixa liquidez
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Free Float < 20%',
                    descricao='O Free Float é baixo, indicando liquidez limitada no mercado. Comum em empresas com forte controle acionário ou pequena capitalização, sugere dificuldade para negociar grandes volumes e menor atratividade para investidores institucionais.',
                    riscos='Risco de baixa liquidez, dificultando entrada e saída de posições. Pode haver maior volatilidade em preços ou manipulação por poucos acionistas.',
                    referencia='Compare com evaluate_liquidez_media_diaria para liquidez, evaluate_beta para risco e evaluate_div_liquida_pl para alavancagem.',
                    recomendacao='Evite investir devido à baixa liquidez, a menos que tolere riscos elevados. Priorize empresas com maior Free Float ou volume de negociação.'
                )
            # Verifica se Free Float está entre 20% e 50%, indicando liquidez moderada
            elif 20 <= free_float <= 50:
                # Retorna ResultadoIND para liquidez moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='20 <= Free Float <= 50%',
                    descricao='O Free Float indica liquidez moderada, típico de empresas com equilíbrio entre controle acionário e negociação pública. Sugere capacidade razoável de negociação, mas pode não atrair grandes investidores institucionais.',
                    riscos='Risco de volatilidade moderada ou dificuldade em negociar grandes volumes. Pode haver influência de acionistas controladores nas decisões.',
                    referencia='Analise evaluate_liquidez_media_diaria para liquidez, evaluate_p_ebitda para valuation e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas avalie o volume de negociação e a governança corporativa. Boa opção para investidores moderados.'
                )
            # Verifica se Free Float está entre 50% e 80%, indicando alta liquidez
            elif 50 < free_float <= 80:
                # Retorna ResultadoIND para alta liquidez
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='50 < Free Float <= 80%',
                    descricao='O Free Float é alto, indicando boa liquidez no mercado. Comum em empresas bem estabelecidas ou de grande capitalização, sugere facilidade de negociação e atratividade para investidores institucionais.',
                    riscos='Risco de maior exposição a flutuações de mercado devido à alta negociação. Pode haver menor controle acionário, impactando decisões estratégicas.',
                    referencia='Verifique evaluate_beta para risco, evaluate_fcd para valuation e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir, especialmente para portfólios diversificados. Boa opção para investidores que buscam liquidez e estabilidade.'
                )
            # Verifica se Free Float excede 80%, indicando liquidez excepcional
            elif free_float > 80:
                # Retorna ResultadoIND para liquidez excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Free Float > 80%',
                    descricao='O Free Float é extremamente alto, indicando liquidez excepcional. Típico de empresas de grande capitalização ou com ampla dispersão acionária, sugere alta facilidade de negociação e forte interesse de investidores institucionais.',
                    riscos='Risco de alta volatilidade em cenários de mercado turbulentos. Pode haver menor influência de acionistas estratégicos, afetando a governança.',
                    referencia='Avalie evaluate_liquidez_media_diaria para liquidez, evaluate_wacc para custo de capital e evaluate_p_vpa para valuation.',
                    recomendacao='Considere investir, mas diversifique para mitigar riscos de mercado. Priorize empresas com fundamentos sólidos e boa governança.'
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
                Ocorreu um erro ao processar o Free Float: {mensagem}.
                Verifique os dados de entrada (ações em circulação, ações restritas, total de ações) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe CAGRLucrosEvaluator para avaliar o indicador CAGR de Lucros 5 Anos
class CAGRLucrosEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do CAGR de Lucros
    def __init__(self):
        # Define string multilinha explicando o índice CAGR de Lucros
        self.definicao = '''
        O CAGR (Compound Annual Growth Rate) de Lucros 5 Anos é a taxa média de crescimento anual do lucro líquido de uma empresa ao longo de cinco anos,
        considerando o efeito da capitalização composta. Ele suaviza flutuações anuais, fornecendo uma visão estável do crescimento da lucratividade.
        É amplamente utilizado para avaliar a consistência do crescimento dos lucros, comparar desempenho entre empresas e projetar resultados futuros.
        Um CAGR alto indica crescimento robusto dos lucros, enquanto um CAGR baixo ou negativo sugere estagnação ou declínio na lucratividade.
        '''
        # Define a categoria de agrupamento como "Crescimento"
        self.agrupador = 'Crescimento'
        # Define a fórmula do CAGR
        self.formula = '''
        CAGR = (VF / VI)^(1/n) - 1
        Onde:
        - VF = Valor Final do lucro líquido (ao final do período de 5 anos)
        - VI = Valor Inicial do lucro líquido (no início do período de 5 anos)
        - n = Número de anos (neste caso, 5)
        '''

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

    # Calcula o CAGR com base nos valores inicial e final dos lucros
    def calcular_cagr(self, valor_inicial, valor_final, anos=5):
        try:
            # Verifica se as entradas são numéricas
            for param, nome in [
                (valor_inicial, "Valor Inicial do Lucro Líquido"),
                (valor_final, "Valor Final do Lucro Líquido"),
                (anos, "Número de Anos")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte parâmetros para float
            valor_inicial = float(valor_inicial)
            valor_final = float(valor_final)
            anos = float(anos)
            # Verifica se o valor inicial é maior que zero
            if valor_inicial <= 0:
                raise ValueError("O valor inicial do lucro líquido deve ser maior que zero.")
            # Verifica se o número de anos é positivo
            if anos <= 0:
                raise ValueError("O número de anos deve ser maior que zero.")
            # Calcula o CAGR
            cagr = (valor_final / valor_inicial) ** (1 / anos) - 1
            return cagr
        except Exception as e:
            raise ValueError(f"Erro ao calcular o CAGR: {str(e)}")

    # Avalia o valor do CAGR de Lucros e retorna um objeto ResultadoIND
    def avaliar(self, valor_inicial, valor_final, anos=5):
        # Tenta processar o cálculo do CAGR e a avaliação
        try:
            # Calcula o CAGR
            cagr = self.calcular_cagr(valor_inicial, valor_final, anos)
            # Verifica se CAGR é negativo, indicando declínio nos lucros
            if cagr < 0:
                # Retorna ResultadoIND para CAGR negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='CAGR < 0%',
                    descricao='Um CAGR negativo indica declínio nos lucros líquidos ao longo dos cinco anos. Isso sugere dificuldades operacionais, aumento de custos ou perda de mercado, comprometendo a saúde financeira da empresa.',
                    riscos='Risco de insustentabilidade financeira, erosão de valor para acionistas ou necessidade de reestruturação. Pode haver dependência de fatores externos adversos.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_div_liquida_ebitda para alavancagem e evaluate_fcf para geração de caixa.',
                    recomendacao='Evite investir devido ao declínio nos lucros. Priorize análise de causas do declínio e estratégias de recuperação.'
                )
            # Verifica se CAGR está entre 0 e 5%, indicando crescimento baixo
            elif 0 <= cagr <= 0.05:
                # Retorna ResultadoIND para crescimento baixo
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= CAGR <= 5%',
                    descricao='O CAGR indica crescimento baixo dos lucros líquidos, comum em setores maduros ou empresas com desafios de lucratividade. Sugere estabilidade, mas limitada capacidade de expansão dos lucros.',
                    riscos='Risco de estagnação ou pressão sobre margens em setores competitivos. Pode haver dependência de melhorias operacionais para sustentar lucros.',
                    referencia='Compare com evaluate_margem_ebitda para lucratividade, evaluate_roe para rentabilidade e evaluate_p_l para valuation.',
                    recomendacao='Considere investir com cautela, priorizando empresas com margens sólidas ou potencial de melhoria operacional. Avalie o contexto setorial.'
                )
            # Verifica se CAGR está entre 5% e 10%, indicando crescimento moderado
            elif 0.05 < cagr <= 0.10:
                # Retorna ResultadoIND para crescimento moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5% < CAGR <= 10%',
                    descricao='O CAGR indica crescimento moderado dos lucros líquidos, típico de empresas em setores estáveis ou em consolidação. Sugere equilíbrio entre crescimento e estabilidade, com potencial para ganhos consistentes.',
                    riscos='Risco de competição setorial ou necessidade de investimentos para manter o crescimento. Pode haver sensibilidade a custos ou mudanças econômicas.',
                    referencia='Analise evaluate_fcd para valuation, evaluate_liquidez_corrente para liquidez e evaluate_margem_bruta para eficiência.',
                    recomendacao='Considere investir, especialmente se a empresa apresentar margens sólidas e boa gestão. Boa opção para investidores moderados.'
                )
            # Verifica se CAGR está entre 10% e 20%, indicando crescimento alto
            elif 0.10 < cagr <= 0.20:
                # Retorna ResultadoIND para crescimento alto
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10% < CAGR <= 20%',
                    descricao='O CAGR indica crescimento alto dos lucros líquidos, comum em empresas em setores dinâmicos, como tecnologia ou varejo em expansão. Sugere forte capacidade de crescimento e atratividade para investidores.',
                    riscos='Risco de volatilidade em setores competitivos ou dependência de condições econômicas favoráveis. Pode haver necessidade de capital para expansão.',
                    referencia='Verifique evaluate_p_ebitda para valuation, evaluate_fcf para geração de caixa e evaluate_beta para risco.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade do crescimento e a alavancagem financeira. Boa opção para investidores tolerantes a risco.'
                )
            # Verifica se CAGR excede 20%, indicando crescimento excepcional
            elif cagr > 0.20:
                # Retorna ResultadoIND para crescimento excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='CAGR > 20%',
                    descricao='O CAGR indica crescimento excepcional dos lucros líquidos, típico de empresas em setores de alto crescimento, como tecnologia ou startups. Sugere forte potencial de valorização, mas pode vir acompanhado de maior volatilidade.',
                    riscos='Risco de crescimento insustentável ou dependência de aportes de capital. Pode haver volatilidade significativa em setores de alto crescimento.',
                    referencia='Avalie evaluate_wacc para custo de capital, evaluate_div_liquida_pl para alavancagem e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir, mas diversifique para mitigar riscos. Priorize empresas com fundamentos sólidos e geração de caixa.'
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
                Ocorreu um erro ao processar o CAGR de Lucros: {mensagem}.
                Verifique os dados de entrada (valor inicial, valor final, número de anos) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe CAGREvaluator para avaliar o indicador CAGR de Receitas 5 Anos
class CAGREvaluator:
    # Construtor que inicializa definição, agrupador e descrição do CAGR
    def __init__(self):
        # Define string multilinha explicando o índice CAGR de Receitas
        self.definicao = '''
        O CAGR (Compound Annual Growth Rate) de Receitas 5 Anos é a taxa média de crescimento anual das receitas de uma empresa ao longo de cinco anos,
        considerando o efeito da capitalização composta. Ele suaviza flutuações anuais, fornecendo uma visão estável do crescimento do faturamento.
        É amplamente utilizado para avaliar a consistência do crescimento da empresa, comparar desempenho entre empresas e projetar resultados futuros.
        Um CAGR alto indica crescimento robusto, enquanto um CAGR baixo ou negativo sugere estagnação ou declínio no faturamento.
        '''
        # Define a categoria de agrupamento como "Crescimento"
        self.agrupador = 'Crescimento'
        # Define a fórmula do CAGR
        self.formula = '''
        CAGR = (VF / VI)^(1/n) - 1
        Onde:
        - VF = Valor Final das receitas (ao final do período de 5 anos)
        - VI = Valor Inicial das receitas (no início do período de 5 anos)
        - n = Número de anos (neste caso, 5)
        '''

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

    # Calcula o CAGR com base nos valores inicial e final das receitas
    def calcular_cagr(self, valor_inicial, valor_final, anos=5):
        try:
            # Verifica se as entradas são numéricas
            for param, nome in [
                (valor_inicial, "Valor Inicial"),
                (valor_final, "Valor Final"),
                (anos, "Número de Anos")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte parâmetros para float
            valor_inicial = float(valor_inicial)
            valor_final = float(valor_final)
            anos = float(anos)
            # Verifica se o valor inicial é maior que zero
            if valor_inicial <= 0:
                raise ValueError("O valor inicial das receitas deve ser maior que zero.")
            # Verifica se o número de anos é positivo
            if anos <= 0:
                raise ValueError("O número de anos deve ser maior que zero.")
            # Calcula o CAGR
            cagr = (valor_final / valor_inicial) ** (1 / anos) - 1
            return cagr
        except Exception as e:
            raise ValueError(f"Erro ao calcular o CAGR: {str(e)}")

    # Avalia o valor do CAGR e retorna um objeto ResultadoIND
    def avaliar(self, valor_inicial, valor_final, anos=5):
        # Tenta processar o cálculo do CAGR e a avaliação
        try:
            # Calcula o CAGR
            cagr = self.calcular_cagr(valor_inicial, valor_final, anos)
            # Verifica se CAGR é negativo, indicando declínio nas receitas
            if cagr < 0:
                # Retorna ResultadoIND para CAGR negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='CAGR < 0%',
                    descricao='Um CAGR negativo indica declínio nas receitas ao longo dos cinco anos. Isso sugere dificuldades operacionais, perda de mercado ou desafios setoriais, comprometendo a sustentabilidade financeira da empresa.',
                    riscos='Risco de insustentabilidade financeira, perda de competitividade ou necessidade de reestruturação. Pode haver dependência de fatores externos adversos.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_div_liquida_ebitda para alavancagem e evaluate_fcf para geração de caixa.',
                    recomendacao='Evite investir devido ao declínio nas receitas. Priorize análise de fundamentos operacionais e estratégias de recuperação.'
                )
            # Verifica se CAGR está entre 0 e 5%, indicando crescimento baixo
            elif 0 <= cagr <= 0.05:
                # Retorna ResultadoIND para crescimento baixo
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= CAGR <= 5%',
                    descricao='O CAGR indica crescimento baixo das receitas, comum em setores maduros ou empresas com desafios de expansão. Sugere estabilidade, mas limitada capacidade de crescimento orgânico.',
                    riscos='Risco de estagnação ou perda de competitividade em setores dinâmicos. Pode haver dependência de melhorias operacionais para sustentar margens.',
                    referencia='Compare com evaluate_margem_ebitda para lucratividade, evaluate_roe para rentabilidade e evaluate_p_vpa para valuation.',
                    recomendacao='Considere investir com cautela, priorizando empresas com margens sólidas ou potencial de melhoria operacional. Avalie o contexto setorial.'
                )
            # Verifica se CAGR está entre 5% e 10%, indicando crescimento moderado
            elif 0.05 < cagr <= 0.10:
                # Retorna ResultadoIND para crescimento moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5% < CAGR <= 10%',
                    descricao='O CAGR indica crescimento moderado das receitas, típico de empresas em setores estáveis ou em fase de consolidação. Sugere equilíbrio entre crescimento e estabilidade, com potencial para ganhos consistentes.',
                    riscos='Risco de competição setorial ou necessidade de investimentos para manter o crescimento. Pode haver sensibilidade a mudanças econômicas.',
                    referencia='Analise evaluate_fcd para valuation, evaluate_liquidez_corrente para liquidez e evaluate_margem_bruta para eficiência.',
                    recomendacao='Considere investir, especialmente se a empresa apresentar margens sólidas e boa gestão. Boa opção para investidores moderados.'
                )
            # Verifica se CAGR está entre 10% e 20%, indicando crescimento alto
            elif 0.10 < cagr <= 0.20:
                # Retorna ResultadoIND para crescimento alto
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10% < CAGR <= 20%',
                    descricao='O CAGR indica crescimento alto das receitas, comum em empresas em setores dinâmicos, como tecnologia ou varejo em expansão. Sugere forte capacidade de crescimento e atratividade para investidores.',
                    riscos='Risco de volatilidade em setores competitivos ou dependência de condições econômicas favoráveis. Pode haver necessidade de capital para expansão.',
                    referencia='Verifique evaluate_p_ebitda para valuation, evaluate_fcf para geração de caixa e evaluate_beta para risco.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade do crescimento e a alavancagem financeira. Boa opção para investidores tolerantes a risco.'
                )
            # Verifica se CAGR excede 20%, indicando crescimento excepcional
            elif cagr > 0.20:
                # Retorna ResultadoIND para crescimento excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='CAGR > 20%',
                    descricao='O CAGR indica crescimento excepcional das receitas, típico de empresas em setores de alto crescimento, como tecnologia ou startups. Sugere forte potencial de valorização, mas pode vir acompanhado de maior volatilidade.',
                    riscos='Risco de crescimento insustentável ou dependência de aportes de capital. Pode haver volatilidade significativa em setores de alto crescimento.',
                    referencia='Avalie evaluate_wacc para custo de capital, evaluate_div_liquida_pl para alavancagem e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir, mas diversifique para mitigar riscos. Priorize empresas com fundamentos sólidos e geração de caixa.'
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
                Ocorreu um erro ao processar o CAGR: {mensagem}.
                Verifique os dados de entrada (valor inicial, valor final, número de anos) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe BetaEvaluator para avaliar o indicador Índice Beta
class BetaEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do Beta
    def __init__(self):
        # Define string multilinha explicando o índice Beta
        self.definicao = '''
        O Índice Beta mede a volatilidade de uma ação em relação ao mercado, representando o risco sistemático (relacionado ao mercado)
        de um investimento. É calculado como a covariância entre os retornos da ação e do mercado dividida pela variância dos retornos
        do mercado. Um Beta de 1 indica que a ação acompanha o mercado; maior que 1 sugere maior volatilidade (mais risco); menor que 1
        indica menor volatilidade (menos risco). É usado para avaliar o risco de portfólio e o custo do capital próprio (ex.: via CAPM).
        '''
        # Define a categoria de agrupamento como "Risco"
        self.agrupador = 'Risco'
        # Define a fórmula do Beta
        self.formula = '''
        Beta = Cov(Rₐ, Rₘ) / Var(Rₘ)
        Onde:
        - Rₐ = Retornos da ação
        - Rₘ = Retornos do mercado
        - Cov(Rₐ, Rₘ) = Covariância entre os retornos da ação e do mercado
        - Var(Rₘ) = Variância dos retornos do mercado
        '''

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

    # Calcula o Beta com base nos retornos da ação e do mercado
    def calcular_beta(self, retornos_acao, retornos_mercado):
        try:
            # Verifica se as entradas são listas ou tuplas numéricas com o mesmo tamanho
            if not isinstance(retornos_acao, (list, tuple)) or not isinstance(retornos_mercado, (list, tuple)):
                raise ValueError("Retornos da ação e do mercado devem ser listas ou tuplas.")
            if len(retornos_acao) != len(retornos_mercado):
                raise ValueError("Retornos da ação e do mercado devem ter o mesmo tamanho.")
            if len(retornos_acao) < 2:
                raise ValueError("É necessário pelo menos dois períodos de retornos para calcular o Beta.")
            for r_a, r_m in zip(retornos_acao, retornos_mercado):
                if not isinstance(r_a, (int, float)) and not (isinstance(r_a, str) and r_a.replace('.', '', 1).isdigit()):
                    raise ValueError("Os retornos da ação devem ser numéricos.")
                if not isinstance(r_m, (int, float)) and not (isinstance(r_m, str) and r_m.replace('.', '', 1).isdigit()):
                    raise ValueError("Os retornos do mercado devem ser numéricos.")
            # Converte retornos para float
            retornos_acao = [float(r) for r in retornos_acao]
            retornos_mercado = [float(r) for r in retornos_mercado]
            # Calcula a média dos retornos
            media_acao = sum(retornos_acao) / len(retornos_acao)
            media_mercado = sum(retornos_mercado) / len(retornos_mercado)
            # Calcula a covariância entre retornos da ação e do mercado
            covariancia = sum((r_a - media_acao) * (r_m - media_mercado) for r_a, r_m in zip(retornos_acao, retornos_mercado)) / (len(retornos_acao) - 1)
            # Calcula a variância dos retornos do mercado
            variancia_mercado = sum((r_m - media_mercado) ** 2 for r_m in retornos_mercado) / (len(retornos_mercado) - 1)
            if variancia_mercado == 0:
                raise ValueError("A variância dos retornos do mercado não pode ser zero.")
            # Calcula o Beta
            beta = covariancia / variancia_mercado
            return beta
        except Exception as e:
            raise ValueError(f"Erro ao calcular o Beta: {str(e)}")

    # Avalia o valor do Beta e retorna um objeto ResultadoIND
    def avaliar(self, retornos_acao, retornos_mercado):
        # Tenta processar o cálculo do Beta e a avaliação
        try:
            # Calcula o Beta
            beta = self.calcular_beta(retornos_acao, retornos_mercado)
            # Verifica se Beta é negativo, indicando comportamento atípico
            if beta < 0:
                # Retorna ResultadoIND para Beta negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Beta < 0',
                    descricao='Um Beta negativo indica que a ação se move em direção oposta ao mercado, um comportamento atípico. Comum em ativos de proteção, como ouro, ou em empresas com retornos erráticos, sugere incerteza elevada ou dados inconsistentes.',
                    riscos='Risco de comportamento imprevisível ou dados históricos não confiáveis. Pode haver dificuldades em usar o Beta para estimar o custo do capital.',
                    referencia='Avalie evaluate_wacc para custo de capital, evaluate_fcd para valuation e evaluate_roe para rentabilidade.',
                    recomendacao='Evite usar o Beta para decisões de investimento até validar os dados históricos. Considere outros indicadores de risco e fundamentos.'
                )
            # Verifica se Beta está entre 0 e 0.8, indicando baixo risco
            elif 0 <= beta < 0.8:
                # Retorna ResultadoIND para baixo risco
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= Beta < 0.8',
                    descricao='O Beta é baixo, indicando que a ação é menos volátil que o mercado. Comum em empresas estáveis, como utilities ou bens de consumo, sugere menor risco sistemático e maior segurança para investidores avessos a risco.',
                    riscos='Risco de retornos limitados em mercados de alta. Pode haver menor potencial de valorização em cenários de crescimento.',
                    referencia='Compare com evaluate_wacc para custo de capital, evaluate_div_liquida_ebitda para alavancagem e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir, especialmente para portfólios defensivos. Boa opção para investidores que buscam estabilidade e baixo risco.'
                )
            # Verifica se Beta está entre 0.8 e 1.2, indicando risco moderado
            elif 0.8 <= beta <= 1.2:
                # Retorna ResultadoIND para risco moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.8 <= Beta <= 1.2',
                    descricao='O Beta está próximo de 1, indicando que a ação acompanha a volatilidade do mercado. Comum em empresas de setores maduros, como indústria ou varejo, sugere um equilíbrio entre risco e retorno, adequado para investidores com tolerância moderada.',
                    riscos='Risco de exposição a flutuações de mercado. Pode haver sensibilidade a choques econômicos ou eventos macroeconômicos.',
                    referencia='Verifique evaluate_p_vpa para valuation, evaluate_roe para rentabilidade e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Considere investir, mas diversifique para mitigar riscos de mercado. Boa opção para investidores que buscam equilíbrio.'
                )
            # Verifica se Beta está entre 1.2 e 2, indicando alto risco
            elif 1.2 < beta <= 2:
                # Retorna ResultadoIND para alto risco
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='1.2 < Beta <= 2',
                    descricao='O Beta é alto, indicando que a ação é mais volátil que o mercado. Comum em setores cíclicos ou de crescimento, como tecnologia ou consumo discricionário, sugere maior risco sistemático, mas também maior potencial de retorno em mercados de alta.',
                    riscos='Risco de perdas significativas em mercados de baixa. Pode haver dependência de condições econômicas favoráveis.',
                    referencia='Analise evaluate_fcd para valuation, evaluate_div_liquida_ebitda para alavancagem e evaluate_margem_ebitda para lucratividade.',
                    recomendacao='Considere investir com cautela, apenas se tolerar alta volatilidade. Diversifique e monitore condições de mercado.'
                )
            # Verifica se Beta excede 2, indicando risco muito alto
            elif beta > 2:
                # Retorna ResultadoIND para risco muito alto
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Beta > 2',
                    descricao='O Beta é extremamente alto, indicando volatilidade extrema em relação ao mercado. Comum em empresas especulativas ou em setores de alto risco, sugere risco sistemático elevado e exposição significativa a flutuações de mercado.',
                    riscos='Risco de perdas substanciais em cenários adversos. Pode haver instabilidade financeira ou dependência de eventos especulativos.',
                    referencia='Avalie evaluate_wacc para custo de capital, evaluate_fcf para geração de caixa e evaluate_p_l para valuation.',
                    recomendacao='Evite investir devido ao alto risco sistemático. Considere apenas para portfólios especulativos com alta diversificação.'
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
                Ocorreu um erro ao processar o Beta: {mensagem}.
                Verifique os dados de entrada (retornos da ação e do mercado) e assegure que sejam numéricos válidos e com tamanho suficiente.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe WACCEvaluator para avaliar o indicador Custo Médio Ponderado de Capital
class WACCEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do WACC
    def __init__(self):
        # Define string multilinha explicando o índice WACC
        self.definicao = '''
        O WACC (Weighted Average Cost of Capital) é o custo médio ponderado do capital próprio (equity) e da dívida, ajustado pela
        estrutura de capital da empresa. É calculado como a soma do custo do capital próprio (ponderado pela proporção de equity) e
        do custo da dívida (ponderado pela proporção de dívida, ajustado pela dedução fiscal). O WACC representa a taxa mínima de retorno
        exigida pelos investidores e é usado como taxa de desconto em avaliações como o Fluxo de Caixa Descontado (FCD). Um WACC baixo
        sugere financiamento acessível, enquanto um WACC alto indica maior risco ou custo elevado de capital.
        '''
        # Define a categoria de agrupamento como "Estrutura de Capital"
        self.agrupador = 'Estrutura de Capital'
        # Define a fórmula do WACC
        self.formula = '''
        WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc)
        Onde:
        - E = Valor de mercado do capital próprio (equity)
        - D = Valor de mercado da dívida
        - V = E + D (valor total da empresa)
        - Re = Custo do capital próprio (ex.: estimado pelo CAPM)
        - Rd = Custo da dívida (ex.: taxa de juros média)
        - Tc = Taxa de imposto (alíquota efetiva, para dedução fiscal dos juros)
        '''

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

    # Calcula o WACC com base nos parâmetros fornecidos
    def calcular_wacc(self, equity, divida, custo_equity, custo_divida, taxa_imposto):
        try:
            # Verifica se todas as entradas são numéricas
            for param, nome in [
                (equity, "Equity"),
                (divida, "Dívida"),
                (custo_equity, "Custo do Equity"),
                (custo_divida, "Custo da Dívida"),
                (taxa_imposto, "Taxa de Imposto")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte parâmetros para float
            equity = float(equity)
            divida = float(divida)
            custo_equity = float(custo_equity)
            custo_divida = float(custo_divida)
            taxa_imposto = float(taxa_imposto)
            # Calcula o valor total (V = E + D)
            valor_total = equity + divida
            if valor_total == 0:
                raise ValueError("O valor total (Equity + Dívida) não pode ser zero.")
            # Calcula as proporções de equity e dívida
            proporcao_equity = equity / valor_total
            proporcao_divida = divida / valor_total
            # Calcula o WACC
            wacc = (proporcao_equity * custo_equity) + (proporcao_divida * custo_divida * (1 - taxa_imposto))
            return wacc
        except Exception as e:
            raise ValueError(f"Erro ao calcular o WACC: {str(e)}")

    # Avalia o valor do WACC e retorna um objeto ResultadoIND
    def avaliar(self, equity, divida, custo_equity, custo_divida, taxa_imposto):
        # Tenta processar o cálculo do WACC e a avaliação
        try:
            # Calcula o WACC
            wacc = self.calcular_wacc(equity, divida, custo_equity, custo_divida, taxa_imposto)
            # Verifica se WACC é negativo ou inválido
            if wacc < 0:
                # Retorna ResultadoIND para WACC inválido
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='WACC < 0',
                    descricao='Um WACC negativo é inválido e indica erro nos dados de entrada, como custos de capital negativos ou premissas incorretas. Reflete problemas na estrutura de capital ou cálculos, tornando a análise de valuation não confiável.',
                    riscos='Risco de premissas financeiras incorretas ou dados inconsistentes. Pode comprometer análises de FCD ou decisões de investimento.',
                    referencia='Avalie evaluate_fcd para valuation, evaluate_div_liquida_ebitda para alavancagem e evaluate_roe para rentabilidade.',
                    recomendacao='Revise os dados de entrada (equity, dívida, custos, taxa de imposto) antes de prosseguir com análises financeiras. Evite decisões de investimento.'
                )
            # Verifica se WACC está entre 0 e 5%, indicando custo de capital muito baixo
            elif 0 <= wacc <= 0.05:
                # Retorna ResultadoIND para custo de capital muito baixo
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= WACC <= 5%',
                    descricao='O WACC é muito baixo, indicando um custo de capital extremamente acessível. Comum em empresas com baixa alavancagem ou em setores estáveis com acesso a dívida barata, sugere alta atratividade para investimentos e facilidade de financiamento.',
                    riscos='Risco de subestimação do custo do equity ou dívida, ou premissas otimistas. Pode haver dependência de condições de mercado favoráveis.',
                    referencia='Compare com evaluate_fcd para valuation, evaluate_div_liquida_pl para alavancagem e evaluate_margem_ebitda para lucratividade.',
                    recomendacao='Considere investir, mas valide as premissas do WACC e a sustentabilidade do custo de capital. Boa opção para investidores que buscam baixo risco.'
                )
            # Verifica se WACC está entre 5% e 8%, indicando custo de capital baixo
            elif 0.05 < wacc <= 0.08:
                # Retorna ResultadoIND para custo de capital baixo
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='5% < WACC <= 8%',
                    descricao='O WACC é baixo, indicando um custo de capital acessível. Comum em empresas estáveis, como bens de consumo ou utilities, sugere boa capacidade de financiamento com risco moderado, sendo atraente para investidores.',
                    riscos='Risco de aumento nos custos de capital em cenários de alta de juros ou volatilidade de mercado. Pode haver dependência de dívida barata.',
                    referencia='Analise evaluate_fcd para valuation, evaluate_div_liquida_ebitda para alavancagem e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas monitore mudanças nas taxas de juros e no custo do equity. Boa opção para investidores que buscam equilíbrio.'
                )
            # Verifica se WACC está entre 8% e 12%, indicando custo de capital moderado
            elif 0.08 < wacc <= 0.12:
                # Retorna ResultadoIND para custo de capital moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='8% < WACC <= 12%',
                    descricao='O WACC está em uma faixa moderada, indicando um custo de capital típico para empresas em setores competitivos, como tecnologia ou manufatura. Sugere equilíbrio entre risco e retorno, mas com necessidade de geração de caixa robusta para cobrir o custo.',
                    riscos='Risco de aumento no custo de capital em cenários econômicos adversos. Pode haver pressão para melhorar a eficiência operacional.',
                    referencia='Verifique evaluate_fcd para valuation, evaluate_margem_liquida para lucratividade e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Considere investir com cautela, avaliando a capacidade de geração de caixa e a estabilidade do setor. Boa opção para investidores tolerantes a risco moderado.'
                )
            # Verifica se WACC está entre 12% e 15%, indicando custo de capital alto
            elif 0.12 < wacc <= 0.15:
                # Retorna ResultadoIND para custo de capital alto
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='12% < WACC <= 15%',
                    descricao='O WACC é alto, indicando um custo de capital elevado. Comum em empresas com alta alavancagem ou em setores voláteis, como startups ou cíclicos, sugere maior risco para investidores e necessidade de retornos elevados para justificar investimentos.',
                    riscos='Risco de dificuldades em financiar projetos ou pagar dívidas. Pode haver dependência de capital caro ou volatilidade no custo do equity.',
                    referencia='Analise evaluate_div_liquida_ebitda para alavancagem, evaluate_fcf para geração de caixa e evaluate_p_ebitda para valuation.',
                    recomendacao='Evite investir a menos que a empresa demonstre forte geração de caixa ou potencial de crescimento. Priorize análise de risco e retorno.'
                )
            # Verifica se WACC excede 15%, indicando custo de capital muito alto
            elif wacc > 0.15:
                # Retorna ResultadoIND para custo de capital muito alto
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='WACC > 15%',
                    descricao='O WACC é extremamente alto, indicando um custo de capital muito elevado. Comum em empresas em setores de alto risco ou com estrutura de capital instável, sugere dificuldades significativas em financiar operações ou projetos, com alto risco para investidores.',
                    riscos='Risco de insolvência, necessidade de capital caro ou diluição acionária. Pode haver má gestão financeira ou exposição a mercados voláteis.',
                    referencia='Avalie evaluate_div_liquida_pl para alavancagem, evaluate_fcd para valuation e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir devido ao alto custo de capital e risco financeiro. Priorize análise de reestruturação financeira e fundamentos operacionais.'
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
                Ocorreu um erro ao processar o WACC: {mensagem}.
                Verifique os dados de entrada (Equity, Dívida, Custo do Equity, Custo da Dívida, Taxa de Imposto) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe FCDEvaluator para avaliar o indicador Fluxo de Caixa Descontado
class FCDEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do FCD
    def __init__(self):
        # Define string multilinha explicando o índice Fluxo de Caixa Descontado
        self.definicao = '''
        O Fluxo de Caixa Descontado (FCD) é uma metodologia de valuation que estima o valor intrínseco de uma empresa somando o valor presente
        dos Fluxos de Caixa Livres para a Firma (FCFF) projetados para um período explícito (ex.: 5 anos) e um valor terminal, descontados pelo
        Custo Médio Ponderado de Capital (WACC). O FCD reflete o valor econômico da empresa, considerando sua capacidade de gerar caixa futuro.
        Um FCD maior que o valor de mercado sugere subvalorização, enquanto um FCD menor indica sobrevalorização.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do FCD
        self.formula = '''
        FCD = Σ [FCFFₜ / (1 + WACC)ᵗ] + Valor Terminal / (1 + WACC)ⁿ
        Onde:
        - FCFFₜ = Fluxo de Caixa Livre para a Firma no ano t
        - WACC = Custo Médio Ponderado de Capital
        - Valor Terminal = FCFFₙ₊₁ / (WACC - g), onde g é a taxa de crescimento perpétuo
        - n = número de anos no período explícito
        FCFF = EBIT × (1 - Taxa de Imposto) + Depreciação e Amortização - Variação no Capital de Giro - CAPEX
        '''

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

    # Calcula o Fluxo de Caixa Livre para a Firma (FCFF) para um único ano
    def calcular_fcff(self, ebit, taxa_imposto, depreciacao_amortizacao, variacao_capital_giro, capex):
        try:
            # Verifica se todas as entradas são numéricas
            for param, nome in [
                (ebit, "EBIT"),
                (taxa_imposto, "Taxa de Imposto"),
                (depreciacao_amortizacao, "Depreciação e Amortização"),
                (variacao_capital_giro, "Variação no Capital de Giro"),
                (capex, "CAPEX")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte parâmetros para float
            ebit = float(ebit)
            taxa_imposto = float(taxa_imposto)
            depreciacao_amortizacao = float(depreciacao_amortizacao)
            variacao_capital_giro = float(variacao_capital_giro)
            capex = float(capex)
            # Calcula o FCFF
            fcff = (ebit * (1 - taxa_imposto)) + depreciacao_amortizacao - variacao_capital_giro - capex
            return fcff
        except Exception as e:
            raise ValueError(f"Erro ao calcular o FCFF: {str(e)}")

    # Calcula o Fluxo de Caixa Descontado (FCD)
    def calcular_fcd(self, fcffs_projetados, wacc, taxa_crescimento_perpetuo, anos_projetados):
        try:
            # Verifica se as entradas são válidas
            if not isinstance(fcffs_projetados, (list, tuple)) or len(fcffs_projetados) != anos_projetados:
                raise ValueError("fcffs_projetados deve ser uma lista com tamanho igual a anos_projetados.")
            for fcff in fcffs_projetados:
                if not isinstance(fcff, (int, float)) and not (isinstance(fcff, str) and fcff.replace('.', '', 1).isdigit()):
                    raise ValueError("Cada FCFF projetado deve ser numérico.")
            if not isinstance(wacc, (int, float)) and not (isinstance(wacc, str) and wacc.replace('.', '', 1).isdigit()):
                raise ValueError("O WACC deve ser numérico.")
            if not isinstance(taxa_crescimento_perpetuo, (int, float)) and not (isinstance(taxa_crescimento_perpetuo, str) and taxa_crescimento_perpetuo.replace('.', '', 1).isdigit()):
                raise ValueError("A taxa de crescimento perpétuo deve ser numérica.")
            if not isinstance(anos_projetados, int) or anos_projetados <= 0:
                raise ValueError("anos_projetados deve ser um inteiro positivo.")
            # Converte parâmetros para float
            wacc = float(wacc)
            taxa_crescimento_perpetuo = float(taxa_crescimento_perpetuo)
            fcffs_projetados = [float(fcff) for fcff in fcffs_projetados]
            # Verifica se WACC > taxa de crescimento perpétuo
            if wacc <= taxa_crescimento_perpetuo:
                raise ValueError("O WACC deve ser maior que a taxa de crescimento perpétuo para calcular o valor terminal.")
            # Calcula o valor presente dos FCFFs projetados
            valor_presente_fcffs = 0
            for t in range(1, anos_projetados + 1):
                valor_presente_fcffs += fcffs_projetados[t - 1] / ((1 + wacc) ** t)
            # Calcula o valor terminal (perpetuidade)
            fcff_terminal = fcffs_projetados[-1] * (1 + taxa_crescimento_perpetuo)
            valor_terminal = fcff_terminal / (wacc - taxa_crescimento_perpetuo)
            # Desconta o valor terminal para o presente
            valor_terminal_presente = valor_terminal / ((1 + wacc) ** anos_projetados)
            # Calcula o FCD total
            fcd = valor_presente_fcffs + valor_terminal_presente
            return fcd
        except Exception as e:
            raise ValueError(f"Erro ao calcular o FCD: {str(e)}")

    # Avalia o FCD em relação ao valor de mercado (Enterprise Value) e retorna um objeto ResultadoIND
    def avaliar(self, fcffs_projetados, wacc, taxa_crescimento_perpetuo, anos_projetados, enterprise_value):
        # Tenta processar o cálculo do FCD e a avaliação
        try:
            # Verifica se Enterprise Value é numérico
            if not isinstance(enterprise_value, (int, float)) and not (isinstance(enterprise_value, str) and enterprise_value.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do Enterprise Value deve ser numérico.")
            # Converte Enterprise Value para float
            enterprise_value = float(enterprise_value)
            # Calcula o FCD
            fcd = self.calcular_fcd(fcffs_projetados, wacc, taxa_crescimento_perpetuo, anos_projetados)
            # Calcula a proporção FCD/EV
            if enterprise_value == 0:
                raise ValueError("O Enterprise Value não pode ser zero para calcular a proporção FCD/EV.")
            proporcao_fcd_ev = fcd / enterprise_value
            # Verifica se FCD é negativo, indicando projeções inválidas
            if fcd < 0:
                # Retorna ResultadoIND para FCD negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='FCD < 0',
                    descricao='Um FCD negativo indica projeções de fluxo de caixa inválidas ou insustentáveis, sugerindo problemas graves nas operações ou premissas irrealistas. Comum em empresas em crise ou com projeções excessivamente pessimistas, reflete alto risco de investimento.',
                    riscos='Risco de insolvência, projeções não confiáveis ou má gestão operacional. Pode haver erros nas premissas de crescimento ou CAPEX elevado.',
                    referencia='Avalie evaluate_fcf para geração de caixa, evaluate_ebitda para lucratividade operacional e evaluate_div_liquida_ebitda para alavancagem.',
                    recomendacao='Evite investir até que as projeções sejam revisadas e validadas. Priorize análise de fluxo de caixa histórico e fundamentos operacionais.'
                )
            # Verifica se FCD/EV está abaixo de 0.8, indicando sobrevalorização
            elif proporcao_fcd_ev < 0.8:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='FCD/EV < 0.8',
                    descricao='O FCD é significativamente menor que o valor de mercado, sugerindo que a empresa está sobrevalorizada. Comum em empresas com altas expectativas de mercado ou setores inflacionados, indica que o preço atual pode não ser justificado pelos fluxos de caixa futuros.',
                    riscos='Risco de correção no preço da ação ou bolha de mercado. Pode haver dependência de premissas otimistas não sustentadas pelos fundamentos.',
                    referencia='Compare com evaluate_p_ebitda para valuation, evaluate_margem_liquida para lucratividade e evaluate_roe para rentabilidade patrimonial.',
                    recomendacao='Evite investir devido à possível sobrevalorização. Considere esperar por uma correção de preço ou valide as projeções de crescimento.'
                )
            # Verifica se FCD/EV está entre 0.8 e 1.2, indicando valuation justo
            elif 0.8 <= proporcao_fcd_ev <= 1.2:
                # Retorna ResultadoIND para valuation justo
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.8 <= FCD/EV <= 1.2',
                    descricao='O FCD está alinhado com o valor de mercado, indicando que a empresa está justamente precificada. Comum em empresas estáveis, como bens de consumo ou manufatura, sugere que o preço reflete adequadamente os fluxos de caixa futuros projetados.',
                    riscos='Risco de estagnação no preço se as projeções de crescimento não se concretizarem. Pode haver sensibilidade a mudanças no WACC ou taxa de crescimento.',
                    referencia='Verifique evaluate_p_vpa para valuation, evaluate_giro_ativo para eficiência e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Considere investir, mas avalie a consistência das projeções e a estabilidade do setor. Boa opção para investidores que buscam equilíbrio.'
                )
            # Verifica se FCD/EV está entre 1.2 e 2, indicando subvalorização
            elif 1.2 < proporcao_fcd_ev <= 2:
                # Retorna ResultadoIND para subvalorização
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1.2 < FCD/EV <= 2',
                    descricao='O FCD é significativamente maior que o valor de mercado, indicando que a empresa está subvalorizada. Comum em empresas com forte geração de caixa ou setores subestimados, sugere oportunidade de investimento com potencial de valorização.',
                    riscos='Risco de projeções otimistas ou fundamentos frágeis não refletidos no FCD. Pode haver incertezas no setor ou má percepção do mercado.',
                    referencia='Combine com evaluate_p_l para valuation, evaluate_fcf para geração de caixa e evaluate_margem_ebitda para lucratividade operacional.',
                    recomendacao='Considere investir, mas valide as projeções de fluxo de caixa e fundamentos operacionais. Boa opção para investidores de valor.'
                )
            # Verifica se FCD/EV excede 2, indicando forte subvalorização
            elif proporcao_fcd_ev > 2:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='FCD/EV > 2',
                    descricao='O FCD é muito superior ao valor de mercado, indicando forte subvalorização. Típico de empresas com fluxos de caixa robustos ou mercados subestimados, sugere uma oportunidade significativa de valorização, especialmente em setores cíclicos ou em recuperação.',
                    riscos='Risco de projeções excessivamente otimistas ou ativos de baixa qualidade. Pode haver volatilidade de mercado ou incertezas setoriais.',
                    referencia='Analise evaluate_p_vpa para valuation, evaluate_roe para rentabilidade patrimonial e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se as projeções forem robustas e os fundamentos suportarem a subvalorização. Diversifique para mitigar riscos de projeção.'
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
                Ocorreu um erro ao processar o Fluxo de Caixa Descontado: {mensagem}.
                Verifique os dados de entrada (FCFFs projetados, WACC, taxa de crescimento perpétuo, anos projetados, Enterprise Value) e assegure que sejam válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe FCFEvaluator para avaliar o indicador Fluxo de Caixa Livre
class FCFEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do FCF
    def __init__(self):
        # Define string multilinha explicando o índice Fluxo de Caixa Livre
        self.definicao = '''
        O Fluxo de Caixa Livre (FCF) representa o caixa gerado pelas operações da empresa após deduzir os gastos de capital (CAPEX)
        e as variações no capital de giro, mas antes de pagamentos de juros ou dividendos. É calculado como EBIT ajustado por impostos,
        mais depreciação e amortização, menos variações no capital de giro e CAPEX. É um indicador de saúde financeira que mostra a
        capacidade da empresa de gerar caixa para acionistas, redução de dívidas ou reinvestimento. Valores altos sugerem robustez financeira,
        enquanto valores baixos ou negativos indicam fragilidade ou necessidade de financiamento.
        '''
        # Define a categoria de agrupamento como "Geração de Caixa"
        self.agrupador = 'Geração de Caixa'
        # Define a fórmula do FCF
        self.formula = '''
        FCF = EBIT × (1 - Taxa de Imposto) + Depreciação e Amortização - Variação no Capital de Giro - CAPEX
        Onde:
        - EBIT: Lucro antes de juros e impostos
        - Taxa de Imposto: Alíquota efetiva de imposto
        - Depreciação e Amortização: Despesas não-caixa
        - Variação no Capital de Giro: Mudança nos ativos e passivos circulantes
        - CAPEX: Gastos de capital em ativos fixos
        '''

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

    # Calcula o Fluxo de Caixa Livre com base nos parâmetros fornecidos
    def calcular_fcf(self, ebit, taxa_imposto, depreciacao_amortizacao, variacao_capital_giro, capex):
        try:
            # Verifica se todas as entradas são numéricas
            for param, nome in [
                (ebit, "EBIT"),
                (taxa_imposto, "Taxa de Imposto"),
                (depreciacao_amortizacao, "Depreciação e Amortização"),
                (variacao_capital_giro, "Variação no Capital de Giro"),
                (capex, "CAPEX")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte todos os parâmetros para float
            ebit = float(ebit)
            taxa_imposto = float(taxa_imposto)
            depreciacao_amortizacao = float(depreciacao_amortizacao)
            variacao_capital_giro = float(variacao_capital_giro)
            capex = float(capex)
            # Calcula o FCF
            fcf = (ebit * (1 - taxa_imposto)) + depreciacao_amortizacao - variacao_capital_giro - capex
            return fcf
        except Exception as e:
            raise ValueError(f"Erro ao calcular o FCF: {str(e)}")

    # Avalia o valor do FCF em relação à Receita Líquida e retorna um objeto ResultadoIND
    def avaliar(self, ebit, taxa_imposto, depreciacao_amortizacao, variacao_capital_giro, capex, receita_liquida):
        # Tenta processar o cálculo do FCF e a avaliação
        try:
            # Verifica se Receita Líquida é numérica
            if not isinstance(receita_liquida, (int, float)) and not (isinstance(receita_liquida, str) and receita_liquida.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Receita Líquida deve ser numérico.")
            # Converte Receita Líquida para float
            receita_liquida = float(receita_liquida)
            # Calcula o FCF
            fcf = self.calcular_fcf(ebit, taxa_imposto, depreciacao_amortizacao, variacao_capital_giro, capex)
            # Calcula a margem de FCF (FCF / Receita Líquida)
            if receita_liquida == 0:
                raise ValueError("A Receita Líquida não pode ser zero para calcular a margem de FCF.")
            margem_fcf = fcf / receita_liquida
            # Verifica se FCF é negativo, indicando problemas financeiros
            if margem_fcf < 0:
                # Retorna ResultadoIND para FCF negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='FCF < 0',
                    descricao='Um FCF negativo indica que a empresa não gera caixa suficiente após despesas operacionais e investimentos, sugerindo dependência de financiamento externo ou queima de caixa. Comum em empresas em crise ou em fase de crescimento intensivo, reflete alto risco financeiro.',
                    riscos='Risco de insolvência, necessidade de capital externo ou diluição acionária. Pode haver ineficiência operacional ou investimentos excessivos.',
                    referencia='Avalie evaluate_ebitda para geração de caixa operacional, evaluate_div_liquida_ebitda para alavancagem e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação na geração de caixa. Priorize análise de CAPEX e estratégias de eficiência.'
                )
            # Verifica se a margem FCF está entre 0 e 5%, indicando geração de caixa baixa
            elif 0 <= margem_fcf <= 0.05:
                # Retorna ResultadoIND para geração de caixa baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem FCF <= 5%',
                    descricao='A margem de FCF é baixa, indicando geração de caixa limitada em relação à receita. Comum em setores com altos investimentos ou capital de giro elevado, como indústria pesada, sugere eficiência reduzida na conversão de receita em caixa livre.',
                    riscos='Risco de dificuldades em financiar dividendos, reduzir dívidas ou reinvestir. Pode haver dependência de financiamento ou CAPEX elevado.',
                    referencia='Analise evaluate_margem_ebitda para lucratividade operacional, evaluate_giro_ativo para eficiência e evaluate_div_liquida_ebitda para alavancagem.',
                    recomendacao='Considere investir com cautela, avaliando a gestão de CAPEX e capital de giro. Priorize empresas com planos de melhoria na geração de caixa.'
                )
            # Verifica se a margem FCF está entre 5% e 10%, indicando geração de caixa moderada
            elif 0.05 < margem_fcf <= 0.10:
                # Retorna ResultadoIND para geração de caixa moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5% < Margem FCF <= 10%',
                    descricao='A margem de FCF está em uma faixa moderada, indicando eficiência razoável na geração de caixa livre. Comum em empresas estáveis, como varejo ou manufatura, sugere capacidade de cobrir despesas e investimentos, mas com espaço para melhorias.',
                    riscos='Risco de estagnação na geração de caixa em cenários de aumento de CAPEX ou custos. Pode haver dependência de mercados específicos.',
                    referencia='Compare com evaluate_margem_liquida para lucratividade, evaluate_ccc para eficiência de capital de giro e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade da geração de caixa e estratégias de crescimento. Boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se a margem FCF está entre 10% e 20%, indicando boa geração de caixa
            elif 0.10 < margem_fcf <= 0.20:
                # Retorna ResultadoIND para boa geração de caixa
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10% < Margem FCF <= 20%',
                    descricao='A margem de FCF é alta, indicando boa geração de caixa livre em relação à receita. Comum em empresas com operações eficientes, como bens de consumo ou tecnologia, sugere forte capacidade de financiar dividendos, reduzir dívidas ou reinvestir.',
                    riscos='Risco de dependência de mercados específicos ou sazonalidade na receita. Pode haver vulnerabilidade a aumentos no CAPEX.',
                    referencia='Verifique evaluate_margem_ebitda para lucratividade operacional, evaluate_p_ebitda para valuation e evaluate_liquidez_seca para liquidez.',
                    recomendacao='Considere investir, mas monitore a consistência do fluxo de caixa e exposição a riscos de mercado. Boa opção para investidores que buscam eficiência.'
                )
            # Verifica se a margem FCF excede 20%, indicando geração de caixa excepcional
            elif margem_fcf > 0.20:
                # Retorna ResultadoIND para geração de caixa excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem FCF > 20%',
                    descricao='A margem de FCF é extremamente alta, indicando geração de caixa excepcional. Típico de empresas com modelos de negócios eficientes, como tecnologia ou serviços especializados, sugere forte competitividade e flexibilidade financeira para crescimento ou dividendos.',
                    riscos='Risco de caixa ocioso ou margens insustentáveis em mercados saturados. Pode haver dependência de receitas voláteis.',
                    referencia='Combine com evaluate_margem_liquida para lucratividade, evaluate_roe para rentabilidade patrimonial e evaluate_p_ebitda para valuation.',
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
                Ocorreu um erro ao processar o Fluxo de Caixa Livre: {mensagem}.
                Verifique os dados de entrada (EBIT, Taxa de Imposto, Depreciação e Amortização, Variação no Capital de Giro, CAPEX, Receita Líquida) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe CCCEvaluator para avaliar o indicador Ciclo de Conversão de Caixa
class CCCEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do CCC
    def __init__(self):
        # Define string multilinha explicando o índice Ciclo de Conversão de Caixa
        self.definicao = '''
        O Ciclo de Conversão de Caixa (CCC) mede o tempo (em dias) necessário para uma empresa converter seus investimentos em estoques
        e contas a receber em caixa, menos o tempo que leva para pagar seus fornecedores. É calculado como (Período Médio de Estoques +
        Período Médio de Recebíveis - Período Médio de Pagamento). É um indicador de eficiência operacional que avalia a gestão do capital
        de giro. Um CCC baixo indica alta eficiência, enquanto um CCC alto sugere ineficiência ou necessidade de capital elevado.
        '''
        # Define a categoria de agrupamento como "Eficiência Operacional"
        self.agrupador = 'Eficiência Operacional'
        # Define a fórmula do CCC
        self.formula = '''
        CCC = (Período Médio de Estoques + Período Médio de Recebíveis - Período Médio de Pagamento)
        Onde:
        - Período Médio de Estoques = (Estoque Médio / Custo dos Bens Vendidos) * 365
        - Período Médio de Recebíveis = (Contas a Receber Médias / Receita Líquida) * 365
        - Período Médio de Pagamento = (Contas a Pagar Médias / Custo dos Bens Vendidos) * 365
        '''

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

    # Avalia o valor do Ciclo de Conversão de Caixa e retorna um objeto ResultadoIND
    def avaliar(self, ccc):
        # Tenta processar o valor do CCC
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(ccc, (int, float)) and not (isinstance(ccc, str) and ccc.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do CCC deve ser numérico.")
            # Converte CCC para float
            ccc = float(ccc)
            # Verifica se CCC é negativo, indicando eficiência excepcional
            if ccc < 0:
                # Retorna ResultadoIND para CCC negativo
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='CCC < 0 dias',
                    descricao='Um CCC negativo indica que a empresa recebe pagamentos de clientes antes de pagar fornecedores, sugerindo eficiência excepcional na gestão do capital de giro. Comum em empresas com forte poder de negociação, como varejo ou tecnologia, reflete robustez operacional.',
                    riscos='Risco de dependência de termos de pagamento agressivos com fornecedores, que podem ser insustentáveis. Pode haver pressão de fornecedores no longo prazo.',
                    referencia='Analise evaluate_giro_ativo para eficiência, evaluate_liquidez_corrente para liquidez e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade dos termos de pagamento e a qualidade dos recebíveis. Boa opção para investidores que buscam eficiência operacional.'
                )
            # Verifica se CCC está entre 0 e 30 dias, indicando alta eficiência
            elif 0 <= ccc <= 30:
                # Retorna ResultadoIND para alta eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0 <= CCC <= 30 dias',
                    descricao='O CCC é baixo, indicando alta eficiência na gestão do capital de giro. Comum em empresas com operações ágeis, como tecnologia ou bens de consumo, sugere rápida conversão de estoques e recebíveis em caixa, com boa gestão de pagamentos.',
                    riscos='Risco de dependência de ciclos operacionais rápidos, que podem ser afetados por choques de mercado. Pode haver necessidade de monitoramento de estoques.',
                    referencia='Compare com evaluate_liquidez_seca para liquidez, evaluate_margem_bruta para eficiência de custos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir, mas monitore a consistência do ciclo operacional. Boa opção para investidores que buscam eficiência e liquidez.'
                )
            # Verifica se CCC está entre 30 e 60 dias, indicando eficiência moderada
            elif 30 < ccc <= 60:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='30 < CCC <= 60 dias',
                    descricao='O CCC está em uma faixa moderada, indicando eficiência razoável na gestão do capital de giro. Comum em setores como manufatura ou varejo, sugere capacidade de converter estoques e recebíveis em caixa, mas com espaço para melhorias na gestão operacional.',
                    riscos='Risco de ineficiência em estoques ou atrasos em recebíveis, aumentando a necessidade de capital de giro. Pode haver vulnerabilidade a interrupções na cadeia de suprimentos.',
                    referencia='Verifique evaluate_giro_ativo para eficiência, evaluate_liquidez_corrente para liquidez e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir com cautela, avaliando a gestão de estoques e recebíveis. Priorize empresas com estratégias de otimização do capital de giro.'
                )
            # Verifica se CCC está entre 60 e 90 dias, indicando baixa eficiência
            elif 60 < ccc <= 90:
                # Retorna ResultadoIND para baixa eficiência
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='60 < CCC <= 90 dias',
                    descricao='O CCC é alto, indicando baixa eficiência na gestão do capital de giro. Comum em setores com estoques de baixa rotatividade, como indústria pesada, sugere demora na conversão de estoques e recebíveis em caixa, aumentando o risco de necessidade de financiamento.',
                    riscos='Risco de dependência de capital de giro elevado ou dificuldades de liquidez. Pode haver estoques obsoletos ou atrasos em recebíveis.',
                    referencia='Analise evaluate_liquidez_seca para liquidez, evaluate_margem_bruta para eficiência de custos e evaluate_debt_to_ebitda para alavancagem.',
                    recomendacao='Evite investir a menos que haja planos claros de otimização do capital de giro. Monitore a gestão de estoques e recebíveis.'
                )
            # Verifica se CCC excede 90 dias, indicando ineficiência crítica
            elif ccc > 90:
                # Retorna ResultadoIND para ineficiência crítica
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='CCC > 90 dias',
                    descricao='O CCC é extremamente alto, indicando ineficiência grave na gestão do capital de giro. Comum em empresas com problemas operacionais ou setores com baixa rotatividade, sugere dificuldades significativas em converter estoques e recebíveis em caixa, aumentando o risco financeiro.',
                    riscos='Risco de insolvência, necessidade de financiamento constante ou problemas de liquidez. Pode haver estoques obsoletos ou má gestão de recebíveis.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Evite investir devido ao alto risco de ineficiência operacional. Priorize análise de recuperação do capital de giro e estratégias de otimização.'
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
                Ocorreu um erro ao processar o Ciclo de Conversão de Caixa: {mensagem}.
                Verifique os dados de entrada (Estoque Médio, Contas a Receber, Contas a Pagar, Custo dos Bens Vendidos, Receita Líquida) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


# Define a classe LiquidezSecaEvaluator para avaliar o indicador Liquidez Seca
class LiquidezSecaEvaluator:
    # Construtor que inicializa definição, agrupador e descrição da Liquidez Seca
    def __init__(self):
        # Define string multilinha explicando o índice Liquidez Seca
        self.definicao = '''
        A Liquidez Seca mede a capacidade da empresa de cobrir suas obrigações de curto prazo (Passivo Circulante) utilizando apenas
        os ativos circulantes mais líquidos, excluindo estoques, calculada como (Ativo Circulante - Estoques) / Passivo Circulante.
        É um indicador conservador de liquidez de curto prazo que avalia a saúde financeira sem depender da conversão de estoques em caixa.
        Valores altos sugerem robustez financeira, enquanto valores baixos indicam fragilidade em cenários de estresse.
        '''
        # Define a categoria de agrupamento como "Liquidez"
        self.agrupador = 'Liquidez'
        # Define a fórmula da Liquidez Seca
        self.formula = 'Liquidez Seca = (Ativo Circulante - Estoques) / Passivo Circulante'

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

    # Avalia o valor da Liquidez Seca e retorna um objeto ResultadoIND
    def avaliar(self, ativo_circulante, estoques, passivo_circulante):
        # Tenta processar os valores de Ativo Circulante, Estoques e Passivo Circulante
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [
                (ativo_circulante, "Ativo Circulante"),
                (estoques, "Estoques"),
                (passivo_circulante, "Passivo Circulante")
            ]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Ativo Circulante, Estoques e Passivo Circulante para float
            ativo_circulante = float(ativo_circulante)
            estoques = float(estoques)
            passivo_circulante = float(passivo_circulante)
            # Calcula Liquidez Seca
            if passivo_circulante == 0:
                raise ValueError("O Passivo Circulante não pode ser zero para calcular a Liquidez Seca.")
            liquidez_seca = (ativo_circulante - estoques) / passivo_circulante
            # Verifica se Liquidez Seca é negativa, indicando insuficiência de ativos líquidos
            if liquidez_seca < 0:
                # Retorna ResultadoIND para Liquidez Seca negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Liquidez Seca < 0',
                    descricao='Uma Liquidez Seca negativa indica que os ativos circulantes, excluindo estoques, são insuficientes para cobrir o passivo circulante. Comum em empresas em crise ou com má gestão de liquidez, sugere alto risco de insolvência e dependência de estoques.',
                    riscos='Risco de falência, atrasos em pagamentos ou necessidade de financiamento emergencial. Pode haver baixa conversibilidade de ativos em caixa.',
                    referencia='Analise evaluate_liquidez_corrente para liquidez geral, evaluate_disponibilidades para liquidez imediata e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação da liquidez. Priorize análise de fluxo de caixa e estratégias de reestruturação.'
                )
            # Verifica se Liquidez Seca está entre 0 e 0.5, indicando liquidez muito baixa
            elif 0 <= liquidez_seca < 0.5:
                # Retorna ResultadoIND para liquidez muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Liquidez Seca < 0.5',
                    descricao='A Liquidez Seca é muito baixa, indicando capacidade limitada de cobrir o passivo circulante sem depender de estoques. Comum em setores com estoques de baixa liquidez, como manufatura pesada, sugere risco financeiro em cenários de estresse.',
                    riscos='Risco de dificuldades financeiras se os estoques não forem convertidos em caixa. Pode haver dependência de vendas ou financiamentos de curto prazo.',
                    referencia='Compare com evaluate_liquidez_corrente para liquidez geral, evaluate_cash_conversion_cycle para eficiência e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Considere investir com cautela, avaliando a qualidade dos estoques e a gestão de caixa. Priorize empresas com forte geração de caixa.'
                )
            # Verifica se Liquidez Seca está entre 0.5 e 1, indicando liquidez moderada
            elif 0.5 <= liquidez_seca <= 1:
                # Retorna ResultadoIND para liquidez moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.5 <= Liquidez Seca <= 1',
                    descricao='A Liquidez Seca cobre parcialmente ou totalmente o passivo circulante, indicando liquidez moderada. Comum em empresas estáveis, como varejo ou serviços, sugere capacidade de honrar obrigações de curto prazo, mas com dependência limitada de estoques.',
                    riscos='Risco de dificuldades em cenários de estresse, especialmente se os recebíveis forem de baixa qualidade. Pode haver necessidade de gestão rigorosa de caixa.',
                    referencia='Verifique evaluate_disponibilidades para liquidez imediata, evaluate_margem_liquida para lucratividade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir, mas avalie a qualidade dos ativos circulantes e a consistência do fluxo de caixa. Boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se Liquidez Seca está entre 1 e 1.5, indicando boa liquidez
            elif 1 < liquidez_seca <= 1.5:
                # Retorna ResultadoIND para boa liquidez
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1 < Liquidez Seca <= 1.5',
                    descricao='A Liquidez Seca é alta, indicando boa capacidade de cobrir o passivo circulante sem depender de estoques. Comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugere robustez financeira e resistência a imprevistos.',
                    riscos='Risco de ativos circulantes ociosos, como excesso de caixa ou recebíveis de longo prazo. Pode haver ineficiência na alocação de recursos.',
                    referencia='Combine com evaluate_liquidez_corrente para liquidez geral, evaluate_cash_conversion_cycle para eficiência e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas monitore a eficiência na gestão de ativos circulantes. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se Liquidez Seca excede 1.5, indicando liquidez excepcional
            elif liquidez_seca > 1.5:
                # Retorna ResultadoIND para liquidez excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Liquidez Seca > 1.5',
                    descricao='A Liquidez Seca é extremamente alta, indicando capacidade excepcional de cobrir o passivo circulante sem depender de estoques. Típico de empresas com forte geração de caixa, como software ou serviços, sugere robustez financeira e alta resistência a choques.',
                    riscos='Risco de ineficiência no uso de ativos líquidos, com excesso de caixa ocioso. Pode haver perda de oportunidades de investimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_disponibilidades para liquidez imediata, evaluate_cash_flow para geração de caixa e evaluate_psr para valuation.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de recursos. Considere empresas com planos de reinvestimento.'
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
                Ocorreu um erro ao processar a Liquidez Seca: {mensagem}.
                Verifique os dados de entrada (Ativo Circulante, Estoques e Passivo Circulante) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
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
# Define a classe EBITEvaluator para avaliar o indicador EBIT
class EBITEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do EBIT
    def __init__(self):
        # Define string multilinha explicando o índice EBIT
        self.definicao = '''
        O EBIT (Earnings Before Interest and Taxes) representa o lucro antes de juros e impostos, calculado como Receita Líquida menos
        Custos e Despesas Operacionais (excluindo juros e impostos). É um indicador de lucratividade operacional que avalia a capacidade
        da empresa de gerar lucros a partir de suas operações principais. Valores altos sugerem eficiência operacional, enquanto valores
        baixos ou negativos indicam fragilidade ou ineficiência.
        '''
        # Define a categoria de agrupamento como "Lucratividade Operacional"
        self.agrupador = 'Lucratividade Operacional'
        # Define a fórmula do EBIT
        self.formula = 'EBIT = Receita Líquida - Custos Operacionais - Despesas Operacionais'

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

    # Avalia o valor do EBIT em relação à Receita Líquida e retorna um objeto ResultadoIND
    def avaliar(self, ebit, receita_liquida):
        # Tenta processar o valor do EBIT e Receita Líquida
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(ebit, "EBIT"), (receita_liquida, "Receita Líquida")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte EBIT e Receita Líquida para float
            ebit = float(ebit)
            receita_liquida = float(receita_liquida)
            # Calcula a margem EBIT (EBIT / Receita Líquida)
            if receita_liquida == 0:
                raise ValueError("A Receita Líquida não pode ser zero para calcular a margem EBIT.")
            margem_ebit = ebit / receita_liquida
            # Verifica se EBIT é negativo, indicando prejuízo operacional
            if margem_ebit < 0:
                # Retorna ResultadoIND para EBIT negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='EBIT < 0',
                    descricao='Um EBIT negativo indica prejuízo operacional, sugerindo que os custos e despesas superam a receita das operações. Comum em empresas em crise, startups em fase inicial ou setores com margens pressionadas, isso reflete ineficiência operacional e risco elevado.',
                    riscos='Risco de insolvência, má gestão operacional ou baixa competitividade de mercado. Pode haver necessidade de reestruturação ou cortes de custos.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade líquida, evaluate_cash_flow para geração de caixa e evaluate_giro_ativo para eficiência.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação operacional. Priorize análise de custos e estratégias de turnaround.'
                )
            # Verifica se a margem EBIT está entre 0 e 5%, indicando lucratividade operacional baixa
            elif 0 <= margem_ebit <= 0.05:
                # Retorna ResultadoIND para lucratividade baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem EBIT <= 5%',
                    descricao='A margem EBIT é baixa, indicando lucratividade operacional limitada. Comum em setores competitivos ou com altos custos, como varejo ou indústria pesada, sugere eficiência reduzida na geração de lucros a partir das operações principais.',
                    riscos='Risco de margens comprimidas por concorrência ou aumento de custos. Pode haver dificuldades em financiar investimentos ou pagar dívidas.',
                    referencia='Analise evaluate_margem_bruta para eficiência de custos, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir com cautela, avaliando estratégias de redução de custos e competitividade. Priorize empresas com planos de melhoria operacional.'
                )
            # Verifica se a margem EBIT está entre 5% e 10%, indicando lucratividade moderada
            elif 0.05 < margem_ebit <= 0.10:
                # Retorna ResultadoIND para lucratividade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5% < Margem EBIT <= 10%',
                    descricao='A margem EBIT está em uma faixa moderada, indicando eficiência razoável na geração de lucros operacionais. Comum em empresas estáveis, como manufatura ou serviços, sugere capacidade de cobrir custos operacionais, mas com espaço para melhorias.',
                    riscos='Risco de estagnação na lucratividade em cenários de aumento de custos ou concorrência. Pode haver dependência de mercados específicos.',
                    referencia='Compare com evaluate_margem_liquida para lucratividade líquida, evaluate_giro_ativo para eficiência e evaluate_debt_to_ebitda para alavancagem.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade dos lucros e estratégias de crescimento. Boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se a margem EBIT está entre 10% e 20%, indicando boa lucratividade
            elif 0.10 < margem_ebit <= 0.20:
                # Retorna ResultadoIND para boa lucratividade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10% < Margem EBIT <= 20%',
                    descricao='A margem EBIT é alta, indicando boa lucratividade operacional. Comum em empresas com operações eficientes, como bens de consumo ou tecnologia, sugere forte capacidade de gerar lucros a partir das atividades principais, com folga para investimentos.',
                    riscos='Risco de dependência de mercados específicos ou sazonalidade. Pode haver vulnerabilidade a choques econômicos ou aumento de custos.',
                    referencia='Verifique evaluate_roic para retorno sobre capital, evaluate_cash_flow para geração de caixa e evaluate_psr para valuation.',
                    recomendacao='Considere investir, mas monitore a consistência dos lucros e exposição a riscos de mercado. Boa opção para investidores que buscam eficiência.'
                )
            # Verifica se a margem EBIT excede 20%, indicando lucratividade excepcional
            elif margem_ebit > 0.20:
                # Retorna ResultadoIND para lucratividade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem EBIT > 20%',
                    descricao='A margem EBIT é extremamente alta, indicando lucratividade operacional excepcional. Típico de empresas com modelos de negócios eficientes, como tecnologia ou serviços especializados, sugere forte competitividade e capacidade de financiar crescimento ou dividendos.',
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
                Ocorreu um erro ao processar o EBIT: {mensagem}.
                Verifique os dados de entrada (EBIT e Receita Líquida) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe ReceitaLiquidaEvaluator para avaliar o indicador Receita Líquida
class ReceitaLiquidaEvaluator:
    # Construtor que inicializa definição, agrupador e descrição da Receita Líquida
    def __init__(self):
        # Define string multilinha explicando o índice Receita Líquida
        self.definicao = '''
        A Receita Líquida representa o total de vendas de bens ou serviços da empresa, após deduções como impostos, devoluções e descontos,
        em um determinado período. É um indicador de desempenho operacional que reflete a capacidade da empresa de gerar vendas. Valores altos
        sugerem forte desempenho comercial, enquanto valores baixos ou negativos indicam fraqueza operacional ou problemas de mercado.
        '''
        # Define a categoria de agrupamento como "Desempenho Operacional"
        self.agrupador = 'Desempenho Operacional'
        # Define a fórmula da Receita Líquida
        self.formula = 'Receita Líquida = Receita Bruta - (Impostos + Devoluções + Descontos)'

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

    # Avalia o valor da Receita Líquida em relação aos Ativos Totais e retorna um objeto ResultadoIND
    def avaliar(self, receita_liquida, ativos_totais):
        # Tenta processar o valor da Receita Líquida e Ativos Totais
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(receita_liquida, "Receita Líquida"), (ativos_totais, "Ativos Totais")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Receita Líquida e Ativos Totais para float
            receita_liquida = float(receita_liquida)
            ativos_totais = float(ativos_totais)
            # Calcula a proporção da Receita Líquida em relação aos Ativos Totais (Giro do Ativo)
            if ativos_totais == 0:
                raise ValueError("Os Ativos Totais não podem ser zero para calcular a proporção.")
            proporcao_receita_ativos = receita_liquida / ativos_totais
            # Verifica se Receita Líquida é negativa, indicando problemas operacionais
            if receita_liquida < 0:
                # Retorna ResultadoIND para Receita Líquida negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Receita Líquida < 0',
                    descricao='Uma Receita Líquida negativa é inválida ou indica perdas operacionais graves, como devoluções ou ajustes contábeis excessivos. Comum em empresas em crise ou com problemas de mercado, sugere fragilidade operacional e risco elevado.',
                    riscos='Risco de insolvência, má gestão operacional ou baixa demanda de mercado. Pode haver manipulação contábil ou erros nos relatórios financeiros.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_cash_flow para geração de caixa e evaluate_psr para valuation.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação operacional. Priorize análise de fluxo de caixa e estratégias de mercado.'
                )
            # Verifica se a proporção está entre 0 e 0.5, indicando baixa eficiência
            elif 0 <= proporcao_receita_ativos <= 0.5:
                # Retorna ResultadoIND para baixa eficiência
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Receita Líquida / Ativos Totais <= 0.5',
                    descricao='A Receita Líquida é baixa em relação aos ativos, indicando baixa eficiência na utilização de recursos para gerar vendas. Comum em setores intensivos em capital, como imobiliário ou infraestrutura, sugere ineficiência operacional ou ativos ociosos.',
                    riscos='Risco de ativos subutilizados ou baixa competitividade de mercado. Pode haver necessidade de desinvestimento ou reestruturação operacional.',
                    referencia='Analise evaluate_giro_ativo para eficiência, evaluate_roa para rentabilidade dos ativos e evaluate_cash_conversion_cycle para eficiência operacional.',
                    recomendacao='Evite investir a menos que haja planos claros de otimização de ativos. Monitore estratégias para aumentar a receita.'
                )
            # Verifica se a proporção está entre 0.5 e 1, indicando eficiência moderada
            elif 0.5 < proporcao_receita_ativos <= 1:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.5 < Receita Líquida / Ativos Totais <= 1',
                    descricao='A Receita Líquida está em uma faixa moderada em relação aos ativos, indicando eficiência razoável na utilização de recursos. Comum em empresas de setores como manufatura ou varejo, sugere capacidade de gerar vendas, mas com espaço para melhorias.',
                    riscos='Risco de estagnação na receita se os ativos não forem otimizados. Pode haver dependência de ativos fixos ou necessidade de reinvestimento.',
                    referencia='Compare com evaluate_giro_ativo para eficiência, evaluate_margem_liquida para lucratividade e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Considere investir com cautela, avaliando a capacidade de aumentar a receita e otimizar ativos. Priorize empresas com estratégias de crescimento.'
                )
            # Verifica se a proporção está entre 1 e 2, indicando boa eficiência
            elif 1 < proporcao_receita_ativos <= 2:
                # Retorna ResultadoIND para boa eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1 < Receita Líquida / Ativos Totais <= 2',
                    descricao='A Receita Líquida é alta em relação aos ativos, indicando boa eficiência na utilização de recursos para gerar vendas. Comum em empresas estáveis, como bens de consumo ou tecnologia, sugere forte desempenho operacional e produtividade dos ativos.',
                    riscos='Risco de dependência de mercados específicos ou sazonalidade na receita. Pode haver necessidade de reinvestimento para manter o crescimento.',
                    referencia='Verifique evaluate_roa para rentabilidade dos ativos, evaluate_cash_flow para geração de caixa e evaluate_psr para valuation.',
                    recomendacao='Considere investir, mas monitore a sustentabilidade da receita e planos de expansão. Boa opção para investidores que buscam eficiência operacional.'
                )
            # Verifica se a proporção excede 2, indicando eficiência excepcional
            elif proporcao_receita_ativos > 2:
                # Retorna ResultadoIND para eficiência excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Receita Líquida / Ativos Totais > 2',
                    descricao='A Receita Líquida é extremamente alta em relação aos ativos, indicando eficiência excepcional na utilização de recursos. Típico de empresas com modelos leves, como tecnologia ou serviços, sugere forte competitividade e alta produtividade dos ativos.',
                    riscos='Risco de dependência de receitas voláteis ou mercados saturados. Pode haver vulnerabilidade a choques econômicos ou mudanças de demanda.',
                    referencia='Combine com evaluate_giro_ativo para eficiência, evaluate_margem_liquida para lucratividade e evaluate_cash_flow para geração de caixa.',
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
                Ocorreu um erro ao processar a Receita Líquida: {mensagem}.
                Verifique os dados de entrada (Receita Líquida e Ativos Totais) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe DisponibilidadesEvaluator para avaliar o indicador Disponibilidades
class DisponibilidadesEvaluator:
    # Construtor que inicializa definição, agrupador e descrição das Disponibilidades
    def __init__(self):
        # Define string multilinha explicando o índice Disponibilidades
        self.definicao = '''
        As Disponibilidades representam os recursos financeiros líquidos da empresa, como caixa, equivalentes de caixa (ex.: aplicações financeiras de curto prazo)
        e outros ativos imediatamente conversíveis em dinheiro. É um indicador de liquidez imediata que avalia a capacidade da empresa de cumprir obrigações
        financeiras de curto prazo sem depender de vendas ou recebíveis. Valores altos sugerem robustez financeira, enquanto valores baixos indicam fragilidade.
        '''
        # Define a categoria de agrupamento como "Liquidez"
        self.agrupador = 'Liquidez'
        # Define a fórmula das Disponibilidades
        self.formula = 'Disponibilidades = Caixa + Equivalentes de Caixa'

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

    # Avalia o valor das Disponibilidades em relação ao Passivo Circulante e retorna um objeto ResultadoIND
    def avaliar(self, disponibilidades, passivo_circulante):
        # Tenta processar o valor das Disponibilidades e Passivo Circulante
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(disponibilidades, "Disponibilidades"), (passivo_circulante, "Passivo Circulante")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Disponibilidades e Passivo Circulante para float
            disponibilidades = float(disponibilidades)
            passivo_circulante = float(passivo_circulante)
            # Calcula a proporção das Disponibilidades em relação ao Passivo Circulante (Liquidez Imediata)
            if passivo_circulante == 0:
                raise ValueError("O Passivo Circulante não pode ser zero para calcular a proporção.")
            proporcao_liquidez_imediata = disponibilidades / passivo_circulante
            # Verifica se Disponibilidades são negativas, indicando erro nos dados
            if disponibilidades < 0:
                # Retorna ResultadoIND para Disponibilidades negativas
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Disponibilidades < 0',
                    descricao='Disponibilidades negativas são inválidas, indicando erros nos dados financeiros ou relatórios contábeis. Isso pode refletir falhas na consolidação de caixa ou manipulação de informações, tornando a análise de liquidez imediata inviável.',
                    riscos='Risco de manipulação contábil ou baixa confiabilidade nos dados financeiros. Pode haver ausência de transparência ou erros graves nos relatórios.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez geral, evaluate_cash_flow para geração de caixa e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou falta de transparência. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se a proporção está entre 0 e 0.2, indicando liquidez imediata muito baixa
            elif 0 <= proporcao_liquidez_imediata < 0.2:
                # Retorna ResultadoIND para liquidez imediata muito baixa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='0 <= Disponibilidades / Passivo Circulante < 0.2',
                    descricao='As Disponibilidades são muito baixas em relação ao Passivo Circulante, indicando liquidez imediata insuficiente para cobrir obrigações de curto prazo. Comum em empresas em crise ou com má gestão de caixa, sugere alto risco de insolvência.',
                    riscos='Risco de falência, atrasos em pagamentos ou necessidade de financiamento emergencial. Pode haver dependência de recebíveis ou vendas de ativos.',
                    referencia='Analise evaluate_liquidez_corrente para liquidez geral, evaluate_cash_flow para geração de caixa e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação da liquidez. Priorize análise de fluxo de caixa e estratégias de reestruturação.'
                )
            # Verifica se a proporção está entre 0.2 e 0.5, indicando liquidez imediata moderada
            elif 0.2 <= proporcao_liquidez_imediata < 0.5:
                # Retorna ResultadoIND para liquidez imediata moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.2 <= Disponibilidades / Passivo Circulante < 0.5',
                    descricao='As Disponibilidades cobrem parcialmente o Passivo Circulante, indicando liquidez imediata moderada. Comum em empresas estáveis, como varejo ou manufatura, mas sugere capacidade limitada de lidar com obrigações de curto prazo sem recorrer a outros ativos.',
                    riscos='Risco de dificuldades financeiras em cenários de estresse ou atrasos em recebíveis. Pode haver dependência de conversão de ativos para cobrir dívidas.',
                    referencia='Compare com evaluate_liquidez_seca para liquidez sem estoques, evaluate_cash_conversion_cycle para eficiência e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir com cautela, avaliando a qualidade do fluxo de caixa e a gestão de caixa. Priorize empresas com reservas financeiras estáveis.'
                )
            # Verifica se a proporção está entre 0.5 e 1, indicando boa liquidez imediata
            elif 0.5 <= proporcao_liquidez_imediata <= 1:
                # Retorna ResultadoIND para boa liquidez imediata
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.5 <= Disponibilidades / Passivo Circulante <= 1',
                    descricao='As Disponibilidades cobrem bem o Passivo Circulante, indicando boa liquidez imediata. Comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugere capacidade de honrar obrigações de curto prazo com folga e resistência a imprevistos.',
                    riscos='Risco de caixa ocioso, reduzindo retornos potenciais. Pode haver dependência de aplicações financeiras de baixo rendimento.',
                    referencia='Verifique evaluate_liquidez_corrente para liquidez geral, evaluate_cash_flow para geração de caixa e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de caixa. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se a proporção excede 1, indicando liquidez imediata excepcional
            elif proporcao_liquidez_imediata > 1:
                # Retorna ResultadoIND para liquidez imediata excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Disponibilidades / Passivo Circulante > 1',
                    descricao='As Disponibilidades excedem significativamente o Passivo Circulante, indicando liquidez imediata excepcional. Típico de empresas com forte geração de caixa, como software ou serviços, sugere robustez financeira e alta capacidade de honrar obrigações sem depender de outros ativos.',
                    riscos='Risco de ineficiência no uso de caixa, com recursos ociosos. Pode haver perda de oportunidades de investimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_liquidez_seca para liquidez sem estoques, evaluate_cash_conversion_cycle para eficiência e evaluate_psr para receita.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de caixa. Considere empresas com planos de reinvestimento.'
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
                Ocorreu um erro ao processar as Disponibilidades: {mensagem}.
                Verifique os dados de entrada (Disponibilidades e Passivo Circulante) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe AtivoCirculanteEvaluator para avaliar o indicador Ativo Circulante
class AtivoCirculanteEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do Ativo Circulante
    def __init__(self):
        # Define string multilinha explicando o índice Ativo Circulante
        self.definicao = '''
        O Ativo Circulante representa os bens e direitos da empresa que podem ser convertidos em caixa ou consumidos em até um ano,
        como caixa, equivalentes de caixa, recebíveis e estoques. É um indicador de liquidez de curto prazo que avalia a capacidade da
        empresa de honrar obrigações imediatas. Valores altos sugerem boa liquidez, enquanto valores baixos indicam fragilidade financeira.
        '''
        # Define a categoria de agrupamento como "Liquidez"
        self.agrupador = 'Liquidez'
        # Define a fórmula do Ativo Circulante
        self.formula = 'Ativo Circulante = Caixa e Equivalentes + Contas a Receber + Estoques + Outros Ativos de Curto Prazo'

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

    # Avalia o valor do Ativo Circulante em relação ao Passivo Circulante e retorna um objeto ResultadoIND
    def avaliar(self, ativo_circulante, passivo_circulante):
        # Tenta processar o valor do Ativo Circulante e Passivo Circulante
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(ativo_circulante, "Ativo Circulante"), (passivo_circulante, "Passivo Circulante")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Ativo Circulante e Passivo Circulante para float
            ativo_circulante = float(ativo_circulante)
            passivo_circulante = float(passivo_circulante)
            # Calcula a proporção do Ativo Circulante em relação ao Passivo Circulante (Liquidez Corrente)
            if passivo_circulante == 0:
                raise ValueError("O Passivo Circulante não pode ser zero para calcular a proporção.")
            proporcao_liquidez_corrente = ativo_circulante / passivo_circulante
            # Verifica se Ativo Circulante é negativo, indicando erro nos dados
            if ativo_circulante < 0:
                # Retorna ResultadoIND para Ativo Circulante negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Ativo Circulante < 0',
                    descricao='Um Ativo Circulante negativo é inválido, indicando erros nos dados financeiros ou relatórios contábeis. Isso pode refletir falhas na consolidação de ativos ou manipulação de informações, tornando a análise de liquidez inviável.',
                    riscos='Risco de manipulação contábil ou baixa confiabilidade nos dados financeiros. Pode haver ausência de transparência ou erros graves nos relatórios.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou falta de transparência. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se a proporção está entre 0 e 1, indicando baixa liquidez
            elif 0 <= proporcao_liquidez_corrente < 1:
                # Retorna ResultadoIND para baixa liquidez
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='0 <= Ativo Circulante / Passivo Circulante < 1',
                    descricao='O Ativo Circulante é inferior ao Passivo Circulante, indicando baixa liquidez e dificuldade em honrar obrigações de curto prazo. Comum em empresas em crise ou com má gestão financeira, sugere alto risco de insolvência.',
                    riscos='Risco de falência, necessidade de financiamento emergencial ou atrasos em pagamentos. Pode haver restrições severas de credores.',
                    referencia='Analise evaluate_liquidez_imediata para liquidez de caixa, evaluate_cash_flow para geração de caixa e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação da liquidez. Priorize análise de fluxo de caixa e estratégias de reestruturação.'
                )
            # Verifica se a proporção está entre 1 e 1.5, indicando liquidez moderada
            elif 1 <= proporcao_liquidez_corrente <= 1.5:
                # Retorna ResultadoIND para liquidez moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1 <= Ativo Circulante / Passivo Circulante <= 1.5',
                    descricao='O Ativo Circulante cobre o Passivo Circulante com margem limitada, indicando liquidez moderada. Comum em empresas estáveis, como varejo ou manufatura, mas sugere capacidade restrita de lidar com imprevistos financeiros de curto prazo.',
                    riscos='Risco de dificuldades financeiras em cenários de queda na receita ou aumento de obrigações. Pode haver dependência de recebíveis ou estoques.',
                    referencia='Compare com evaluate_liquidez_imediata para liquidez de caixa, evaluate_cash_conversion_cycle para eficiência e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Considere investir com cautela, avaliando a qualidade dos ativos circulantes e fluxo de caixa. Priorize empresas com gestão financeira robusta.'
                )
            # Verifica se a proporção está entre 1.5 e 2, indicando boa liquidez
            elif 1.5 < proporcao_liquidez_corrente <= 2:
                # Retorna ResultadoIND para boa liquidez
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1.5 < Ativo Circulante / Passivo Circulante <= 2',
                    descricao='O Ativo Circulante cobre bem o Passivo Circulante, indicando boa liquidez de curto prazo. Comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugere capacidade de honrar obrigações com folga e lidar com imprevistos.',
                    riscos='Risco de ativos circulantes de baixa qualidade, como recebíveis duvidosos ou estoques obsoletos. Pode haver ineficiência no uso de recursos.',
                    referencia='Verifique evaluate_liquidez_seca para liquidez sem estoques, evaluate_cash_flow para geração de caixa e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas avalie a qualidade dos ativos circulantes e a consistência do fluxo de caixa. Boa opção para investidores que buscam segurança.'
                )
            # Verifica se a proporção excede 2, indicando liquidez excepcional
            elif proporcao_liquidez_corrente > 2:
                # Retorna ResultadoIND para liquidez excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Ativo Circulante / Passivo Circulante > 2',
                    descricao='O Ativo Circulante excede significativamente o Passivo Circulante, indicando liquidez excepcional. Típico de empresas com forte geração de caixa ou baixa necessidade de capital, como software ou serviços, sugere robustez financeira e alta capacidade de honrar obrigações.',
                    riscos='Risco de ineficiência no uso de ativos circulantes, com excesso de caixa ou estoques ociosos. Pode haver perda de oportunidades de investimento.',
                    referencia='Combine com evaluate_liquidez_imediata para liquidez de caixa, evaluate_cash_conversion_cycle para eficiência e evaluate_psr para receita.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de ativos. Considere empresas com planos de reinvestimento.'
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
                Ocorreu um erro ao processar o Ativo Circulante: {mensagem}.
                Verifique os dados de entrada (Ativo Circulante e Passivo Circulante) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe AtivosEvaluator para avaliar o indicador Ativos Totais
class AtivosEvaluator:
    # Construtor que inicializa definição, agrupador e descrição dos Ativos Totais
    def __init__(self):
        # Define string multilinha explicando o índice Ativos Totais
        self.definicao = '''
        Os Ativos Totais representam o valor total dos bens e direitos da empresa, incluindo ativos circulantes (como caixa e recebíveis)
        e não circulantes (como imobilizado e intangíveis). É um indicador de saúde financeira que reflete a capacidade da empresa de financiar
        suas operações e investimentos. Valores altos sugerem robustez, enquanto valores baixos ou estagnados indicam fragilidade ou baixa escala.
        '''
        # Define a categoria de agrupamento como "Saúde Financeira"
        self.agrupador = 'Saúde Financeira'
        # Define a fórmula dos Ativos Totais
        self.formula = 'Ativos Totais = Ativo Circulante + Ativo Não Circulante'

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

    # Avalia o valor dos Ativos Totais em relação à Receita Líquida e retorna um objeto ResultadoIND
    def avaliar(self, ativos_totais, receita_liquida):
        # Tenta processar o valor dos Ativos Totais e Receita Líquida
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(ativos_totais, "Ativos Totais"), (receita_liquida, "Receita Líquida")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Ativos Totais e Receita Líquida para float
            ativos_totais = float(ativos_totais)
            receita_liquida = float(receita_liquida)
            # Calcula a proporção dos Ativos Totais em relação à Receita Líquida
            if receita_liquida == 0:
                raise ValueError("A Receita Líquida não pode ser zero para calcular a proporção.")
            proporcao_ativos_receita = ativos_totais / receita_liquida
            # Verifica se Ativos Totais são negativos, indicando erro nos dados
            if ativos_totais < 0:
                # Retorna ResultadoIND para Ativos Totais negativos
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Ativos Totais < 0',
                    descricao='Ativos Totais negativos são inválidos, indicando erros nos dados financeiros ou relatórios contábeis. Isso pode refletir falhas na consolidação de ativos ou manipulação de informações, tornando a análise de saúde financeira inviável.',
                    riscos='Risco de manipulação contábil ou baixa confiabilidade nos dados financeiros. Pode haver ausência de transparência ou erros graves nos relatórios.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou falta de transparência. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se a proporção está entre 0 e 1, indicando alta eficiência na utilização de ativos
            elif 0 <= proporcao_ativos_receita <= 1:
                # Retorna ResultadoIND para alta eficiência
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= Ativos Totais / Receita Líquida <= 1',
                    descricao='Os Ativos Totais são baixos em relação à receita, indicando alta eficiência na utilização de ativos para gerar vendas. Comum em empresas com modelos leves, como tecnologia ou serviços, sugere robustez financeira e alta produtividade dos ativos.',
                    riscos='Risco de dependência de ativos intangíveis ou baixa capacidade de expansão sem novos investimentos. Pode haver vulnerabilidade a choques de mercado.',
                    referencia='Analise evaluate_giro_ativo para eficiência, evaluate_roe para rentabilidade patrimonial e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade da receita e a qualidade dos ativos. Boa opção para investidores que buscam eficiência.'
                )
            # Verifica se a proporção está entre 1 e 2, indicando boa eficiência
            elif 1 < proporcao_ativos_receita <= 2:
                # Retorna ResultadoIND para boa eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1 < Ativos Totais / Receita Líquida <= 2',
                    descricao='Os Ativos Totais estão em uma faixa equilibrada em relação à receita, indicando boa eficiência na utilização de ativos. Comum em empresas estáveis, como varejo ou manufatura, sugere capacidade de gerar vendas com uma base de ativos moderada.',
                    riscos='Risco de estagnação na receita se os ativos não forem otimizados. Pode haver dependência de ativos fixos ou necessidade de reinvestimento.',
                    referencia='Compare com evaluate_giro_ativo para eficiência, evaluate_margem_liquida para lucratividade e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Considere investir, mas monitore a eficiência operacional e planos de expansão. Boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se a proporção está entre 2 e 4, indicando eficiência moderada
            elif 2 < proporcao_ativos_receita <= 4:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='2 < Ativos Totais / Receita Líquida <= 4',
                    descricao='Os Ativos Totais são moderadamente altos em relação à receita, indicando eficiência limitada na utilização de ativos. Comum em setores intensivos em capital, como indústria ou infraestrutura, sugere dependência de ativos pesados para gerar vendas.',
                    riscos='Risco de baixa produtividade dos ativos ou necessidade de investimentos elevados. Pode haver dificuldades em escalar vendas sem aumentar os ativos.',
                    referencia='Verifique evaluate_roa para rentabilidade dos ativos, evaluate_cash_conversion_cycle para eficiência e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Considere investir com cautela, avaliando a capacidade de otimizar ativos e gerar receita. Priorize empresas com estratégias de eficiência.'
                )
            # Verifica se a proporção está entre 4 e 6, indicando baixa eficiência
            elif 4 < proporcao_ativos_receita <= 6:
                # Retorna ResultadoIND para baixa eficiência
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='4 < Ativos Totais / Receita Líquida <= 6',
                    descricao='Os Ativos Totais são altos em relação à receita, indicando baixa eficiência na utilização de ativos. Comum em empresas com ativos ociosos ou setores de baixa rotatividade, como imobiliário, sugere ineficiência operacional e risco financeiro.',
                    riscos='Risco de ativos subutilizados ou necessidade de desinvestimento. Pode haver dificuldades em manter a lucratividade com alta base de ativos.',
                    referencia='Analise evaluate_giro_ativo para eficiência, evaluate_margem_operacional para lucratividade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir a menos que haja planos claros de otimização de ativos. Monitore a capacidade de aumentar a receita.'
                )
            # Verifica se a proporção excede 6, indicando eficiência crítica
            elif proporcao_ativos_receita > 6:
                # Retorna ResultadoIND para eficiência crítica
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Ativos Totais / Receita Líquida > 6',
                    descricao='Os Ativos Totais são extremamente altos em relação à receita, indicando ineficiência grave na utilização de ativos. Comum em empresas em crise ou com ativos obsoletos, sugere dificuldades financeiras significativas e baixa capacidade de gerar vendas.',
                    riscos='Risco de insolvência, ativos ociosos ou necessidade de reestruturação. Pode haver baixa competitividade ou má gestão de recursos.',
                    referencia='Avalie evaluate_roa para rentabilidade dos ativos, evaluate_liquidez_corrente para liquidez e evaluate_p_vp para valuation patrimonial.',
                    recomendacao='Evite investir devido ao alto risco de ineficiência. Priorize análise de recuperação operacional e estratégias de desinvestimento.'
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
                Ocorreu um erro ao processar os Ativos Totais: {mensagem}.
                Verifique os dados de entrada (Ativos Totais e Receita Líquida) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe DividaLiquidaEvaluator para avaliar o indicador Dívida Líquida
class DividaLiquidaEvaluator:
    # Construtor que inicializa definição, agrupador e descrição da Dívida Líquida
    def __init__(self):
        # Define string multilinha explicando o índice Dívida Líquida
        self.definicao = '''
        A Dívida Líquida representa o total de obrigações financeiras da empresa, descontada a disponibilidade de caixa e equivalentes,
        calculada como (Dívida Bruta - Caixa e Equivalentes de Caixa). É um indicador de alavancagem que avalia o endividamento real,
        considerando os recursos líquidos disponíveis. Um valor baixo ou negativo sugere boa saúde financeira, enquanto valores altos indicam
        maior risco financeiro.
        '''
        # Define a categoria de agrupamento como "Alavancagem"
        self.agrupador = 'Alavancagem'
        # Define a fórmula da Dívida Líquida
        self.formula = 'Dívida Líquida = Dívida Bruta - Caixa e Equivalentes de Caixa'

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

    # Avalia o valor da Dívida Líquida em relação aos Ativos Totais e retorna um objeto ResultadoIND
    def avaliar(self, divida_liquida, ativos_totais):
        # Tenta processar o valor da Dívida Líquida e Ativos Totais
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(divida_liquida, "Dívida Líquida"), (ativos_totais, "Ativos Totais")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Dívida Líquida e Ativos Totais para float
            divida_liquida = float(divida_liquida)
            ativos_totais = float(ativos_totais)
            # Calcula a proporção da Dívida Líquida em relação aos Ativos Totais
            if ativos_totais == 0:
                raise ValueError("Os Ativos Totais não podem ser zero para calcular a proporção.")
            proporcao_divida_ativos = divida_liquida / ativos_totais
            # Verifica se Dívida Líquida é negativa, indicando caixa superior à dívida
            if proporcao_divida_ativos < 0:
                # Retorna ResultadoIND para Dívida Líquida negativa
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dívida Líquida < 0',
                    descricao='Uma Dívida Líquida negativa indica que o caixa e equivalentes superam a dívida bruta, sugerindo robustez financeira. Comum em empresas com forte geração de caixa, como tecnologia ou serviços, isso reflete baixa alavancagem e alta capacidade de honrar obrigações.',
                    riscos='Risco de ineficiência no uso de caixa, com recursos ociosos. Pode haver perda de oportunidades de investimento ou retorno aos acionistas.',
                    referencia='Analise evaluate_roe para rentabilidade patrimonial, evaluate_cash_flow para geração de caixa e evaluate_psr para receita.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de caixa. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se Dívida Líquida é zero, indicando equilíbrio entre dívida e caixa
            elif proporcao_divida_ativos == 0:
                # Retorna ResultadoIND para Dívida Líquida zero
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dívida Líquida = 0',
                    descricao='A Dívida Líquida é zero, indicando que o caixa e equivalentes igualam a dívida bruta. Comum em empresas com gestão financeira sólida, como bens de consumo, isso sugere equilíbrio financeiro e ausência de alavancagem líquida.',
                    riscos='Risco de subalavancagem, limitando crescimento com dívida barata. Pode haver dependência de geração de caixa para manter o equilíbrio.',
                    referencia='Compare com evaluate_debt_to_ebitda para alavancagem operacional, evaluate_liquidez_corrente para liquidez e evaluate_roe para rentabilidade.',
                    recomendacao='Considere investir, mas verifique a estratégia de crescimento e uso de capital. Boa opção para investidores que priorizam estabilidade.'
                )
            # Verifica se a proporção está entre 0 e 0.3, indicando baixa alavancagem
            elif 0 < proporcao_divida_ativos <= 0.3:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0 < Dívida Líquida / Ativos <= 0.3',
                    descricao='A Dívida Líquida é baixa em relação aos ativos, indicando alavancagem moderada e boa saúde financeira. Comum em empresas estáveis, como varejo ou tecnologia, sugere capacidade de gerenciar dívidas com folga, apoiada por reservas de caixa.',
                    riscos='Risco de aumento de dívidas em expansões ou cenários adversos. Pode haver dependência de caixa para manter a baixa alavancagem.',
                    referencia='Verifique evaluate_div_liquida_pl para alavancagem patrimonial, evaluate_margem_liquida para lucratividade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir, mas monitore a política de endividamento e fluxo de caixa. Boa opção para investidores que buscam equilíbrio financeiro.'
                )
            # Verifica se a proporção está entre 0.3 e 0.6, indicando alavancagem moderada
            elif 0.3 < proporcao_divida_ativos <= 0.6:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.3 < Dívida Líquida / Ativos <= 0.6',
                    descricao='A Dívida Líquida está em uma faixa moderada em relação aos ativos, indicando equilíbrio entre dívida e caixa. Comum em empresas de setores como manufatura ou serviços, reflete dependência moderada de financiamento externo, mas com riscos gerenciáveis.',
                    riscos='Risco de pressão financeira se os lucros caírem ou taxas de juros subirem. Pode haver limitações em investimentos ou pagamento de dividendos.',
                    referencia='Compare com evaluate_debt_to_equity para estrutura de dívida, evaluate_ebit_margin para eficiência operacional e evaluate_liquidez_imediata para liquidez.',
                    recomendacao='Considere investir com cautela, avaliando a estabilidade dos lucros e reservas de caixa. Priorize empresas com fluxo de caixa consistente.'
                )
            # Verifica se a proporção está entre 0.6 e 1.0, indicando alta alavancagem
            elif 0.6 < proporcao_divida_ativos <= 1.0:
                # Retorna ResultadoIND para alta alavancagem
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0.6 < Dívida Líquida / Ativos <= 1.0',
                    descricao='A Dívida Líquida é alta em relação aos ativos, indicando elevada alavancagem. Comum em setores intensivos em capital, como infraestrutura ou energia, sugere risco financeiro significativo devido à dependência de dívidas, mesmo considerando o caixa disponível.',
                    riscos='Risco de insolvência em cenários de queda na receita ou aumento de juros. Pode haver restrições de credores ou necessidade de venda de ativos.',
                    referencia='Analise evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_p_vp para valuation patrimonial.',
                    recomendacao='Evite investir a menos que haja forte geração de caixa ou planos de desalavancagem. Monitore a capacidade de pagamento de dívidas.'
                )
            # Verifica se a proporção excede 1.0, indicando alavancagem crítica
            elif proporcao_divida_ativos > 1.0:
                # Retorna ResultadoIND para alavancagem crítica
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dívida Líquida / Ativos > 1.0',
                    descricao='A Dívida Líquida excede os ativos totais, indicando alavancagem extrema e fragilidade financeira grave. Comum em empresas em crise ou com má gestão financeira, sugere alto risco de insolvência e dificuldade em honrar obrigações, mesmo com caixa disponível.',
                    riscos='Risco de falência, reestruturação forçada ou diluição acionária. Pode haver incapacidade de cobrir dívidas ou restrições severas de credores.',
                    referencia='Avalie evaluate_div_liquida_pl para alavancagem patrimonial, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
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
                Ocorreu um erro ao processar a Dívida Líquida: {mensagem}.
                Verifique os dados de entrada (Dívida Líquida e Ativos Totais) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe DividaBrutaEvaluator para avaliar o indicador Dívida Bruta
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
# Define a classe PatrimonioLiquidoEvaluator para avaliar o indicador Patrimônio Líquido
class PatrimonioLiquidoEvaluator:
    # Construtor que inicializa definição, agrupador e descrição do Patrimônio Líquido
    def __init__(self):
        # Define string multilinha explicando o índice Patrimônio Líquido
        self.definicao = '''
        O Patrimônio Líquido representa o valor contábil dos recursos próprios da empresa, calculado como (Ativos Totais - Passivos Totais).
        É um indicador de saúde financeira que mostra o valor residual pertencente aos acionistas após o pagamento de todas as dívidas.
        Um valor alto sugere solidez financeira, enquanto valores baixos ou negativos indicam fragilidade ou endividamento excessivo.
        '''
        # Define a categoria de agrupamento como "Saúde Financeira"
        self.agrupador = 'Saúde Financeira'
        # Define a fórmula do Patrimônio Líquido
        self.formula = 'Patrimônio Líquido = Ativos Totais - Passivos Totais'

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

    # Avalia o valor do Patrimônio Líquido e retorna um objeto ResultadoIND
    def avaliar(self, patrimonio_liquido, ativos_totais=None):
        # Tenta processar o valor do Patrimônio Líquido e Ativos Totais
        try:
            # Verifica se as entradas são numéricas (int ou float) ou strings que podem ser convertidas
            for param, nome in [(patrimonio_liquido, "Patrimônio Líquido"), (ativos_totais, "Ativos Totais")]:
                if not isinstance(param, (int, float)) and not (isinstance(param, str) and param.replace('.', '', 1).isdigit()):
                    raise ValueError(f"O valor de {nome} deve ser numérico.")
            # Converte Patrimônio Líquido e Ativos Totais para float
            patrimonio_liquido = float(patrimonio_liquido)
            ativos_totais = float(ativos_totais)
            # Calcula a proporção do Patrimônio Líquido em relação aos Ativos Totais
            if ativos_totais == 0:
                raise ValueError("Os Ativos Totais não podem ser zero para calcular a proporção.")
            #proporcao_pl_ativos = patrimonio_liquido / ativos_totais
            proporcao_pl_ativos = patrimonio_liquido
            # Verifica se Patrimônio Líquido é negativo, indicando problemas financeiros graves
            if proporcao_pl_ativos < 0:
                # Retorna ResultadoIND para Patrimônio Líquido negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Patrimônio Líquido < 0',
                    descricao='Um Patrimônio Líquido negativo indica que os passivos superam os ativos, sugerindo prejuízos acumulados ou endividamento excessivo. Comum em empresas em crise ou com alta alavancagem, isso aponta para instabilidade financeira e risco elevado para acionistas.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver incapacidade de cobrir dívidas ou gerar valor para acionistas.',
                    referencia='Avalie evaluate_div_liquida_pl para alavancagem, evaluate_cash_flow para geração de caixa e evaluate_roe para rentabilidade.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação patrimonial. Priorize análise de turnaround e saúde financeira.'
                )
            # Verifica se a proporção está entre 0 e 0.2, indicando alta alavancagem
            elif 0 <= proporcao_pl_ativos <= 0.2:
                # Retorna ResultadoIND para alta alavancagem
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Patrimônio Líquido / Ativos <= 0.2',
                    descricao='O Patrimônio Líquido é baixo em relação aos ativos, indicando alta alavancagem, com a maior parte dos ativos financiada por dívidas. Comum em setores intensivos em capital, como energia ou infraestrutura, mas implica maior risco financeiro devido à dependência de credores.',
                    riscos='Risco de insolvência em cenários adversos, como aumento de juros ou queda na receita. Pode haver restrições de credores ou venda de ativos.',
                    referencia='Analise evaluate_debt_to_assets para estrutura de dívida, evaluate_ebit_margin para eficiência operacional e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Evite investir a menos que haja forte geração de caixa ou planos de desalavancagem. Monitore a capacidade de pagamento de dívidas.'
                )
            # Verifica se a proporção está entre 0.2 e 0.4, indicando alavancagem moderada
            elif 0.2 < proporcao_pl_ativos <= 0.4:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.2 < Patrimônio Líquido / Ativos <= 0.4',
                    descricao='O Patrimônio Líquido está em uma faixa moderada em relação aos ativos, indicando equilíbrio razoável entre capital próprio e dívida. Comum em empresas estáveis, como manufatura ou varejo, mas ainda reflete dependência significativa de financiamento externo.',
                    riscos='Risco de pressão financeira se os lucros caírem ou taxas de juros subirem. Pode haver limitações em novos investimentos ou dividendos.',
                    referencia='Compare com evaluate_div_liquida_pl para alavancagem, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
                    recomendacao='Considere investir com cautela, avaliando a estabilidade dos lucros e planos de redução de dívida. Priorize empresas com fluxo de caixa consistente.'
                )
            # Verifica se a proporção está entre 0.4 e 0.6, indicando boa estrutura financeira
            elif 0.4 < proporcao_pl_ativos <= 0.6:
                # Retorna ResultadoIND para boa estrutura financeira
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.4 < Patrimônio Líquido / Ativos <= 0.6',
                    descricao='O Patrimônio Líquido está em uma faixa saudável, indicando que uma proporção significativa dos ativos é financiada por capital próprio. Comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugerindo estabilidade e menor dependência de dívida.',
                    riscos='Risco de subalavancagem, perdendo oportunidades de crescimento com dívida barata. Pode haver ineficiência no uso de capital próprio.',
                    referencia='Verifique evaluate_roe para rentabilidade patrimonial, evaluate_margem_operacional para eficiência e evaluate_debt_to_ebitda para alavancagem.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de capital e planos de crescimento. Boa opção para investidores que buscam segurança.'
                )
            # Verifica se a proporção excede 0.6, indicando robustez financeira
            elif proporcao_pl_ativos > 0.6:
                # Retorna ResultadoIND para robustez financeira
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Patrimônio Líquido / Ativos > 0.6',
                    descricao='O Patrimônio Líquido é extremamente alto em relação aos ativos, indicando baixa alavancagem e robustez financeira. Típico de empresas com forte geração de caixa ou baixa necessidade de capital, como software ou serviços especializados, refletindo solidez financeira.',
                    riscos='Risco de ineficiência no uso de capital, com excesso de capital próprio ocioso. Pode haver perda de oportunidades de crescimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_roe para rentabilidade patrimonial, evaluate_psr para receita e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de capital. Considere empresas com planos de reinvestimento ou dividendos.'
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
                Ocorreu um erro ao processar o Patrimônio Líquido: {mensagem}.
                Verifique os dados de entrada (Patrimônio Líquido e Ativos Totais) e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe LiquidezMediaDiariaEvaluator para avaliar o indicador Liquidez Média Diária
class LiquidezMediaDiariaEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula da Liquidez Média Diária
    def __init__(self):
        # Define string multilinha explicando o índice Liquidez Média Diária
        self.definicao = '''
        A Liquidez Média Diária mede o volume financeiro médio negociado de uma ação por dia, geralmente em reais, dólares ou outra moeda,
        calculado como o valor total negociado em um período dividido pelo número de dias. É um indicador de liquidez de mercado que avalia a facilidade
        de comprar ou vender uma ação sem impactar significativamente seu preço. Um valor alto sugere alta liquidez, enquanto valores baixos indicam dificuldade
        em negociar a ação.
        '''
        # Define a categoria de agrupamento como "Liquidez de Mercado"
        self.agrupador = 'Liquidez de Mercado'
        # Define a fórmula da Liquidez Média Diária
        self.formula = 'Liquidez Média Diária = Valor Total Negociado / Número de Dias'

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

    # Avalia o valor da Liquidez Média Diária e retorna um objeto ResultadoIND
    def avaliar(self, liquidez_media_diaria):
        # Tenta processar o valor da Liquidez Média Diária
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(liquidez_media_diaria, (int, float)) and not (isinstance(liquidez_media_diaria, str) and liquidez_media_diaria.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Liquidez Média Diária deve ser numérico.")
            # Converte a Liquidez Média Diária para float para garantir que é numérico
            liquidez_media_diaria = float(liquidez_media_diaria)
            # Verifica se Liquidez Média Diária é negativa, indicando erro
            if liquidez_media_diaria < 0:
                # Retorna ResultadoIND para Liquidez Média Diária negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Liquidez Média Diária < 0',
                    descricao='Uma Liquidez Média Diária negativa é inválida, indicando erros nos dados de negociação ou ausência de volume negociado. Isso pode refletir falhas no mercado, manipulação de dados ou ações suspensas, tornando a análise de liquidez inviável.',
                    riscos='Risco de manipulação de dados ou ausência de mercado ativo. Pode haver impossibilidade de negociar a ação ou baixa confiabilidade nos dados financeiros.',
                    referencia='Avalie evaluate_volume_negociado para confirmação de volume, evaluate_beta para volatilidade e evaluate_market_share para relevância de mercado.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou ausência de mercado ativo. Verifique relatórios de negociação e status da ação.'
                )
            # Verifica se Liquidez Média Diária está entre 0 e 100,000, indicando liquidez muito baixa
            elif 0 <= liquidez_media_diaria <= 100000:
                # Retorna ResultadoIND para liquidez muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Liquidez Média Diária <= 100.000',
                    descricao='A Liquidez Média Diária está muito baixa, indicando dificuldade significativa para comprar ou vender a ação sem impactar seu preço. Essa faixa é comum em empresas de baixa capitalização ou com pouco interesse de mercado, como small caps ou setores de nicho.',
                    riscos='Risco de baixa negociabilidade, spreads elevados ou dificuldade de saída do investimento. Pode haver volatilidade excessiva ou manipulação de preços.',
                    referencia='Analise evaluate_free_float para proporção de ações disponíveis, evaluate_beta para volatilidade e evaluate_p_l para valuation.',
                    recomendacao='Evite investir, a menos que tolere baixa liquidez e alta volatilidade. Priorize análise de volume de negociação e interesse de mercado.'
                )
            # Verifica se Liquidez Média Diária está entre 100,000 e 500,000, indicando liquidez moderada
            elif 100000 < liquidez_media_diaria <= 500000:
                # Retorna ResultadoIND para liquidez moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='100.000 < Liquidez Média Diária <= 500.000',
                    descricao='A Liquidez Média Diária está em uma faixa moderada, sugerindo facilidade razoável para negociar a ação, mas com limitações em grandes volumes. Essa faixa é comum em empresas de média capitalização ou setores com interesse moderado, como varejo ou indústria.',
                    riscos='Risco de spreads elevados em negociações de grande volume ou em momentos de estresse de mercado. Pode haver dependência de investidores institucionais.',
                    referencia='Compare com evaluate_volume_negociado para consistência de volume, evaluate_p_vp para valuation patrimonial e evaluate_market_share para competitividade.',
                    recomendacao='Considere investir com cautela, monitorando o volume de negociação e a volatilidade. Boa opção para investidores que aceitam liquidez moderada.'
                )
            # Verifica se Liquidez Média Diária está entre 500,000 e 2,000,000, indicando boa liquidez
            elif 500000 < liquidez_media_diaria <= 2000000:
                # Retorna ResultadoIND para boa liquidez
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='500.000 < Liquidez Média Diária <= 2.000.000',
                    descricao='A Liquidez Média Diária está em uma faixa saudável, indicando boa facilidade para comprar ou vender a ação sem impacto significativo no preço. Essa faixa é comum em empresas de grande capitalização ou setores populares, como tecnologia ou bens de consumo.',
                    riscos='Risco de redução na liquidez em cenários de baixa demanda ou crises de mercado. Pode haver dependência de investidores institucionais para manter o volume.',
                    referencia='Verifique evaluate_free_float para disponibilidade de ações, evaluate_beta para volatilidade e evaluate_cash_flow para saúde financeira.',
                    recomendacao='Considere investir, mas monitore a consistência do volume de negociação. Boa opção para investidores que buscam liquidez e estabilidade.'
                )
            # Verifica se Liquidez Média Diária excede 2,000,000, indicando liquidez excepcional
            elif liquidez_media_diaria > 2000000:
                # Retorna ResultadoIND para liquidez excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Liquidez Média Diária > 2.000.000',
                    descricao='A Liquidez Média Diária é extremamente alta, indicando facilidade excepcional para negociar a ação, mesmo em grandes volumes. Essa faixa é típica de empresas de alta capitalização, blue chips ou setores de grande interesse, como financeiro ou tecnologia, refletindo forte presença no mercado.',
                    riscos='Risco de sobreexposição a movimentos de mercado ou manipulação por grandes investidores. Pode haver volatilidade em crises sistêmicas.',
                    referencia='Combine com evaluate_p_l para valuation, evaluate_beta para volatilidade e evaluate_dividend_yield para retorno de dividendos.',
                    recomendacao='Invista se os fundamentos suportarem, mas diversifique para mitigar riscos de mercado. Boa opção para investidores que buscam alta negociabilidade.'
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
                Ocorreu um erro ao processar a Liquidez Média Diária: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe PatrimonioAtivosEvaluator para avaliar o indicador Patrimônio Líquido / Ativos
class PatrimonioAtivosEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do Patrimônio/Ativos
    def __init__(self):
        # Define string multilinha explicando o índice Patrimônio/Ativos
        self.definicao = '''
        O Patrimônio/Ativos (Patrimônio Líquido sobre Ativos) mede a proporção do patrimônio líquido em relação aos ativos totais da empresa,
        calculado como (Patrimônio Líquido / Ativos Totais). É um indicador de estrutura de capital que avalia o grau de financiamento
        dos ativos por capital próprio versus dívida. Um valor alto sugere baixa alavancagem, enquanto valores baixos ou negativos indicam
        alta dependência de dívida ou fragilidade financeira.
        '''
        # Define a categoria de agrupamento como "Estrutura de Capital"
        self.agrupador = 'Estrutura de Capital'
        # Define a fórmula do Patrimônio/Ativos
        self.formula = 'Patrimônio/Ativos = Patrimônio Líquido / Ativos Totais'

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

    # Avalia o valor do Patrimônio/Ativos e retorna um objeto ResultadoIND
    def avaliar(self, patrimonio_ativos):
        # Tenta processar o valor do Patrimônio/Ativos
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(patrimonio_ativos, (int, float)) and not (isinstance(patrimonio_ativos, str) and patrimonio_ativos.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do Patrimônio/Ativos deve ser numérico.")
            # Converte o Patrimônio/Ativos para float para garantir que é numérico
            patrimonio_ativos = float(patrimonio_ativos)
            # Verifica se Patrimônio/Ativos é negativo, indicando patrimônio líquido negativo
            if patrimonio_ativos < 0:
                # Retorna ResultadoIND para Patrimônio/Ativos negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Patrimônio/Ativos < 0',
                    descricao='Um Patrimônio/Ativos negativo indica que o patrimônio líquido é negativo, sugerindo prejuízos acumulados ou problemas financeiros graves. Isso ocorre quando as dívidas superam os ativos líquidos, comum em empresas em crise ou com alta alavancagem, apontando para instabilidade financeira.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver endividamento excessivo ou incapacidade de gerar valor para acionistas.',
                    referencia='Avalie evaluate_roe para rentabilidade patrimonial, evaluate_div_liquida_pl para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação patrimonial. Priorize análise de turnaround e saúde financeira.'
                )
            # Verifica se Patrimônio/Ativos está entre 0 e 0.2, indicando alta alavancagem
            elif 0 <= patrimonio_ativos <= 0.2:
                # Retorna ResultadoIND para alta alavancagem
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Patrimônio/Ativos <= 0.2',
                    descricao='O Patrimônio/Ativos está muito baixo, indicando que a maior parte dos ativos é financiada por dívidas, sugerindo alta alavancagem. Essa faixa é comum em setores intensivos em capital, como infraestrutura ou energia, mas implica maior risco financeiro devido à dependência de credores.',
                    riscos='Risco de insolvência em cenários adversos, como aumento de juros ou queda na receita. Pode haver restrições de credores ou necessidade de venda de ativos.',
                    referencia='Analise evaluate_debt_to_assets para estrutura de dívida, evaluate_ebit_margin para eficiência operacional e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Evite investir a menos que haja forte geração de caixa ou planos de desalavancagem. Monitore a capacidade de pagamento de dívidas.'
                )
            # Verifica se Patrimônio/Ativos está entre 0.2 e 0.4, indicando alavancagem moderada
            elif 0.2 < patrimonio_ativos <= 0.4:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.2 < Patrimônio/Ativos <= 0.4',
                    descricao='O Patrimônio/Ativos está em uma faixa moderada, indicando um equilíbrio razoável entre capital próprio e dívida no financiamento dos ativos. Essa faixa é comum em empresas com operações estáveis, como manufatura ou varejo, mas ainda reflete dependência significativa de financiamento externo.',
                    riscos='Risco de pressão financeira se os lucros caírem ou taxas de juros subirem. Pode haver limitações em novos investimentos ou distribuições aos acionistas.',
                    referencia='Compare com evaluate_div_liquida_pl para alavancagem, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
                    recomendacao='Considere investir com cautela, avaliando a estabilidade dos lucros e planos de redução de dívida. Priorize empresas com fluxo de caixa consistente.'
                )
            # Verifica se Patrimônio/Ativos está entre 0.4 e 0.6, indicando boa estrutura de capital
            elif 0.4 < patrimonio_ativos <= 0.6:
                # Retorna ResultadoIND para boa estrutura de capital
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.4 < Patrimônio/Ativos <= 0.6',
                    descricao='O Patrimônio/Ativos está em uma faixa saudável, indicando que uma proporção significativa dos ativos é financiada por capital próprio. Essa faixa é comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugerindo estabilidade e menor dependência de dívida.',
                    riscos='Risco de subalavancagem, onde a empresa pode perder oportunidades de crescimento por não usar dívida barata. Pode haver ineficiência no uso de capital próprio.',
                    referencia='Verifique evaluate_roe para rentabilidade patrimonial, evaluate_margem_operacional para eficiência e evaluate_debt_to_ebitda para alavancagem operacional.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de capital e planos de crescimento. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se Patrimônio/Ativos excede 0.6, indicando baixa alavancagem
            elif patrimonio_ativos > 0.6:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Patrimônio/Ativos > 0.6',
                    descricao='O Patrimônio/Ativos é extremamente alto, indicando que a maior parte dos ativos é financiada por capital próprio, sugerindo baixa alavancagem e robustez financeira. Essa faixa é típica de empresas com forte geração de caixa ou baixa necessidade de capital, como software ou serviços especializados.',
                    riscos='Risco de ineficiência no uso de capital, com excesso de capital próprio ocioso. Pode haver perda de oportunidades de crescimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_roe para rentabilidade patrimonial, evaluate_psr para receita e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de capital. Considere empresas com planos de reinvestimento ou dividendos.'
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
                Ocorreu um erro ao processar o Patrimônio/Ativos: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe PAtivoCirculanteLiquidoEvaluator para avaliar o indicador Preço sobre Ativo Circulante Líquido
class PAtivoCirculanteLiquidoEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/Ativo Circulante Líquido
    def __init__(self):
        # Define string multilinha explicando o índice P/Ativo Circulante Líquido
        self.definicao = '''
        O P/Ativo Circulante Líquido mede o valor de mercado da empresa em relação ao seu ativo circulante líquido, calculado
        como (Valor de Mercado / Ativo Circulante Líquido), onde Ativo Circulante Líquido é o Ativo Circulante menos o Passivo Circulante.
        É um indicador de valuation que avalia a relação entre o preço da empresa e sua liquidez de curto prazo. Um valor baixo sugere
        subvalorização ou alta liquidez, enquanto valores altos indicam sobrevalorização ou baixa liquidez operacional.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/Ativo Circulante Líquido
        self.formula = 'P/Ativo Circulante Líquido = Valor de Mercado / (Ativo Circulante - Passivo Circulante)'

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

    # Avalia o valor do P/Ativo Circulante Líquido e retorna um objeto ResultadoIND
    def avaliar(self, p_ativo_circulante_liquido):
        # Tenta processar o valor do P/Ativo Circulante Líquido
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_ativo_circulante_liquido, (int, float)) and not (isinstance(p_ativo_circulante_liquido, str) and p_ativo_circulante_liquido.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do P/Ativo Circulante Líquido deve ser numérico.")
            # Converte o P/Ativo Circulante Líquido para float para garantir que é numérico
            p_ativo_circulante_liquido = float(p_ativo_circulante_liquido)
            # Verifica se P/Ativo Circulante Líquido é negativo, indicando ativo circulante líquido negativo
            if p_ativo_circulante_liquido < 0:
                # Retorna ResultadoIND para P/Ativo Circulante Líquido negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/Ativo Circulante Líquido < 0',
                    descricao='Um P/Ativo Circulante Líquido negativo indica que o ativo circulante líquido é negativo, ou seja, o passivo circulante excede o ativo circulante. Isso sugere problemas graves de liquidez de curto prazo, comum em empresas em crise ou com má gestão financeira, indicando risco de insolvência.',
                    riscos='Risco de falência, incapacidade de honrar obrigações de curto prazo ou necessidade de financiamento emergencial. Pode haver baixa confiabilidade financeira.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação da liquidez. Priorize análise de fluxo de caixa e estratégias de reestruturação financeira.'
                )
            # Verifica se P/Ativo Circulante Líquido está entre 0 e 5, indicando forte subvalorização
            elif 0 <= p_ativo_circulante_liquido <= 5:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/Ativo Circulante Líquido <= 5',
                    descricao='O P/Ativo Circulante Líquido está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação à sua liquidez operacional. Essa faixa indica oportunidades de compra, comum em empresas com forte ativo circulante líquido, mas preço de mercado deprimido devido a ciclos econômicos.',
                    riscos='Risco de ativo circulante de baixa qualidade, como estoques obsoletos ou recebíveis duvidosos. Pode haver ineficiência no uso de recursos líquidos.',
                    referencia='Analise evaluate_liquidez_corrente para liquidez, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
                    recomendacao='Considere investir, mas verifique a qualidade do ativo circulante e a eficiência operacional. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/Ativo Circulante Líquido está entre 5 e 10, indicando valuation equilibrado
            elif 5 < p_ativo_circulante_liquido <= 10:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='5 < P/Ativo Circulante Líquido <= 10',
                    descricao='O P/Ativo Circulante Líquido está em uma faixa equilibrada, sugerindo que o valor de mercado está alinhado com a liquidez operacional da empresa. Essa faixa é comum em empresas estáveis com ativo circulante líquido adequado, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação na liquidez devido a aumento de passivos circulantes ou queda na receita. Pode haver dependência de fatores macroeconômicos afetando o ativo circulante.',
                    referencia='Compare com evaluate_p_ebitda para valuation operacional, evaluate_current_ratio para liquidez e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de liquidez e estratégias de gestão de ativos circulantes antes de investir. Boa opção para investidores que buscam estabilidade financeira.'
                )
            # Verifica se P/Ativo Circulante Líquido está entre 10 e 15, indicando valuation moderado
            elif 10 < p_ativo_circulante_liquido <= 15:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='10 < P/Ativo Circulante Líquido <= 15',
                    descricao='O P/Ativo Circulante Líquido está moderadamente elevado, indicando que o mercado atribui um prêmio à liquidez operacional da empresa. Essa faixa sugere expectativas de crescimento ou confiança na gestão de caixa, comum em empresas com potencial moderado ou setores estáveis.',
                    riscos='Risco de correção no preço se o ativo circulante líquido diminuir ou as obrigações de curto prazo aumentarem. Pode haver sobrevalorização devido a otimismo de mercado.',
                    referencia='Verifique evaluate_p_vp para valuation patrimonial, evaluate_beta para volatilidade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere esperar por sinais de melhoria na liquidez ou redução no valuation antes de investir. Combine com análise de fluxo de caixa e margens.'
                )
            # Verifica se P/Ativo Circulante Líquido está entre 15 e 20, indicando sobrevalorização
            elif 15 < p_ativo_circulante_liquido <= 20:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='15 < P/Ativo Circulante Líquido <= 20',
                    descricao='O P/Ativo Circulante Líquido está consideravelmente elevado, indicando sobrevalorização em relação à liquidez operacional. Essa faixa é comum em empresas com altas expectativas de crescimento ou setores premium, mas o preço reflete otimismo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se o ativo circulante líquido não suportar as expectativas. Pode haver dependência de ativos circulantes de baixa qualidade ou bolhas setoriais.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para lucratividade e evaluate_current_ratio para liquidez.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com forte gestão de caixa e fundamentos sólidos.'
                )
            # Verifica se P/Ativo Circulante Líquido excede 20, indicando sobrevalorização extrema
            elif p_ativo_circulante_liquido > 20:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='P/Ativo Circulante Líquido > 20',
                    descricao='O P/Ativo Circulante Líquido é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de liquidez operacional. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço desconecta dos fundamentos financeiros.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de narrativas de mercado ou baixa liquidez operacional.',
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
                Ocorreu um erro ao processar o P/Ativo Circulante Líquido: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe PLAtivosEvaluator para avaliar o indicador Patrimônio Líquido / Ativos
class PLAtivosEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do PL/Ativos
    def __init__(self):
        # Define string multilinha explicando o índice PL/Ativos
        self.definicao = '''
        O PL/Ativos (Patrimônio Líquido sobre Ativos) mede a proporção do patrimônio líquido em relação aos ativos totais da empresa,
        calculado como (Patrimônio Líquido / Ativos Totais). É um indicador de estrutura de capital que avalia o grau de financiamento
        dos ativos por capital próprio versus dívida. Um valor alto sugere baixa alavancagem, enquanto valores baixos ou negativos indicam
        alta dependência de dívida ou fragilidade financeira.
        '''
        # Define a categoria de agrupamento como "Estrutura de Capital"
        self.agrupador = 'Estrutura de Capital'
        # Define a fórmula do PL/Ativos
        self.formula = 'PL/Ativos = Patrimônio Líquido / Ativos Totais'

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

    # Avalia o valor do PL/Ativos e retorna um objeto ResultadoIND
    def avaliar(self, pl_ativos):
        # Tenta processar o valor do PL/Ativos
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(pl_ativos, (int, float)) and not (isinstance(pl_ativos, str) and pl_ativos.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do PL/Ativos deve ser numérico.")
            # Converte o PL/Ativos para float para garantir que é numérico
            pl_ativos = float(pl_ativos)
            # Verifica se PL/Ativos é negativo, indicando patrimônio líquido negativo
            if pl_ativos < 0:
                # Retorna ResultadoIND para PL/Ativos negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='PL/Ativos < 0',
                    descricao='Um PL/Ativos negativo indica que o patrimônio líquido é negativo, sugerindo prejuízos acumulados ou problemas financeiros graves. Isso ocorre quando as dívidas superam os ativos líquidos, comum em empresas em crise ou com alta alavancagem, apontando para instabilidade financeira.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver endividamento excessivo ou incapacidade de gerar valor para acionistas.',
                    referencia='Avalie evaluate_roe para rentabilidade patrimonial, evaluate_div_liquida_pl para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação patrimonial. Priorize análise de turnaround e saúde financeira.'
                )
            # Verifica se PL/Ativos está entre 0 e 0.2, indicando alta alavancagem
            elif 0 <= pl_ativos <= 0.2:
                # Retorna ResultadoIND para alta alavancagem
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= PL/Ativos <= 0.2',
                    descricao='O PL/Ativos está muito baixo, indicando que a maior parte dos ativos é financiada por dívidas, sugerindo alta alavancagem. Essa faixa é comum em setores intensivos em capital, como infraestrutura ou energia, mas implica maior risco financeiro devido à dependência de credores.',
                    riscos='Risco de insolvência em cenários adversos, como aumento de juros ou queda na receita. Pode haver restrições de credores ou necessidade de venda de ativos.',
                    referencia='Analise evaluate_debt_to_assets para estrutura de dívida, evaluate_ebit_margin para eficiência operacional e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Evite investir a menos que haja forte geração de caixa ou planos de desalavancagem. Monitore a capacidade de pagamento de dívidas.'
                )
            # Verifica se PL/Ativos está entre 0.2 e 0.4, indicando alavancagem moderada
            elif 0.2 < pl_ativos <= 0.4:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.2 < PL/Ativos <= 0.4',
                    descricao='O PL/Ativos está em uma faixa moderada, indicando um equilíbrio razoável entre capital próprio e dívida no financiamento dos ativos. Essa faixa é comum em empresas com operações estáveis, como manufatura ou varejo, mas ainda reflete dependência significativa de financiamento externo.',
                    riscos='Risco de pressão financeira se os lucros caírem ou taxas de juros subirem. Pode haver limitações em novos investimentos ou distribuições aos acionistas.',
                    referencia='Compare com evaluate_div_liquida_pl para alavancagem, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
                    recomendacao='Considere investir com cautela, avaliando a estabilidade dos lucros e planos de redução de dívida. Priorize empresas com fluxo de caixa consistente.'
                )
            # Verifica se PL/Ativos está entre 0.4 e 0.6, indicando boa estrutura de capital
            elif 0.4 < pl_ativos <= 0.6:
                # Retorna ResultadoIND para boa estrutura de capital
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.4 < PL/Ativos <= 0.6',
                    descricao='O PL/Ativos está em uma faixa saudável, indicando que uma proporção significativa dos ativos é financiada por capital próprio. Essa faixa é comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugerindo estabilidade e menor dependência de dívida.',
                    riscos='Risco de subalavancagem, onde a empresa pode perder oportunidades de crescimento por não usar dívida barata. Pode haver ineficiência no uso de capital próprio.',
                    referencia='Verifique evaluate_roe para rentabilidade patrimonial, evaluate_margem_operacional para eficiência e evaluate_debt_to_ebitda para alavancagem operacional.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de capital e planos de crescimento. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se PL/Ativos excede 0.6, indicando baixa alavancagem
            elif pl_ativos > 0.6:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='PL/Ativos > 0.6',
                    descricao='O PL/Ativos é extremamente alto, indicando que a maior parte dos ativos é financiada por capital próprio, sugerindo baixa alavancagem e robustez financeira. Essa faixa é típica de empresas com forte geração de caixa ou baixa necessidade de capital, como software ou serviços especializados.',
                    riscos='Risco de ineficiência no uso de capital, com excesso de capital próprio ocioso. Pode haver perda de oportunidades de crescimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_roe para rentabilidade patrimonial, evaluate_psr para receita e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de capital. Considere empresas com planos de reinvestimento ou dividendos.'
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
                Ocorreu um erro ao processar o PL/Ativos: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe DividendYieldEvaluator para avaliar o indicador Dividend Yield (DY)
class DividendYieldEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do Dividend Yield
    def __init__(self):
        # Define string multilinha explicando o índice Dividend Yield
        self.definicao = '''
        O Dividend Yield (DY) mede o retorno anual dos dividendos pagos por ação em relação ao preço da ação, calculado
        como (Dividendos por Ação / Preço da Ação) * 100. É um indicador de rentabilidade para investidores que buscam
        renda passiva. Um DY alto sugere bom retorno de dividendos, enquanto valores baixos podem indicar baixa distribuição
        de lucros ou expectativas de crescimento.
        '''
        # Define a categoria de agrupamento como "Rentabilidade"
        self.agrupador = 'Rentabilidade'
        # Define a fórmula do Dividend Yield
        self.formula = 'Dividend Yield (%) = (Dividendos por Ação / Preço da Ação) * 100'

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

    # Avalia o valor do Dividend Yield e retorna um objeto ResultadoIND
    def avaliar(self, dividend_yield):
        # Tenta processar o valor do Dividend Yield
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(dividend_yield, (int, float)) and not (isinstance(dividend_yield, str) and dividend_yield.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do Dividend Yield deve ser numérico.")
            # Converte o Dividend Yield para float para garantir que é numérico
            dividend_yield = float(dividend_yield)
            # Verifica se Dividend Yield é menor que 0, indicando erro ou dividendos negativos
            if dividend_yield < 0:
                # Retorna ResultadoIND para Dividend Yield negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dividend Yield < 0%',
                    descricao='Um Dividend Yield negativo é inválido, indicando dividendos negativos ou erros nos dados financeiros. Isso pode ocorrer em empresas que não pagam dividendos ou com problemas contábeis, inviabilizando a análise de retorno de dividendos.',
                    riscos='Risco de manipulação contábil ou ausência de política de dividendos. Pode haver baixa confiabilidade nos dados financeiros ou instabilidade operacional.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_cash_flow para geração de caixa e evaluate_p_l para valuation.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou ausência de dividendos. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se Dividend Yield é 0, indicando ausência de dividendos
            elif dividend_yield == 0:
                # Retorna ResultadoIND para ausência de dividendos
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dividend Yield = 0%',
                    descricao='Um Dividend Yield de 0% indica que a empresa não paga dividendos, comum em empresas de crescimento que reinvestem lucros ou em empresas com dificuldades financeiras. Isso pode refletir uma estratégia de retenção de capital ou baixa lucratividade.',
                    riscos='Risco de baixa atratividade para investidores que buscam renda passiva. Pode haver incerteza sobre a capacidade de gerar lucros distribuíveis no futuro.',
                    referencia='Analise evaluate_p_l para valuation, evaluate_growth_rate para crescimento e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere investir apenas se o foco for crescimento de capital e não renda. Avalie a estratégia de reinvestimento e a saúde financeira da empresa.'
                )
            # Verifica se Dividend Yield está entre 0 e 2, indicando retorno baixo
            elif 0 < dividend_yield <= 2:
                # Retorna ResultadoIND para retorno baixo
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 < Dividend Yield <= 2%',
                    descricao='O Dividend Yield está baixo, sugerindo retorno limitado via dividendos em relação ao preço da ação. Essa faixa é comum em empresas de crescimento, como tecnologia, que priorizam reinvestimento de lucros, ou em empresas com margens apertadas e baixa distribuição.',
                    riscos='Risco de baixa atratividade para investidores que buscam renda passiva. Pode haver dependência de crescimento futuro ou lucros instáveis para sustentar dividendos.',
                    referencia='Compare com evaluate_p_l para valuation, evaluate_margem_liquida para lucratividade e evaluate_peg_ratio para crescimento.',
                    recomendacao='Considere investir apenas se alinhado com crescimento de capital. Verifique a sustentabilidade dos lucros e planos de distribuição de dividendos.'
                )
            # Verifica se Dividend Yield está entre 2 e 4, indicando retorno moderado
            elif 2 < dividend_yield <= 4:
                # Retorna ResultadoIND para retorno moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='2 < Dividend Yield <= 4%',
                    descricao='O Dividend Yield está em uma faixa moderada, indicando retorno razoável via dividendos. Essa faixa é comum em empresas estáveis, como utilities ou bens de consumo, que distribuem lucros de forma consistente, mas sem priorizar altos retornos de dividendos.',
                    riscos='Risco de estagnação nos dividendos devido a concorrência ou custos crescentes. Pode haver dependência de lucros estáveis para manter a distribuição.',
                    referencia='Verifique evaluate_p_vp para valuation patrimonial, evaluate_roe para rentabilidade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Boa opção para investidores que buscam renda moderada e estabilidade. Avalie a consistência dos lucros e a política de dividendos.'
                )
            # Verifica se Dividend Yield está entre 4 e 6, indicando bom retorno
            elif 4 < dividend_yield <= 6:
                # Retorna ResultadoIND para bom retorno
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='4 < Dividend Yield <= 6%',
                    descricao='O Dividend Yield está em uma faixa alta, sugerindo bom retorno via dividendos em relação ao preço da ação. Essa faixa é comum em empresas maduras com forte geração de caixa, como bancos ou energia, indicando capacidade de distribuição robusta para acionistas.',
                    riscos='Risco de dependência de setores cíclicos ou lucros instáveis. Pode haver cortes nos dividendos se a lucratividade diminuir ou surgirem despesas inesperadas.',
                    referencia='Combine com evaluate_margem_liquida para lucratividade, evaluate_p_l para valuation e evaluate_debt_to_equity para alavancagem.',
                    recomendacao='Considere investir para renda, mas monitore a sustentabilidade dos dividendos e a saúde financeira. Boa opção para investidores focados em dividendos.'
                )
            # Verifica se Dividend Yield excede 6, indicando retorno excepcional
            elif dividend_yield > 6:
                # Retorna ResultadoIND para retorno excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dividend Yield > 6%',
                    descricao='O Dividend Yield é extremamente alto, indicando retorno excepcional via dividendos. Essa faixa é típica de empresas com forte geração de caixa e política agressiva de distribuição, como utilities ou REITs, mas pode também sinalizar empresas em declínio com preços deprimidos.',
                    riscos='Risco de dividendos insustentáveis, especialmente se o preço da ação caiu significativamente. Pode haver problemas financeiros ou dependência de setores maduros.',
                    referencia='Analise evaluate_p_l para valuation, evaluate_cash_flow para geração de caixa e evaluate_beta para volatilidade.',
                    recomendacao='Invista com cautela, verificando a sustentabilidade dos dividendos e a saúde financeira. Diversifique para mitigar riscos de cortes ou instabilidade.'
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
                Ocorreu um erro ao processar o Dividend Yield: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe PCapitalGiroEvaluator para avaliar o indicador Preço sobre Capital de Giro
class PCapitalGiroEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/Capital de Giro
    def __init__(self):
        # Define string multilinha explicando o índice P/Capital de Giro
        self.definicao = '''
        O P/Capital de Giro mede o valor de mercado da empresa em relação ao seu capital de giro, calculado
        como (Valor de Mercado / Capital de Giro), onde Capital de Giro é o Ativo Circulante menos o Passivo Circulante.
        É um indicador de valuation que avalia a relação entre o preço da empresa e sua liquidez operacional de curto prazo.
        Um valor baixo sugere subvalorização ou alta liquidez, enquanto valores altos indicam sobrevalorização ou baixa liquidez.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/Capital de Giro
        self.formula = 'P/Capital de Giro = Valor de Mercado / (Ativo Circulante - Passivo Circulante)'

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

    # Avalia o valor do P/Capital de Giro e retorna um objeto ResultadoIND
    def avaliar(self, p_capital_giro):
        # Tenta processar o valor do P/Capital de Giro
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_capital_giro, (int, float)) and not (isinstance(p_capital_giro, str) and p_capital_giro.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do P/Capital de Giro deve ser numérico.")
            # Converte o P/Capital de Giro para float para garantir que é numérico
            p_capital_giro = float(p_capital_giro)
            # Verifica se P/Capital de Giro é negativo, indicando capital de giro negativo
            if p_capital_giro < 0:
                # Retorna ResultadoIND para P/Capital de Giro negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/Capital de Giro < 0',
                    descricao='Um P/Capital de Giro negativo indica que o capital de giro é negativo, ou seja, o passivo circulante excede o ativo circulante. Isso sugere problemas graves de liquidez de curto prazo, comum em empresas em crise ou com má gestão financeira, indicando risco de insolvência.',
                    riscos='Risco de falência, incapacidade de honrar obrigações de curto prazo ou necessidade de financiamento emergencial. Pode haver baixa confiabilidade financeira.',
                    referencia='Avalie evaluate_liquidez_corrente para liquidez, evaluate_cash_flow para geração de caixa e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação da liquidez. Priorize análise de fluxo de caixa e estratégias de reestruturação financeira.'
                )
            # Verifica se P/Capital de Giro está entre 0 e 5, indicando forte subvalorização
            elif 0 <= p_capital_giro <= 5:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/Capital de Giro <= 5',
                    descricao='O P/Capital de Giro está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação à sua liquidez operacional. Essa faixa indica oportunidades de compra, comum em empresas com forte capital de giro, mas preço de mercado deprimido devido a ciclos econômicos ou baixa visibilidade.',
                    riscos='Risco de capital de giro excessivo, indicando ineficiência no uso de recursos. Pode haver ativos circulantes de baixa qualidade, como estoques obsoletos.',
                    referencia='Analise evaluate_liquidez_corrente para liquidez, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
                    recomendacao='Considere investir, mas verifique a qualidade do capital de giro e a eficiência operacional. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/Capital de Giro está entre 5 e 10, indicando valuation equilibrado
            elif 5 < p_capital_giro <= 10:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='5 < P/Capital de Giro <= 10',
                    descricao='O P/Capital de Giro está em uma faixa equilibrada, sugerindo que o valor de mercado está alinhado com a liquidez operacional da empresa. Essa faixa é comum em empresas estáveis com capital de giro adequado, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação na liquidez devido a aumento de passivos circulantes ou queda na receita. Pode haver dependência de fatores macroeconômicos afetando o capital de giro.',
                    referencia='Compare com evaluate_p_ebitda para valuation operacional, evaluate_current_ratio para liquidez e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de liquidez e estratégias de gestão de capital de giro antes de investir. Boa opção para investidores que buscam estabilidade financeira.'
                )
            # Verifica se P/Capital de Giro está entre 10 e 15, indicando valuation moderado
            elif 10 < p_capital_giro <= 15:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='10 < P/Capital de Giro <= 15',
                    descricao='O P/Capital de Giro está moderadamente elevado, indicando que o mercado atribui um prêmio à liquidez operacional da empresa. Essa faixa sugere expectativas de crescimento ou confiança na gestão de caixa, comum em empresas com potencial moderado ou em setores com margens estáveis.',
                    riscos='Risco de correção no preço se o capital de giro diminuir ou as obrigações de curto prazo aumentarem. Pode haver sobrevalorização devido a otimismo de mercado.',
                    referencia='Verifique evaluate_p_vp para valuation patrimonial, evaluate_beta para volatilidade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Considere esperar por sinais de melhoria na liquidez ou redução no valuation antes de investir. Combine com análise de fluxo de caixa e margens.'
                )
            # Verifica se P/Capital de Giro está entre 15 e 20, indicando sobrevalorização
            elif 15 < p_capital_giro <= 20:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='15 < P/Capital de Giro <= 20',
                    descricao='O P/Capital de Giro está consideravelmente elevado, indicando sobrevalorização em relação à liquidez operacional. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se o capital de giro não suportar as expectativas. Pode haver dependência de ativos circulantes de baixa qualidade ou bolhas setoriais.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para lucratividade e evaluate_current_ratio para liquidez.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com forte gestão de caixa e fundamentos sólidos.'
                )
            # Verifica se P/Capital de Giro excede 20, indicando sobrevalorização extrema
            elif p_capital_giro > 20:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='P/Capital de Giro > 20',
                    descricao='O P/Capital de Giro é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de liquidez operacional. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço de mercado desconecta dos fundamentos financeiros.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de narrativas de mercado ou baixa liquidez operacional.',
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
                Ocorreu um erro ao processar o P/Capital de Giro: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe PSREvaluator para avaliar o indicador Preço sobre Vendas (PSR)
class PSREvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do PSR
    def __init__(self):
        # Define string multilinha explicando o índice PSR
        self.definicao = '''
        O PSR (Preço sobre Vendas) mede o valor de mercado da empresa em relação à sua receita líquida, calculado
        como (Valor de Mercado / Receita Líquida). É um indicador de valuation que avalia se a empresa está cara ou barata
        com base em sua capacidade de gerar vendas. Um PSR baixo sugere subvalorização, enquanto valores altos indicam
        sobrevalorização ou expectativas de crescimento futuro.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do PSR
        self.formula = 'PSR = Valor de Mercado / Receita Líquida'

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

    # Avalia o valor do PSR e retorna um objeto ResultadoIND
    def avaliar(self, psr):
        # Tenta processar o valor do PSR
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(psr, (int, float)) and not (isinstance(psr, str) and psr.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do PSR deve ser numérico.")
            # Converte o PSR para float para garantir que é numérico
            psr = float(psr)
            # Verifica se PSR é menor que 0, indicando receita negativa ou erro
            if psr < 0:
                # Retorna ResultadoIND para PSR negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='PSR < 0',
                    descricao='Um PSR negativo indica que a receita líquida é negativa, sugerindo problemas graves como vendas nulas ou erros contábeis. Isso pode ocorrer em empresas em crise ou com dados financeiros inconsistentes, tornando a valuation irrelevante e indicando instabilidade financeira.',
                    riscos='Risco de falência, manipulação contábil ou insolvência. Pode haver incapacidade de gerar receita ou baixa confiabilidade nos dados financeiros.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_cash_flow para geração de caixa e evaluate_giro_ativo para eficiência.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou instabilidade financeira grave. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se PSR está entre 0 e 0.5, indicando forte subvalorização
            elif 0 <= psr <= 0.5:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= PSR <= 0.5',
                    descricao='O PSR está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação à sua receita líquida. Essa faixa indica oportunidades de compra, comum em empresas com vendas robustas, mas preço de mercado deprimido devido a ciclos econômicos ou baixa percepção de mercado.',
                    riscos='Risco de margens de lucro baixas ou receita instável. Pode haver desafios setoriais ou problemas operacionais que justifiquem o desconto no valuation.',
                    referencia='Analise evaluate_p_l para comparação de lucros, evaluate_margem_bruta para eficiência e evaluate_debt_to_equity para alavancagem.',
                    recomendacao='Considere investir, mas verifique a sustentabilidade da receita e a lucratividade. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se PSR está entre 0.5 e 1.0, indicando valuation equilibrado
            elif 0.5 < psr <= 1.0:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.5 < PSR <= 1.0',
                    descricao='O PSR está em uma faixa equilibrada, sugerindo que o valor de mercado está alinhado com a receita líquida da empresa. Essa faixa é comum em empresas estáveis com vendas consistentes e crescimento moderado, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação na receita devido a concorrência ou custos crescentes. Pode haver dependência de fatores macroeconômicos que afetem as vendas ou o preço de mercado.',
                    referencia='Compare com evaluate_p_ebitda para valuation operacional, evaluate_margem_liquida para lucratividade e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de receita e planos de expansão antes de investir. Pode ser uma boa opção para investidores de longo prazo com foco em estabilidade.'
                )
            # Verifica se PSR está entre 1.0 e 2.0, indicando valuation moderado
            elif 1.0 < psr <= 2.0:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1.0 < PSR <= 2.0',
                    descricao='O PSR está moderadamente elevado, indicando que o mercado atribui um prêmio à receita líquida da empresa. Essa faixa sugere expectativas de crescimento futuro ou confiança no modelo de negócios, comum em empresas com potencial moderado ou em setores com margens estáveis.',
                    riscos='Risco de correção no preço se a receita não crescer conforme esperado. Pode haver sobrevalorização devido a otimismo de mercado ou dependência de setores cíclicos.',
                    referencia='Verifique evaluate_p_vp para valuation patrimonial, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Considere esperar por sinais de crescimento ou redução no valuation antes de investir. Combine com análise de margens e fluxo de caixa para validar o prêmio.'
                )
            # Verifica se PSR está entre 2.0 e 3.0, indicando sobrevalorização
            elif 2.0 < psr <= 3.0:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='2.0 < PSR <= 3.0',
                    descricao='O PSR está consideravelmente elevado, indicando sobrevalorização em relação à receita líquida. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, como tecnologia, mas o preço reflete otimismo significativo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se a receita declinar ou expectativas não se realizarem. Pode haver bolhas setoriais ou dependência de fatores intangíveis no valuation.',
                    referencia='Combine com evaluate_margem_liquida para lucratividade, evaluate_roic para retorno sobre capital e evaluate_current_ratio para liquidez.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com receitas crescentes e fundamentos sólidos.'
                )
            # Verifica se PSR excede 3.0, indicando sobrevalorização extrema
            elif psr > 3.0:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='PSR > 3.0',
                    descricao='O PSR é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de crescimento de receita. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço de mercado desconecta dos fundamentos de vendas.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de narrativas de mercado, risco de fraudes ou receitas infladas.',
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
                Ocorreu um erro ao processar o PSR: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe GiroAtivoEvaluator para avaliar o indicador Giro do Ativo
class GiroAtivoEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do Giro do Ativo
    def __init__(self):
        # Define string multilinha explicando o índice Giro do Ativo
        self.definicao = '''
        O Giro do Ativo mede a eficiência com que a empresa utiliza seus ativos totais para gerar receita, calculado
        como (Receita Líquida / Ativos Totais). É um indicador de eficiência operacional que avalia o quão bem os ativos
        são empregados para produzir vendas. Um valor alto sugere alta eficiência, enquanto valores baixos indicam subutilização
        de ativos ou ineficiência operacional.
        '''
        # Define a categoria de agrupamento como "Eficiência Operacional"
        self.agrupador = 'Eficiência Operacional'
        # Define a fórmula do Giro do Ativo
        self.formula = 'Giro do Ativo = Receita Líquida / Ativos Totais'

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

    # Avalia o valor do Giro do Ativo e retorna um objeto ResultadoIND
    def avaliar(self, giro_ativo):
        # Tenta processar o valor do Giro do Ativo
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(giro_ativo, (int, float)) and not (isinstance(giro_ativo, str) and giro_ativo.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do Giro do Ativo deve ser numérico.")
            # Converte o Giro do Ativo para float para garantir que é numérico
            giro_ativo = float(giro_ativo)
            # Verifica se Giro do Ativo é menor que 0, indicando erro ou receita negativa
            if giro_ativo < 0:
                # Retorna ResultadoIND para Giro do Ativo negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Giro do Ativo < 0',
                    descricao='Um Giro do Ativo negativo é inválido, indicando receita líquida negativa ou erros nos dados financeiros. Isso pode ocorrer em empresas em crise, com vendas nulas ou problemas contábeis, inviabilizando a análise de eficiência operacional.',
                    riscos='Risco de falência, manipulação contábil ou insolvência. Pode haver incapacidade de gerar receita ou baixa confiabilidade nos dados financeiros.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_cash_flow para geração de caixa e evaluate_roe para rentabilidade.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou instabilidade financeira grave. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se Giro do Ativo está entre 0 e 0.5, indicando eficiência muito baixa
            elif 0 <= giro_ativo <= 0.5:
                # Retorna ResultadoIND para eficiência muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Giro do Ativo <= 0.5',
                    descricao='O Giro do Ativo está muito baixo, indicando baixa eficiência na utilização dos ativos para gerar receita. Essa faixa é comum em setores intensivos em capital, como infraestrutura ou imobiliário, ou em empresas com ativos ociosos ou baixa demanda por seus produtos.',
                    riscos='Risco de ineficiência operacional, com ativos subutilizados ou custos elevados. Pode haver dependência de investimentos pesados ou baixa competitividade no mercado.',
                    referencia='Analise evaluate_margem_ebit para eficiência operacional, evaluate_roa para rentabilidade dos ativos e evaluate_cash_conversion_cycle para ciclo de caixa.',
                    recomendacao='Evite investir a menos que haja planos claros para aumentar a receita ou otimizar ativos. Monitore estratégias de melhoria operacional.'
                )
            # Verifica se Giro do Ativo está entre 0.5 e 1.0, indicando eficiência moderada
            elif 0.5 < giro_ativo <= 1.0:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.5 < Giro do Ativo <= 1.0',
                    descricao='O Giro do Ativo está em uma faixa moderada, indicando eficiência razoável na utilização dos ativos para gerar receita. Essa faixa é comum em empresas com operações estáveis, como manufatura ou varejo, mas com potencial limitado para maximizar o uso de ativos.',
                    riscos='Risco de estagnação na receita devido a concorrência ou ineficiência parcial na gestão de ativos. Pode haver limitações em escalar vendas sem novos investimentos.',
                    referencia='Compare com evaluate_margem_liquida para lucratividade, evaluate_p_ativo para valuation e evaluate_market_share para competitividade.',
                    recomendacao='Considere investir com cautela, avaliando a capacidade de aumentar a receita ou otimizar ativos. Priorize empresas com estratégias de crescimento ou eficiência.'
                )
            # Verifica se Giro do Ativo está entre 1.0 e 2.0, indicando boa eficiência
            elif 1.0 < giro_ativo <= 2.0:
                # Retorna ResultadoIND para boa eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1.0 < Giro do Ativo <= 2.0',
                    descricao='O Giro do Ativo está em uma faixa saudável, indicando boa eficiência na utilização dos ativos para gerar receita. Essa faixa é comum em empresas com operações otimizadas, como bens de consumo ou tecnologia, sugerindo capacidade de gerar vendas significativas com os ativos disponíveis.',
                    riscos='Risco de dependência de mercados específicos ou sazonalidade na receita. Pode haver necessidade de reinvestimento para manter a eficiência em longo prazo.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão.',
                    recomendacao='Considere investir, mas avalie a sustentabilidade da receita e a qualidade dos ativos. Boa opção para investidores que buscam eficiência operacional.'
                )
            # Verifica se Giro do Ativo excede 2.0, indicando eficiência excepcional
            elif giro_ativo > 2.0:
                # Retorna ResultadoIND para eficiência excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Giro do Ativo > 2.0',
                    descricao='O Giro do Ativo é extremamente alto, indicando eficiência excepcional na utilização dos ativos para gerar receita. Essa faixa é típica de empresas com modelos de negócios escaláveis, baixa intensidade de capital ou alta rotatividade, como varejo de alta rotatividade ou software.',
                    riscos='Risco de sobredependência de canais de receita específicos ou saturação de mercado. Pode haver vulnerabilidade a mudanças regulatórias ou entrada de concorrentes.',
                    referencia='Combine com evaluate_psr para receita, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a eficiência elevada, mas diversifique para mitigar riscos de concentração ou mudanças de mercado.'
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
                Ocorreu um erro ao processar o Giro do Ativo: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe PLAtivosEvaluator para avaliar o indicador Patrimônio Líquido / Ativos
class PLAtivosEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do PL/Ativos
    def __init__(self):
        # Define string multilinha explicando o índice PL/Ativos
        self.definicao = '''
        O PL/Ativos (Patrimônio Líquido sobre Ativos) mede a proporção do patrimônio líquido em relação aos ativos totais da empresa,
        calculado como (Patrimônio Líquido / Ativos Totais). É um indicador de estrutura de capital que avalia o grau de financiamento
        dos ativos por capital próprio versus dívida. Um valor alto sugere baixa alavancagem, enquanto valores baixos ou negativos indicam
        alta dependência de dívida ou fragilidade financeira.
        '''
        # Define a categoria de agrupamento como "Estrutura de Capital"
        self.agrupador = 'Estrutura de Capital'
        # Define a fórmula do PL/Ativos
        self.formula = 'PL/Ativos = Patrimônio Líquido / Ativos Totais'

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

    # Avalia o valor do PL/Ativos e retorna um objeto ResultadoIND
    def avaliar(self, pl_ativos):
        # Tenta processar o valor do PL/Ativos
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(pl_ativos, (int, float)) and not (isinstance(pl_ativos, str) and pl_ativos.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do PL/Ativos deve ser numérico.")
            # Converte o PL/Ativos para float para garantir que é numérico
            pl_ativos = float(pl_ativos)
            # Verifica se PL/Ativos é negativo, indicando patrimônio líquido negativo
            if pl_ativos < 0:
                # Retorna ResultadoIND para PL/Ativos negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='PL/Ativos < 0',
                    descricao='Um PL/Ativos negativo indica que o patrimônio líquido é negativo, sugerindo prejuízos acumulados ou problemas financeiros graves. Isso ocorre quando as dívidas superam os ativos líquidos, comum em empresas em crise ou com alta alavancagem, apontando para instabilidade financeira.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver endividamento excessivo ou incapacidade de gerar valor para acionistas.',
                    referencia='Avalie evaluate_roe para rentabilidade patrimonial, evaluate_div_liquida_pl para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação patrimonial. Priorize análise de turnaround e saúde financeira.'
                )
            # Verifica se PL/Ativos está entre 0 e 0.2, indicando alta alavancagem
            elif 0 <= pl_ativos <= 0.2:
                # Retorna ResultadoIND para alta alavancagem
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= PL/Ativos <= 0.2',
                    descricao='O PL/Ativos está muito baixo, indicando que a maior parte dos ativos é financiada por dívidas, sugerindo alta alavancagem. Essa faixa é comum em setores intensivos em capital, como infraestrutura ou energia, mas implica maior risco financeiro devido à dependência de credores.',
                    riscos='Risco de insolvência em cenários adversos, como aumento de juros ou queda na receita. Pode haver restrições de credores ou necessidade de venda de ativos.',
                    referencia='Analise evaluate_debt_to_assets para estrutura de dívida, evaluate_ebit_margin para eficiência operacional e evaluate_liquidez_corrente para liquidez.',
                    recomendacao='Evite investir a menos que haja forte geração de caixa ou planos de desalavancagem. Monitore a capacidade de pagamento de dívidas.'
                )
            # Verifica se PL/Ativos está entre 0.2 e 0.4, indicando alavancagem moderada
            elif 0.2 < pl_ativos <= 0.4:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.2 < PL/Ativos <= 0.4',
                    descricao='O PL/Ativos está em uma faixa moderada, indicando um equilíbrio razoável entre capital próprio e dívida no financiamento dos ativos. Essa faixa é comum em empresas com operações estáveis, como manufatura ou varejo, mas ainda reflete dependência significativa de financiamento externo.',
                    riscos='Risco de pressão financeira se os lucros caírem ou taxas de juros subirem. Pode haver limitações em novos investimentos ou distribuições aos acionistas.',
                    referencia='Compare com evaluate_div_liquida_pl para alavancagem, evaluate_margem_liquida para lucratividade e evaluate_cash_conversion_cycle para eficiência.',
                    recomendacao='Considere investir com cautela, avaliando a estabilidade dos lucros e planos de redução de dívida. Priorize empresas com fluxo de caixa consistente.'
                )
            # Verifica se PL/Ativos está entre 0.4 e 0.6, indicando boa estrutura de capital
            elif 0.4 < pl_ativos <= 0.6:
                # Retorna ResultadoIND para boa estrutura de capital
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.4 < PL/Ativos <= 0.6',
                    descricao='O PL/Ativos está em uma faixa saudável, indicando que uma proporção significativa dos ativos é financiada por capital próprio. Essa faixa é comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugerindo estabilidade e menor dependência de dívida.',
                    riscos='Risco de subalavancagem, onde a empresa pode perder oportunidades de crescimento por não usar dívida barata. Pode haver ineficiência no uso de capital próprio.',
                    referencia='Verifique evaluate_roe para rentabilidade patrimonial, evaluate_margem_operacional para eficiência e evaluate_debt_to_ebitda para alavancagem operacional.',
                    recomendacao='Considere investir, mas avalie a eficiência na alocação de capital e planos de crescimento. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se PL/Ativos excede 0.6, indicando baixa alavancagem
            elif pl_ativos > 0.6:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='PL/Ativos > 0.6',
                    descricao='O PL/Ativos é extremamente alto, indicando que a maior parte dos ativos é financiada por capital próprio, sugerindo baixa alavancagem e robustez financeira. Essa faixa é típica de empresas com forte geração de caixa ou baixa necessidade de capital, como software ou serviços especializados.',
                    riscos='Risco de ineficiência no uso de capital, com excesso de capital próprio ocioso. Pode haver perda de oportunidades de crescimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_roe para rentabilidade patrimonial, evaluate_psr para receita e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a robustez financeira, mas verifique a eficiência na alocação de capital. Considere empresas com planos de reinvestimento ou dividendos.'
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
                Ocorreu um erro ao processar o PL/Ativos: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe LiquidezCorrenteEvaluator para avaliar o indicador Liquidez Corrente
class LiquidezCorrenteEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula da Liquidez Corrente
    def __init__(self):
        # Define string multilinha explicando o índice Liquidez Corrente
        self.definicao = '''
        A Liquidez Corrente mede a capacidade da empresa de pagar suas obrigações de curto prazo com seus ativos circulantes,
        calculada como (Ativo Circulante / Passivo Circulante). É um indicador de liquidez que avalia a saúde financeira de curto
        prazo da empresa. Um valor alto sugere boa capacidade de pagamento, enquanto valores baixos indicam risco de insolvência
        no curto prazo.
        '''
        # Define a categoria de agrupamento como "Liquidez"
        self.agrupador = 'Liquidez'
        # Define a fórmula da Liquidez Corrente
        self.formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'

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

    # Avalia o valor da Liquidez Corrente e retorna um objeto ResultadoIND
    def avaliar(self, liquidez_corrente):
        # Tenta processar o valor da Liquidez Corrente
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(liquidez_corrente, (int, float)) and not (isinstance(liquidez_corrente, str) and liquidez_corrente.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Liquidez Corrente deve ser numérico.")
            # Converte a Liquidez Corrente para float para garantir que é numérico
            liquidez_corrente = float(liquidez_corrente)
            # Verifica se Liquidez Corrente é menor que 0, indicando erro ou passivo circulante negativo
            if liquidez_corrente < 0:
                # Retorna ResultadoIND para Liquidez Corrente negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Liquidez Corrente < 0',
                    descricao='Uma Liquidez Corrente negativa é inválida, indicando que o ativo circulante ou passivo circulante contém valores negativos, sugerindo erros contábeis ou problemas financeiros graves. Isso pode ocorrer em empresas em crise ou com balanços mal estruturados, inviabilizando a análise de liquidez.',
                    riscos='Risco de falência, manipulação contábil ou insolvência iminente. Pode haver incapacidade de honrar obrigações de curto prazo ou baixa confiabilidade nos dados financeiros.',
                    referencia='Avalie evaluate_cash_flow para geração de caixa, evaluate_debt_to_assets para alavancagem e evaluate_margem_liquida para lucratividade.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou instabilidade financeira grave. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se Liquidez Corrente está entre 0 e 0.8, indicando liquidez muito baixa
            elif 0 <= liquidez_corrente < 0.8:
                # Retorna ResultadoIND para liquidez muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Liquidez Corrente < 0.8',
                    descricao='A Liquidez Corrente está muito baixa, indicando que os ativos circulantes não cobrem as obrigações de curto prazo. Isso sugere alto risco de insolvência no curto prazo, comum em empresas com fluxo de caixa restrito, alta alavancagem ou setores intensivos em capital.',
                    riscos='Risco de default em obrigações de curto prazo, aumento de endividamento ou necessidade de venda de ativos. Pode haver pressão financeira ou baixa competitividade.',
                    referencia='Analise evaluate_cash_conversion_cycle para ciclo de caixa, evaluate_debt_to_equity para alavancagem e evaluate_ebit_margin para eficiência operacional.',
                    recomendacao='Evite investir até que a empresa demonstre melhoria na liquidez ou gestão de caixa. Priorize análise de fluxo de caixa e planos de redução de dívidas.'
                )
            # Verifica se Liquidez Corrente está entre 0.8 e 1.2, indicando liquidez limitada
            elif 0.8 <= liquidez_corrente < 1.2:
                # Retorna ResultadoIND para liquidez limitada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='0.8 <= Liquidez Corrente < 1.2',
                    descricao='A Liquidez Corrente está em uma faixa limitada, sugerindo que os ativos circulantes cobrem as obrigações de curto prazo de forma marginal. Essa faixa é comum em empresas com operações estáveis, mas com pouca folga financeira, como varejo ou manufatura com margens apertadas.',
                    riscos='Risco de dificuldades financeiras em cenários adversos, como queda na receita ou aumento de custos. Pode haver dependência de financiamento externo para cumprir obrigações.',
                    referencia='Compare com evaluate_liquidez_imediata para liquidez mais restrita, evaluate_margem_liquida para lucratividade e evaluate_capex para investimentos.',
                    recomendacao='Considere investir com cautela, monitorando a geração de caixa e planos de melhoria de liquidez. Avalie a estabilidade das receitas e a gestão de passivos.'
                )
            # Verifica se Liquidez Corrente está entre 1.2 e 2.0, indicando boa liquidez
            elif 1.2 <= liquidez_corrente <= 2.0:
                # Retorna ResultadoIND para boa liquidez
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1.2 <= Liquidez Corrente <= 2.0',
                    descricao='A Liquidez Corrente está em uma faixa saudável, indicando que os ativos circulantes cobrem bem as obrigações de curto prazo. Essa faixa é comum em empresas com gestão financeira sólida, como tecnologia ou bens de consumo, sugerindo capacidade de honrar compromissos sem pressão imediata.',
                    riscos='Risco de ineficiência no uso de ativos circulantes se a liquidez for excessiva. Pode haver dependência de estoques ou recebíveis de baixa qualidade.',
                    referencia='Verifique evaluate_cash_flow para geração de caixa, evaluate_margem_operacional para eficiência e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Considere investir, mas avalie a qualidade dos ativos circulantes e a sustentabilidade da liquidez. Boa opção para investidores que buscam segurança financeira.'
                )
            # Verifica se Liquidez Corrente excede 2.0, indicando liquidez elevada
            elif liquidez_corrente > 2.0:
                # Retorna ResultadoIND para liquidez elevada
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Liquidez Corrente > 2.0',
                    descricao='A Liquidez Corrente é extremamente alta, indicando que os ativos circulantes superam significativamente as obrigações de curto prazo. Essa faixa é típica de empresas com forte geração de caixa ou baixa alavancagem, como software ou empresas com reservas elevadas, refletindo robustez financeira.',
                    riscos='Risco de ineficiência no uso de capital, com excesso de caixa ocioso ou estoques acumulados. Pode haver perda de oportunidades de investimento ou retorno aos acionistas.',
                    referencia='Combine com evaluate_roe para rentabilidade patrimonial, evaluate_psr para receita e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem a liquidez elevada, mas verifique a eficiência na alocação de capital. Considere empresas com planos de reinvestimento ou dividendos.'
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
                Ocorreu um erro ao processar a Liquidez Corrente: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
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
                    classificacao='Baixo',
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
                    classificacao='Crítico',
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

# Define a classe ROICEvaluator para avaliar o indicador Retorno sobre Capital Investido (ROIC)
class ROICEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do ROIC
    def __init__(self):
        # Define string multilinha explicando o índice ROIC
        self.definicao = '''
        O ROIC (Retorno sobre Capital Investido) mede a eficiência da empresa em gerar lucros a partir do capital total investido, calculado
        como (NOPAT / Capital Investido) * 100, onde NOPAT é o lucro operacional após impostos e Capital Investido é a soma de patrimônio
        líquido e dívida líquida. É um indicador de rentabilidade que avalia a capacidade de alocação eficiente do capital. Um ROIC alto sugere
        eficiência superior, enquanto valores baixos indicam ineficiência ou retornos insuficientes.
        '''
        # Define a categoria de agrupamento como "Rentabilidade"
        self.agrupador = 'Rentabilidade'
        # Define a fórmula do ROIC
        self.formula = 'ROIC (%) = (NOPAT / Capital Investido) * 100'

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

    # Avalia o valor do ROIC e retorna um objeto ResultadoIND
    def avaliar(self, roic):
        # Tenta processar o valor do ROIC
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(roic, (int, float)) and not (isinstance(roic, str) and roic.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do ROIC deve ser numérico.")
            # Converte o ROIC para float para garantir que é numérico
            roic = float(roic)
            # Verifica se ROIC é negativo, indicando prejuízo operacional ou ineficiência
            if roic < 0:
                # Retorna ResultadoIND para ROIC negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='ROIC < 0%',
                    descricao='Um ROIC negativo indica que a empresa está gerando prejuízo operacional após impostos em relação ao capital investido, sugerindo ineficiência grave na alocação de capital. Isso pode ocorrer em empresas em crise, com altos custos operacionais ou investimentos mal planejados.',
                    riscos='Risco de falência, reestruturação ou baixa atratividade para investidores. Pode haver alavancagem excessiva ou incapacidade de gerar retornos sobre o capital.',
                    referencia='Avalie evaluate_ebit_margin para eficiência operacional, evaluate_debt_to_equity para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação operacional ou melhor alocação de capital. Priorize análise de turnaround e eficiência.'
                )
            # Verifica se ROIC está entre 0 e 5, indicando rentabilidade muito baixa
            elif 0 <= roic <= 5:
                # Retorna ResultadoIND para rentabilidade muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= ROIC <= 5%',
                    descricao='O ROIC está muito baixo, sugerindo rentabilidade limitada sobre o capital investido. Isso é comum em setores intensivos em capital, como infraestrutura ou manufatura pesada, ou em empresas com baixa eficiência operacional, onde os retornos não justificam o capital empregado.',
                    riscos='Risco de baixa atratividade para investidores devido a retornos insuficientes. Pode haver capital ocioso, investimentos ineficientes ou dependência de economias de escala.',
                    referencia='Analise evaluate_margem_ebitda para eficiência operacional, evaluate_p_ativo para valuation e evaluate_capex para investimentos em capital.',
                    recomendacao='Considere investir apenas se houver planos claros para otimização de capital ou aumento de lucros. Verifique tendências de mercado e eficiência operacional.'
                )
            # Verifica se ROIC está entre 5 e 10, indicando rentabilidade moderada
            elif 5 < roic <= 10:
                # Retorna ResultadoIND para rentabilidade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5 < ROIC <= 10%',
                    descricao='O ROIC está em uma faixa moderada, indicando rentabilidade razoável sobre o capital investido. Essa faixa é comum em empresas com operações estáveis, mas sem alta eficiência, como manufatura ou serviços com margens moderadas, refletindo um equilíbrio entre retornos e capital empregado.',
                    riscos='Risco de estagnação nos retornos devido a concorrência ou ineficiência na alocação de capital. Pode haver limitações em financiar expansão sem aumentar a alavancagem.',
                    referencia='Compare com evaluate_margem_liquida para lucratividade final, evaluate_roe para rentabilidade patrimonial e evaluate_market_share para competitividade.',
                    recomendacao='Avalie o histórico de retornos e estratégias de alocação de capital antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade com retorno moderado.'
                )
            # Verifica se ROIC está entre 10 e 15, indicando boa rentabilidade
            elif 10 < roic <= 15:
                # Retorna ResultadoIND para boa rentabilidade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='10 < ROIC <= 15%',
                    descricao='O ROIC está em uma faixa alta, sugerindo boa rentabilidade sobre o capital investido. Essa faixa é comum em empresas com eficiência operacional sólida, poder de precificação ou alocação otimizada de capital, como tecnologia ou bens de consumo, indicando retornos robustos sobre os investimentos.',
                    riscos='Risco de dependência de projetos específicos ou mercados premium. Pode haver volatilidade se os retornos ou a eficiência do capital não forem sustentáveis.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roe para retorno patrimonial e evaluate_growth_rate para expansão.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade dos retornos e a eficiência na gestão de capital.'
                )
            # Verifica se ROIC excede 15, indicando rentabilidade excepcional
            elif roic > 15:
                # Retorna ResultadoIND para rentabilidade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='ROIC > 15%',
                    descricao='O ROIC é extremamente alto, indicando rentabilidade excepcional sobre o capital investido. Essa faixa é típica de empresas com modelos de negócios escaláveis, baixa intensidade de capital ou eficiência superior, como software ou serviços especializados, refletindo forte retorno sobre o capital.',
                    riscos='Risco de sobredependência de nichos de mercado ou projetos específicos. Mudanças regulatórias, concorrência ou saturação podem impactar a rentabilidade.',
                    referencia='Combine com evaluate_psr para receita, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem retornos sustentáveis, mas diversifique para mitigar riscos de concentração ou mudanças de mercado.'
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
                Ocorreu um erro ao processar o ROIC: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe ROAEvaluator para avaliar o indicador Retorno sobre Ativos (ROA)
class ROAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do ROA
    def __init__(self):
        # Define string multilinha explicando o índice ROA
        self.definicao = '''
        O ROA (Retorno sobre Ativos) mede a rentabilidade da empresa em relação aos seus ativos totais, calculado
        como (Lucro Líquido / Ativos Totais) * 100. É um indicador de eficiência que avalia a capacidade da empresa
        de gerar lucros utilizando seus ativos. Um ROA alto sugere eficiência na gestão de ativos, enquanto valores
        baixos ou negativos indicam ineficiência ou prejuízos.
        '''
        # Define a categoria de agrupamento como "Rentabilidade"
        self.agrupador = 'Rentabilidade'
        # Define a fórmula do ROA
        self.formula = 'ROA (%) = (Lucro Líquido / Ativos Totais) * 100'

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

    # Avalia o valor do ROA e retorna um objeto ResultadoIND
    def avaliar(self, roa):
        # Tenta processar o valor do ROA
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(roa, (int, float)) and not (isinstance(roa, str) and roa.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do ROA deve ser numérico.")
            # Converte o ROA para float para garantir que é numérico
            roa = float(roa)
            # Verifica se ROA é negativo, indicando prejuízo ou ineficiência
            if roa < 0:
                # Retorna ResultadoIND para ROA negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='ROA < 0%',
                    descricao='Um ROA negativo indica que a empresa está gerando prejuízo líquido em relação aos seus ativos, sugerindo ineficiência grave na utilização de recursos ou perdas operacionais. Isso pode ocorrer em empresas em crise, com ativos ociosos ou em setores com margens apertadas.',
                    riscos='Risco de falência, reestruturação ou baixa atratividade para investidores. Pode haver endividamento excessivo ou incapacidade de converter ativos em lucros.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_debt_to_assets para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação de lucros ou melhor uso de ativos. Priorize análise de eficiência e estratégias de turnaround.'
                )
            # Verifica se ROA está entre 0 e 3, indicando rentabilidade muito baixa
            elif 0 <= roa <= 3:
                # Retorna ResultadoIND para rentabilidade muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= ROA <= 3%',
                    descricao='O ROA está muito baixo, sugerindo rentabilidade limitada na utilização dos ativos. Isso é comum em setores intensivos em capital, como indústria pesada ou infraestrutura, ou em empresas com baixa eficiência operacional, onde os lucros não acompanham o volume de ativos.',
                    riscos='Risco de baixa atratividade para investidores devido a retornos insuficientes. Pode haver ativos subutilizados, custos elevados ou dependência de economias de escala.',
                    referencia='Analise evaluate_margem_ebitda para eficiência operacional, evaluate_p_ativo para valuation e evaluate_current_ratio para liquidez.',
                    recomendacao='Considere investir apenas se houver planos claros para otimização de ativos ou aumento de lucros. Verifique tendências de mercado e eficiência operacional.'
                )
            # Verifica se ROA está entre 3 e 7, indicando rentabilidade moderada
            elif 3 < roa <= 7:
                # Retorna ResultadoIND para rentabilidade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='3 < ROA <= 7%',
                    descricao='O ROA está em uma faixa moderada, indicando rentabilidade razoável na utilização dos ativos. Essa faixa é comum em empresas com operações estáveis, mas sem alta eficiência, como manufatura ou serviços com margens moderadas, refletindo um equilíbrio entre lucros e ativos.',
                    riscos='Risco de estagnação nos lucros devido a concorrência ou ineficiência na gestão de ativos. Pode haver limitações em financiar expansão sem aumentar a alavancagem.',
                    referencia='Compare com evaluate_margem_liquida para eficiência final, evaluate_roe para rentabilidade patrimonial e evaluate_market_share para competitividade.',
                    recomendacao='Avalie o histórico de lucros e estratégias de utilização de ativos antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade com retorno moderado.'
                )
            # Verifica se ROA está entre 7 e 12, indicando boa rentabilidade
            elif 7 < roa <= 12:
                # Retorna ResultadoIND para boa rentabilidade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='7 < ROA <= 12%',
                    descricao='O ROA está em uma faixa alta, sugerindo boa rentabilidade na utilização dos ativos. Essa faixa é comum em empresas com eficiência operacional sólida, poder de precificação ou ativos bem geridos, como tecnologia ou bens de consumo, indicando capacidade de gerar retornos robustos.',
                    riscos='Risco de dependência de ativos específicos ou mercados premium. Pode haver volatilidade se os lucros ou a eficiência dos ativos não forem sustentáveis.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade dos lucros e a eficiência na gestão de ativos.'
                )
            # Verifica se ROA excede 12, indicando rentabilidade excepcional
            elif roa > 12:
                # Retorna ResultadoIND para rentabilidade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='ROA > 12%',
                    descricao='O ROA é extremamente alto, indicando rentabilidade excepcional na utilização dos ativos. Essa faixa é típica de empresas com modelos de negócios escaláveis, baixa intensidade de capital ou eficiência superior, como software ou serviços especializados, refletindo forte retorno sobre os ativos.',
                    riscos='Risco de sobredependência de nichos de mercado ou ativos intangíveis. Mudanças regulatórias, concorrência ou saturação podem impactar a rentabilidade.',
                    referencia='Combine com evaluate_psr para receita, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem lucros sustentáveis, mas diversifique para mitigar riscos de concentração ou mudanças de mercado.'
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
                Ocorreu um erro ao processar o ROA: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe ROEEvaluator para avaliar o indicador Retorno sobre Patrimônio (ROE)
class ROEEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do ROE
    def __init__(self):
        # Define string multilinha explicando o índice ROE
        self.definicao = '''
        O ROE (Retorno sobre Patrimônio Líquido) mede a rentabilidade da empresa em relação ao capital próprio dos acionistas, calculado
        como (Lucro Líquido / Patrimônio Líquido) * 100. É um indicador de eficiência que avalia a capacidade da empresa de gerar lucros
        com o patrimônio investido pelos acionistas. Um ROE alto sugere alta eficiência, enquanto valores baixos ou negativos indicam ineficiência ou prejuízos.
        '''
        # Define a categoria de agrupamento como "Rentabilidade"
        self.agrupador = 'Rentabilidade'
        # Define a fórmula do ROE
        self.formula = 'ROE (%) = (Lucro Líquido / Patrimônio Líquido) * 100'

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

    # Avalia o valor do ROE e retorna um objeto ResultadoIND
    def avaliar(self, roe):
        # Tenta processar o valor do ROE
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(roe, (int, float)) and not (isinstance(roe, str) and roe.replace('.', '', 1).isdigit()):
                raise ValueError("O valor do ROE deve ser numérico.")
            # Converte o ROE para float para garantir que é numérico
            roe = float(roe)
            # Verifica se ROE é negativo, indicando prejuízo ou patrimônio líquido negativo
            if roe < 0:
                # Retorna ResultadoIND para ROE negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='ROE < 0%',
                    descricao='Um ROE negativo indica que a empresa está gerando prejuízo líquido ou possui patrimônio líquido negativo, sugerindo ineficiência grave ou problemas estruturais. Isso pode ocorrer em empresas em crise, com perdas acumuladas ou alta alavancagem, apontando para instabilidade financeira.',
                    riscos='Risco de falência, diluição acionária ou reestruturação financeira. Pode haver endividamento excessivo ou incapacidade de gerar lucros sustentáveis.',
                    referencia='Avalie evaluate_margem_liquida para lucratividade, evaluate_div_liquida_pl para alavancagem e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação de lucros ou estabilização do patrimônio. Priorize análise de turnaround e saúde financeira.'
                )
            # Verifica se ROE está entre 0 e 5, indicando rentabilidade muito baixa
            elif 0 <= roe <= 5:
                # Retorna ResultadoIND para rentabilidade muito baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= ROE <= 5%',
                    descricao='O ROE está muito baixo, sugerindo rentabilidade limitada sobre o patrimônio dos acionistas. Isso é comum em setores com margens apertadas, alta concorrência ou baixa eficiência operacional, como varejo ou indústrias de commodities, onde os lucros são insuficientes para remunerar o capital investido.',
                    riscos='Risco de baixa atratividade para investidores devido a retornos insuficientes. Pode haver dependência de fatores externos ou incapacidade de reinvestir lucros de forma eficaz.',
                    referencia='Analise evaluate_margem_ebit para eficiência operacional, evaluate_p_l para lucros e evaluate_debt_to_equity para estrutura de capital.',
                    recomendacao='Considere investir apenas se houver planos claros para melhoria de lucros ou eficiência. Verifique tendências de mercado e estratégias de crescimento.'
                )
            # Verifica se ROE está entre 5 e 15, indicando rentabilidade moderada
            elif 5 < roe <= 15:
                # Retorna ResultadoIND para rentabilidade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5 < ROE <= 15%',
                    descricao='O ROE está em uma faixa moderada, indicando rentabilidade razoável sobre o patrimônio líquido. Essa faixa é comum em empresas com operações estáveis, mas sem alta eficiência, como manufatura ou serviços com margens moderadas, refletindo um equilíbrio entre lucros e capital próprio.',
                    riscos='Risco de estagnação nos lucros devido a concorrência ou custos crescentes. Pode haver limitações em financiar crescimento sem aumentar a alavancagem.',
                    referencia='Compare com evaluate_margem_liquida para eficiência final, evaluate_p_vp para valuation patrimonial e evaluate_market_share para competitividade.',
                    recomendacao='Avalie o histórico de lucros e estratégias de crescimento antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade com retorno moderado.'
                )
            # Verifica se ROE está entre 15 e 25, indicando boa rentabilidade
            elif 15 < roe <= 25:
                # Retorna ResultadoIND para boa rentabilidade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='15 < ROE <= 25%',
                    descricao='O ROE está em uma faixa alta, sugerindo boa rentabilidade sobre o patrimônio líquido. Essa faixa é comum em empresas com forte eficiência operacional, poder de precificação ou operações otimizadas, como tecnologia ou bens de consumo de marca, indicando capacidade de gerar retornos robustos.',
                    riscos='Risco de dependência de mercados premium ou alta alavancagem para impulsionar o ROE. Pode haver volatilidade se os lucros não forem sustentáveis.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade dos lucros e o nível de endividamento da empresa.'
                )
            # Verifica se ROE excede 25, indicando rentabilidade excepcional
            elif roe > 25:
                # Retorna ResultadoIND para rentabilidade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='ROE > 25%',
                    descricao='O ROE é extremamente alto, indicando rentabilidade excepcional sobre o patrimônio líquido. Essa faixa é típica de empresas com modelos de negócios escaláveis, baixa concorrência ou marcas premium, como software ou bens de luxo, refletindo eficiência superior e forte retorno para acionistas.',
                    riscos='Risco de sobredependência de nichos de mercado ou alavancagem excessiva para inflar o ROE. Mudanças regulatórias ou entrada de concorrentes podem impactar lucros.',
                    referencia='Combine com evaluate_psr para receita, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Invista se os fundamentos suportarem lucros sustentáveis, mas diversifique para mitigar riscos de concentração ou mudanças de mercado.'
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
# Define a classe PEBITDAEvaluator para avaliar o indicador P/EBITDA
class PEBITDAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/EBITDA
    def __init__(self):
        # Define string multilinha explicando o índice P/EBITDA
        self.definicao = '''
        O P/EBITDA (Preço / EBITDA) mede o valor de mercado da empresa em relação ao seu lucro antes de juros, impostos, depreciação e amortização (EBITDA), calculado
        como (Valor de Mercado / EBITDA). É um indicador de valuation que avalia se a empresa está cara ou barata com base em sua geração de caixa operacional ajustada.
        Um P/EBITDA baixo sugere subvalorização, enquanto valores altos indicam sobrevalorização ou expectativas de crescimento futuro.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/EBITDA
        self.formula = 'P/EBITDA = Valor de Mercado / EBITDA'

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

    # Avalia o valor P/EBITDA e retorna um objeto ResultadoIND
    def avaliar(self, p_ebitda):
        # Tenta processar o valor P/EBITDA
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_ebitda, (int, float)) and not (isinstance(p_ebitda, str) and p_ebitda.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de P/EBITDA deve ser numérico.")
            # Converte o P/EBITDA para float para garantir que é numérico
            p_ebitda = float(p_ebitda)
            # Verifica se P/EBITDA é negativo, indicando prejuízo operacional ajustado
            if p_ebitda < 0:
                # Retorna ResultadoIND para P/EBITDA negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/EBITDA < 0',
                    descricao='Um P/EBITDA negativo indica que o EBITDA é negativo, sugerindo prejuízo operacional antes de juros, impostos, depreciação e amortização. Isso pode refletir ineficiência grave, altos custos fixos ou perdas operacionais, tornando a valuation irrelevante e indicando instabilidade financeira significativa.',
                    riscos='Risco de falência, reestruturação ou diluição acionária devido a prejuízos operacionais. Pode haver endividamento crescente ou perda de competitividade no mercado.',
                    referencia='Avalie evaluate_ebitda_margin para eficiência operacional, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa ajustada.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação no EBITDA. Priorize análise de custos, eficiência operacional e estratégias de turnaround.'
                )
            # Verifica se P/EBITDA está entre 0 e 6, indicando forte subvalorização
            elif 0 <= p_ebitda <= 6:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/EBITDA <= 6',
                    descricao='O P/EBITDA está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação à sua geração de caixa operacional ajustada. Essa faixa indica oportunidades de compra, comum em empresas com EBITDA sólido, mas preço de mercado deprimido devido a ciclos econômicos, baixa visibilidade ou setores menos atrativos.',
                    riscos='Risco de EBITDA instável ou ativos superavaliados no valor de mercado. Pode haver desafios setoriais, como commoditização, ou baixa percepção de crescimento que justifiquem o desconto.',
                    referencia='Analise evaluate_p_ebit para comparação operacional, evaluate_roe para rentabilidade e evaluate_debt_to_ebitda para alavancagem operacional.',
                    recomendacao='Considere investir, mas verifique a sustentabilidade do EBITDA e a composição do valor de mercado. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/EBITDA está entre 6 e 10, indicando valuation equilibrado
            elif 6 < p_ebitda <= 10:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='6 < P/EBITDA <= 10',
                    descricao='O P/EBITDA está em uma faixa equilibrada, sugerindo que o valor de mercado está alinhado com a geração de caixa operacional ajustada da empresa. Essa faixa é comum em empresas estáveis com EBITDA consistente e crescimento moderado, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação no EBITDA devido a concorrência ou custos crescentes. Pode haver dependência de fatores macroeconômicos que afetem a geração de caixa ou o preço de mercado.',
                    referencia='Compare com evaluate_evebitda para valuation ajustado, evaluate_margem_ebitda para eficiência e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de EBITDA e planos de expansão antes de investir. Pode ser uma boa opção para investidores de longo prazo com foco em estabilidade e geração de caixa.'
                )
            # Verifica se P/EBITDA está entre 10 e 14, indicando valuation moderado
            elif 10 < p_ebitda <= 14:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='10 < P/EBITDA <= 14',
                    descricao='O P/EBITDA está moderadamente elevado, indicando que o mercado atribui um prêmio à geração de caixa operacional ajustada da empresa. Essa faixa sugere expectativas de crescimento futuro ou confiança na gestão, comum em empresas com potencial moderado ou em setores com margens estáveis.',
                    riscos='Risco de correção no preço se o EBITDA não crescer conforme esperado. Pode haver sobrevalorização devido a otimismo de mercado ou dependência de setores cíclicos.',
                    referencia='Verifique evaluate_p_l para lucros, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Considere esperar por sinais de crescimento ou redução no valuation antes de investir. Combine com análise de margens EBITDA e fluxo de caixa para validar o prêmio.'
                )
            # Verifica se P/EBITDA está entre 14 e 18, indicando sobrevalorização
            elif 14 < p_ebitda <= 18:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='14 < P/EBITDA <= 18',
                    descricao='O P/EBITDA está consideravelmente elevado, indicando sobrevalorização em relação à geração de caixa operacional ajustada. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se o EBITDA declinar ou expectativas não se realizarem. Pode haver bolhas setoriais ou dependência de fatores intangíveis no valuation.',
                    referencia='Combine com evaluate_psr para receita, evaluate_roic para retorno sobre capital e evaluate_current_ratio para liquidez operacional.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com EBITDA crescente e fundamentos sólidos.'
                )
            # Verifica se P/EBITDA excede 18, indicando sobrevalorização extrema
            elif p_ebitda > 18:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/EBITDA > 18',
                    descricao='O P/EBITDA é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de crescimento operacional ajustado. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço de mercado desconecta dos fundamentos operacionais.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de fatores intangíveis, risco de fraudes em valuation ou EBITDA inflado.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_growth_rate para taxas de crescimento ajustadas.',
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
                Ocorreu um erro ao processar o P/EBITDA: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe PEBITEvaluator para avaliar o indicador P/EBIT
class PEBITEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/EBIT
    def __init__(self):
        # Define string multilinha explicando o índice P/EBIT
        self.definicao = '''
        O P/EBIT (Preço / EBIT) mede o valor de mercado da empresa em relação ao seu lucro antes de juros e impostos (EBIT), calculado
        como (Valor de Mercado / EBIT). É um indicador de valuation que avalia se a empresa está cara ou barata com base em sua lucratividade operacional.
        Um P/EBIT baixo sugere subvalorização, enquanto valores altos indicam sobrevalorização ou expectativas de crescimento futuro.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/EBIT
        self.formula = 'P/EBIT = Valor de Mercado / EBIT'

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

    # Avalia o valor P/EBIT e retorna um objeto ResultadoIND
    def avaliar(self, p_ebit):
        # Tenta processar o valor P/EBIT
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_ebit, (int, float)) and not (isinstance(p_ebit, str) and p_ebit.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de P/EBIT deve ser numérico.")
            # Converte o P/EBIT para float para garantir que é numérico
            p_ebit = float(p_ebit)
            # Verifica se P/EBIT é negativo, indicando prejuízo operacional
            if p_ebit < 0:
                # Retorna ResultadoIND para P/EBIT negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/EBIT < 0',
                    descricao='Um P/EBIT negativo indica que o EBIT é negativo, sugerindo prejuízo operacional antes de juros e impostos. Isso pode refletir ineficiência operacional, altos custos ou perdas extraordinárias, tornando a valuation irrelevante e apontando para instabilidade financeira significativa.',
                    riscos='Risco de falência, reestruturação ou diluição acionária devido a prejuízos operacionais. Pode haver endividamento crescente ou perda de competitividade no mercado.',
                    referencia='Avalie evaluate_ebit_margin para eficiência operacional, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação operacional e EBIT positivo. Priorize análise de custos e estratégias de turnaround.'
                )
            # Verifica se P/EBIT está entre 0 e 8, indicando forte subvalorização
            elif 0 <= p_ebit <= 8:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/EBIT <= 8',
                    descricao='O P/EBIT está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação ao seu lucro operacional. Essa faixa indica oportunidades de compra, comum em empresas com EBIT sólido, mas preço de mercado deprimido devido a ciclos econômicos, baixa visibilidade ou setores menos atrativos.',
                    riscos='Risco de EBIT instável ou ativos superavaliados no valor de mercado. Pode haver desafios setoriais ou baixa percepção de crescimento que justifiquem o desconto no valuation.',
                    referencia='Analise evaluate_p_l para comparação de lucros, evaluate_roe para rentabilidade e evaluate_debt_to_ebit para alavancagem operacional.',
                    recomendacao='Considere investir, mas verifique a sustentabilidade do EBIT e a composição do valor de mercado. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/EBIT está entre 8 e 12, indicando valuation equilibrado
            elif 8 < p_ebit <= 12:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='8 < P/EBIT <= 12',
                    descricao='O P/EBIT está em uma faixa equilibrada, sugerindo que o valor de mercado está alinhado com o lucro operacional da empresa. Essa faixa é comum em empresas estáveis com EBIT consistente e crescimento moderado, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação no EBIT devido a concorrência ou custos crescentes. Pode haver dependência de fatores macroeconômicos que afetem o lucro operacional ou o preço de mercado.',
                    referencia='Compare com evaluate_evebit para valuation ajustado, evaluate_margem_ebit para eficiência e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de EBIT e planos de expansão antes de investir. Pode ser uma boa opção para investidores de longo prazo com foco em estabilidade.'
                )
            # Verifica se P/EBIT está entre 12 e 16, indicando valuation moderado
            elif 12 < p_ebit <= 16:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='12 < P/EBIT <= 16',
                    descricao='O P/EBIT está moderadamente elevado, indicando que o mercado atribui um prêmio ao lucro operacional da empresa. Essa faixa sugere expectativas de crescimento futuro ou confiança na gestão, comum em empresas com potencial moderado ou em setores com margens estáveis.',
                    riscos='Risco de correção no preço se o EBIT não crescer conforme esperado. Pode haver sobrevalorização devido a otimismo de mercado ou dependência de setores cíclicos.',
                    referencia='Verifique evaluate_p_ebitda para valuation ajustado, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para eficiência de caixa.',
                    recomendacao='Considere esperar por sinais de crescimento ou redução no valuation antes de investir. Combine com análise de margens e fluxo de caixa para validar o prêmio.'
                )
            # Verifica se P/EBIT está entre 16 e 20, indicando sobrevalorização
            elif 16 < p_ebit <= 20:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='16 < P/EBIT <= 20',
                    descricao='O P/EBIT está consideravelmente elevado, indicando sobrevalorização em relação ao lucro operacional. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado se não sustentado.',
                    riscos='Risco de queda no preço se o EBIT declinar ou expectativas não se realizarem. Pode haver bolhas setoriais ou dependência de fatores intangíveis no valuation.',
                    referencia='Combine com evaluate_psr para receita, evaluate_roic para retorno sobre capital e evaluate_current_ratio para liquidez operacional.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com EBIT crescente e fundamentos sólidos.'
                )
            # Verifica se P/EBIT excede 20, indicando sobrevalorização extrema
            elif p_ebit > 20:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='P/EBIT > 20',
                    descricao='O P/EBIT é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de crescimento operacional. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço de mercado desconecta dos fundamentos operacionais.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de fatores intangíveis, risco de fraudes em valuation ou EBIT inflado.',
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
                Ocorreu um erro ao processar o P/EBIT: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe PAtivoEvaluator para avaliar o indicador P/Ativo
class PAtivoEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/Ativo
    def __init__(self):
        # Define string multilinha explicando o índice P/Ativo
        self.definicao = '''
        O P/Ativo (Preço / Ativo) mede o valor de mercado da empresa em relação aos seus ativos totais, calculado
        como (Valor de Mercado / Ativos Totais). É um indicador de valuation que avalia se a empresa está cara ou barata
        com base em seus ativos. Um P/Ativo baixo sugere subvalorização, enquanto valores altos indicam sobrevalorização ou
        expectativas de alta rentabilidade sobre os ativos.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/Ativo
        self.formula = 'P/Ativo = Valor de Mercado / Ativos Totais'

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

    # Avalia o valor P/Ativo e retorna um objeto ResultadoIND
    def avaliar(self, p_ativo):
        # Tenta processar o valor P/Ativo
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(p_ativo, (int, float)) and not (isinstance(p_ativo, str) and p_ativo.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de P/Ativo deve ser numérico.")
            # Converte o P/Ativo para float para garantir que é numérico
            p_ativo = float(p_ativo)
            # Verifica se P/Ativo é menor ou igual a 0, indicando erro ou ativos negativos
            if p_ativo <= 0:
                # Retorna ResultadoIND para P/Ativo inválido
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/Ativo <= 0',
                    descricao='Um P/Ativo menor ou igual a zero é inválido, indicando valor de mercado nulo, negativo ou ativos totais negativos. Isso pode ocorrer em empresas com problemas contábeis graves, falência iminente ou erros nos dados financeiros, tornando a análise de valuation inviável.',
                    riscos='Risco de falência, manipulação contábil ou ativos superavaliados. Pode haver baixa liquidez de mercado ou necessidade de reestruturação financeira.',
                    referencia='Avalie evaluate_p_l para lucros, evaluate_roe para rentabilidade e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir devido a possíveis erros nos dados ou instabilidade financeira grave. Verifique relatórios financeiros detalhados antes de qualquer decisão.'
                )
            # Verifica se P/Ativo está entre 0 e 0.5, indicando forte subvalorização
            elif 0 < p_ativo <= 0.5:
                # Retorna ResultadoIND para forte subvalorização
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 < P/Ativo <= 0.5',
                    descricao='O P/Ativo está muito baixo, sugerindo que a empresa está fortemente subvalorizada em relação aos seus ativos. Essa faixa indica oportunidades de compra, comum em empresas com ativos significativos, mas preço de mercado deprimido devido a ciclos econômicos, má percepção de mercado ou setores menos atrativos.',
                    riscos='Risco de ativos obsoletos, baixa rentabilidade ou problemas operacionais que justifiquem o desconto. Pode haver dificuldades em converter ativos em lucros ou fluxo de caixa.',
                    referencia='Analise evaluate_p_l para comparação de lucros, evaluate_roa para rentabilidade dos ativos e evaluate_debt_to_assets para alavancagem.',
                    recomendacao='Considere investir, mas verifique a qualidade dos ativos e a capacidade de geração de lucros. Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se P/Ativo está entre 0.5 e 1, indicando valuation equilibrado
            elif 0.5 < p_ativo <= 1:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.5 < P/Ativo <= 1',
                    descricao='O P/Ativo está em uma faixa equilibrada, sugerindo que o valor de mercado da empresa está alinhado com seus ativos totais. Essa faixa é comum em empresas estáveis com rentabilidade moderada, onde o mercado precifica os ativos de forma justa, sem grandes descontos ou prêmios.',
                    riscos='Risco de estagnação na valorização se os ativos não forem utilizados de forma eficiente. Pode haver dependência de fatores macroeconômicos que afetem o valor de mercado.',
                    referencia='Compare com evaluate_p_vp para valor patrimonial, evaluate_margem_liquida para eficiência e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de rentabilidade e utilização de ativos antes de investir. Pode ser uma boa opção para investidores que buscam estabilidade.'
                )
            # Verifica se P/Ativo está entre 1 e 1.5, indicando valuation moderado
            elif 1 < p_ativo <= 1.5:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1 < P/Ativo <= 1.5',
                    descricao='O P/Ativo está moderadamente elevado, sugerindo que o mercado atribui um prêmio aos ativos da empresa. Essa faixa indica expectativas de rentabilidade acima da média ou crescimento futuro, comum em empresas com ativos intangíveis valiosos ou em setores com potencial moderado.',
                    riscos='Risco de correção no preço se a rentabilidade dos ativos não atender às expectativas. Pode haver sobrevalorização de ativos intangíveis ou dependência de setores cíclicos.',
                    referencia='Verifique evaluate_evebitda para valuation operacional, evaluate_roic para retorno sobre capital e evaluate_beta para volatilidade.',
                    recomendacao='Considere esperar por sinais de crescimento ou melhoria na rentabilidade antes de investir. Combine com análise de fluxo de caixa e qualidade dos ativos.'
                )
            # Verifica se P/Ativo está entre 1.5 e 2, indicando sobrevalorização
            elif 1.5 < p_ativo <= 2:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='1.5 < P/Ativo <= 2',
                    descricao='O P/Ativo está consideravelmente elevado, indicando sobrevalorização em relação aos ativos totais. Essa faixa sugere que o mercado espera alta rentabilidade ou crescimento futuro, comum em empresas de tecnologia ou setores premium, mas o preço reflete otimismo que pode ser arriscado.',
                    riscos='Risco de queda no preço se os ativos não gerarem retornos esperados. Pode haver sobrevalorização de intangíveis ou bolhas setoriais impulsionadas por hype de mercado.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para eficiência e evaluate_cash_conversion_cycle para ciclo de caixa.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios financeiros. Invista com cautela, priorizando empresas com ativos produtivos e rentabilidade sólida.'
                )
            # Verifica se P/Ativo excede 2, indicando sobrevalorização extrema
            elif p_ativo > 2:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='P/Ativo > 2',
                    descricao='O P/Ativo é extremamente elevado, sugerindo forte sobrevalorização em relação aos ativos totais. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço de mercado desconecta significativamente dos ativos subjacentes.',
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
                Ocorreu um erro ao processar o P/Ativo: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )

# Define a classe DivLiquidaPatrimonioLiquidoEvaluator para avaliar o indicador Dívida Líquida / Patrimônio Líquido
class DivLiquidaPatrimonioLiquidoEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do Dívida Líquida / Patrimônio Líquido
    def __init__(self):
        # Define string multilinha explicando o índice Dívida Líquida / Patrimônio Líquido
        self.definicao = '''
        A Dívida Líquida / Patrimônio Líquido mede o nível de endividamento da empresa em relação ao seu patrimônio líquido. É calculado
        como (Dívida Líquida / Patrimônio Líquido), onde Dívida Líquida = Dívida Total - Caixa e Equivalentes. É um indicador de solvência
        que avalia a proporção de dívida financiada em relação ao capital próprio dos acionistas. Um valor baixo sugere baixa alavancagem,
        enquanto valores altos indicam risco financeiro elevado.
        '''
        # Define a categoria de agrupamento como "Solvência"
        self.agrupador = 'Solvência'
        # Define a fórmula do Dívida Líquida / Patrimônio Líquido
        self.formula = 'Dívida Líquida / Patrimônio Líquido = (Dívida Total - Caixa e Equivalentes) / Patrimônio Líquido'

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

    # Avalia o valor Dívida Líquida / Patrimônio Líquido e retorna um objeto ResultadoIND
    def avaliar(self, div_pl):
        # Tenta processar o valor Dívida Líquida / Patrimônio Líquido
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(div_pl, (int, float)) and not (isinstance(div_pl, str) and div_pl.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de Dívida Líquida / Patrimônio Líquido deve ser numérico.")
            # Converte o Dívida Líquida / Patrimônio Líquido para float para garantir que é numérico
            div_pl = float(div_pl)
            # Verifica se Dívida Líquida / Patrimônio Líquido é negativo, indicando excesso de caixa ou patrimônio líquido negativo
            if div_pl < 0:
                # Retorna ResultadoIND para Dívida Líquida / Patrimônio Líquido negativo
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dívida Líquida / PL < 0',
                    descricao='Um valor negativo pode indicar que a empresa possui mais caixa do que dívidas ou que o patrimônio líquido é negativo. Um excesso de caixa sugere uma posição financeira sólida, mas um patrimônio líquido negativo aponta para prejuízos acumulados ou problemas estruturais, exigindo análise detalhada.',
                    riscos='Se causado por excesso de caixa, risco de ineficiência no uso de capital (caixa ocioso). Se devido a patrimônio líquido negativo, risco de falência, diluição acionária ou reestruturação financeira.',
                    referencia='Avalie evaluate_cash_flow para geração de caixa, evaluate_roe para rentabilidade e evaluate_debt_to_ebitda para alavancagem operacional.',
                    recomendacao='Se excesso de caixa, verifique planos de investimento ou retorno aos acionistas. Se patrimônio líquido negativo, evite investir até sinais claros de recuperação financeira.'
                )
            # Verifica se Dívida Líquida / Patrimônio Líquido está entre 0 e 0.5, indicando baixa alavancagem
            elif 0 <= div_pl <= 0.5:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= Dívida Líquida / PL <= 0.5',
                    descricao='A dívida líquida é muito baixa em relação ao patrimônio líquido, indicando que a empresa financia a maior parte de suas operações com capital próprio. Isso sugere solvência forte, baixa dependência de dívida e resiliência financeira, comum em empresas maduras ou com fluxo de caixa robusto.',
                    riscos='Risco de subalavancagem, onde a empresa perde oportunidades de crescimento via dívida barata. Pode haver conservadorismo excessivo ou setores de baixa intensidade de capital.',
                    referencia='Analise evaluate_roe para rentabilidade sobre patrimônio, evaluate_ebitda_margin para eficiência operacional e evaluate_capex para investimentos em capital.',
                    recomendacao='Considere investir para estabilidade financeira. Avalie se a baixa alavancagem permite expansão ou aquisições sem comprometer a solvência.'
                )
            # Verifica se Dívida Líquida / Patrimônio Líquido está entre 0.5 e 1, indicando alavancagem moderada
            elif 0.5 < div_pl <= 1:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='0.5 < Dívida Líquida / PL <= 1',
                    descricao='A dívida líquida é moderada em relação ao patrimônio líquido, sugerindo que a empresa equilibra capital próprio e dívida para financiar suas operações. Essa faixa indica alavancagem razoável, permitindo crescimento sem risco financeiro excessivo, comum em empresas em expansão controlada.',
                    riscos='Risco de aumento nos custos de juros se as taxas subirem ou lucros caírem. Pode haver dependência moderada de financiamento externo ou limitações em novos investimentos.',
                    referencia='Compare com evaluate_debt_to_ebitda para alavancagem operacional, evaluate_interest_coverage para cobertura de juros e evaluate_current_ratio para liquidez.',
                    recomendacao='Avalie o histórico de lucros e planos de redução de dívida. Pode ser uma boa opção para investidores que buscam equilíbrio entre risco e crescimento.'
                )
            # Verifica se Dívida Líquida / Patrimônio Líquido está entre 1 e 2, indicando alavancagem elevada
            elif 1 < div_pl <= 2:
                # Retorna ResultadoIND para alavancagem elevada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1 < Dívida Líquida / PL <= 2',
                    descricao='A dívida líquida é elevada em relação ao patrimônio líquido, indicando que a dívida é até duas vezes maior que o capital próprio. Essa faixa sugere alavancagem moderada-alta, comum em setores capital-intensivos como infraestrutura, energia ou manufatura pesada.',
                    riscos='Risco de pressão financeira se os lucros diminuírem ou taxas de juros aumentarem. Pode haver restrições de credores ou limitações em novos investimentos e distribuições.',
                    referencia='Verifique evaluate_peg_ratio para crescimento ajustado, evaluate_evebitda para valuation e evaluate_beta para volatilidade.',
                    recomendacao='Considere investir com cautela, monitorando a geração de caixa e planos de desalavancagem. Priorize empresas com lucros consistentes e fluxo de caixa robusto.'
                )
            # Verifica se Dívida Líquida / Patrimônio Líquido está entre 2 e 3, indicando risco financeiro alto
            elif 2 < div_pl <= 3:
                # Retorna ResultadoIND para risco financeiro alto
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='2 < Dívida Líquida / PL <= 3',
                    descricao='A dívida líquida é alta em relação ao patrimônio líquido, indicando que a dívida é até três vezes maior que o capital próprio. Essa faixa sugere risco financeiro significativo, comum em empresas em recuperação, com aquisições agressivas ou em setores cíclicos com alta alavancagem.',
                    riscos='Risco de default em dívidas se houver desaceleração econômica ou queda na receita. Pode haver restrições de credores, diluição acionária ou necessidade de venda de ativos.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para eficiência e evaluate_cash_conversion_cycle para ciclo de caixa.',
                    recomendacao='Evite investir a menos que haja planos claros de desalavancagem ou recuperação. Monitore relatórios trimestrais para sinais de melhoria financeira.'
                )
            # Verifica se Dívida Líquida / Patrimônio Líquido excede 3, indicando risco financeiro crítico
            elif div_pl > 3:
                # Retorna ResultadoIND para risco financeiro crítico
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dívida Líquida / PL > 3',
                    descricao='A dívida líquida é extremamente alta em relação ao patrimônio líquido, indicando que a dívida excede três vezes o capital próprio. Essa faixa sugere alavancagem excessiva e vulnerabilidade financeira grave, comum em empresas em crise, com expansões mal planejadas ou em setores sob pressão financeira.',
                    riscos='Alto risco de insolvência, reestruturação de dívida ou falência. Pode haver custos elevados de juros, redução drástica de investimentos e impacto severo na cotação das ações.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_p_l para lucros.',
                    recomendacao='Não invista devido ao risco elevado de perdas. Considere apenas se houver turnaround comprovado ou suporte externo, como injeção de capital.'
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
                Ocorreu um erro ao processar o Dívida Líquida / Patrimônio Líquido: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


# Define a classe DivLiquidaEBITEvaluator para avaliar o indicador Dívida Líquida / EBIT
class DivLiquidaEBITEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do Dívida Líquida / EBIT
    def __init__(self):
        # Define string multilinha explicando o índice Dívida Líquida / EBIT
        self.definicao = '''
        A Dívida Líquida / EBIT mede o nível de endividamento da empresa em relação ao seu lucro antes de juros e impostos (EBIT). É calculado
        como (Dívida Líquida / EBIT), onde Dívida Líquida = Dívida Total - Caixa e Equivalentes. É um indicador de solvência que avalia
        a capacidade da empresa de pagar suas dívidas com seu lucro operacional. Um valor baixo sugere baixa alavancagem, enquanto valores altos indicam risco financeiro elevado.
        '''
        # Define a categoria de agrupamento como "Solvência"
        self.agrupador = 'Solvência'
        # Define a fórmula do Dívida Líquida / EBIT
        self.formula = 'Dívida Líquida / EBIT = (Dívida Total - Caixa e Equivalentes) / EBIT'

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

    # Avalia o valor Dívida Líquida / EBIT e retorna um objeto ResultadoIND
    def avaliar(self, div_ebit):
        # Tenta processar o valor Dívida Líquida / EBIT
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(div_ebit, (int, float)) and not (isinstance(div_ebit, str) and div_ebit.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de Dívida Líquida / EBIT deve ser numérico.")
            # Converte o Dívida Líquida / EBIT para float para garantir que é numérico
            div_ebit = float(div_ebit)
            # Verifica se Dívida Líquida / EBIT é negativo, indicando excesso de caixa ou EBIT negativo
            if div_ebit < 0:
                # Retorna ResultadoIND para Dívida Líquida / EBIT negativo
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dívida Líquida / EBIT < 0',
                    descricao='Um valor negativo pode indicar que a empresa possui mais caixa do que dívidas ou que o EBIT é negativo. Um excesso de caixa sugere uma posição financeira sólida, mas um EBIT negativo aponta para prejuízo operacional, exigindo análise cuidadosa do contexto.',
                    riscos='Se causado por excesso de caixa, risco de ineficiência no uso de capital (caixa ocioso). Se devido a EBIT negativo, risco de falência ou reestruturação. Pode haver baixa rentabilidade ou necessidade de capital externo.',
                    referencia='Avalie evaluate_ebit_margin para eficiência operacional, evaluate_cash_flow para geração de caixa e evaluate_roe para rentabilidade sobre patrimônio.',
                    recomendacao='Se excesso de caixa, verifique planos de investimento ou retorno aos acionistas. Se EBIT negativo, evite investir até recuperação operacional ser comprovada.'
                )
            # Verifica se Dívida Líquida / EBIT está entre 0 e 1.5, indicando baixa alavancagem
            elif 0 <= div_ebit <= 1.5:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= Dívida Líquida / EBIT <= 1.5',
                    descricao='A dívida líquida é muito baixa em relação ao EBIT, indicando que a empresa pode quitar suas dívidas com menos de 1,5 anos de lucro operacional. Isso sugere solvência forte, baixa dependência de financiamento externo e capacidade de suportar crises, comum em empresas maduras com fluxos estáveis.',
                    riscos='Risco de subalavancagem, onde a empresa perde oportunidades de crescimento via dívida barata. Pode haver conservadorismo excessivo ou setores de baixa intensidade de capital.',
                    referencia='Analise evaluate_roe para rentabilidade, evaluate_ebit_margin para eficiência operacional e evaluate_capex para investimentos em capital.',
                    recomendacao='Considere investir para estabilidade financeira. Avalie se a baixa alavancagem permite expansão ou aquisições sem comprometer a solvência.'
                )
            # Verifica se Dívida Líquida / EBIT está entre 1.5 e 3, indicando alavancagem moderada
            elif 1.5 < div_ebit <= 3:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1.5 < Dívida Líquida / EBIT <= 3',
                    descricao='A dívida líquida é moderada em relação ao EBIT, sugerindo que a empresa pode quitar suas dívidas em até três anos de lucro operacional. Essa faixa indica alavancagem equilibrada, permitindo crescimento sem risco financeiro excessivo, comum em empresas em expansão controlada.',
                    riscos='Risco de aumento nos custos de juros se as taxas subirem ou EBIT cair. Pode haver dependência de financiamento para operações ou limitações em novos investimentos.',
                    referencia='Compare com evaluate_debt_to_equity para estrutura de capital, evaluate_interest_coverage para cobertura de juros e evaluate_current_ratio para liquidez.',
                    recomendacao='Avalie o histórico de EBIT e planos de redução de dívida. Pode ser uma boa opção para investidores que buscam equilíbrio entre risco e crescimento.'
                )
            # Verifica se Dívida Líquida / EBIT está entre 3 e 4.5, indicando alavancagem elevada
            elif 3 < div_ebit <= 4.5:
                # Retorna ResultadoIND para alavancagem elevada
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='3 < Dívida Líquida / EBIT <= 4.5',
                    descricao='A dívida líquida é elevada em relação ao EBIT, indicando que a empresa precisaria de até 4,5 anos de lucro operacional para quitar suas dívidas. Essa faixa sugere alavancagem moderada-alta, comum em setores capital-intensivos como infraestrutura ou manufatura pesada.',
                    riscos='Risco de pressão financeira se o EBIT declinar devido a recessões ou custos crescentes. Pode haver restrições de credores ou limitações em novos investimentos.',
                    referencia='Verifique evaluate_peg_ratio para crescimento ajustado, evaluate_evebit para valuation e evaluate_beta para volatilidade.',
                    recomendacao='Considere investir com cautela, monitorando a estabilidade do EBIT e planos de desalavancagem. Priorize empresas com lucros operacionais consistentes.'
                )
            # Verifica se Dívida Líquida / EBIT está entre 4.5 e 6, indicando risco financeiro alto
            elif 4.5 < div_ebit <= 6:
                # Retorna ResultadoIND para risco financeiro alto
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='4.5 < Dívida Líquida / EBIT <= 6',
                    descricao='A dívida líquida é alta em relação ao EBIT, sugerindo que a empresa precisaria de até seis anos de lucro operacional para quitar suas dívidas. Essa faixa indica risco financeiro significativo, comum em empresas em recuperação, com aquisições agressivas ou em setores cíclicos.',
                    riscos='Risco de default em dívidas se houver desaceleração econômica ou queda no EBIT. Pode haver restrições de credores, diluição acionária ou necessidade de reestruturação.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_ebit para eficiência e evaluate_cash_conversion_cycle para ciclo de caixa.',
                    recomendacao='Evite investir a menos que haja planos claros de desalavancagem ou recuperação. Monitore relatórios trimestrais para sinais de melhoria no EBIT.'
                )
            # Verifica se Dívida Líquida / EBIT excede 6, indicando risco financeiro crítico
            elif div_ebit > 6:
                # Retorna ResultadoIND para risco financeiro crítico
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dívida Líquida / EBIT > 6',
                    descricao='A dívida líquida é extremamente alta em relação ao EBIT, indicando que a empresa precisaria de mais de seis anos de lucro operacional para quitar suas dívidas. Essa faixa sugere alavancagem excessiva e vulnerabilidade financeira, comum em empresas em crise ou com expansões mal planejadas.',
                    riscos='Alto risco de insolvência, reestruturação de dívida ou falência. Pode haver custos elevados de juros, redução de investimentos e impacto severo na cotação das ações.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_p_l para lucros.',
                    recomendacao='Não invista devido ao risco elevado de perdas. Considere apenas se houver turnaround comprovado ou suporte externo, como injeção de capital.'
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
                Ocorreu um erro ao processar o Dívida Líquida / EBIT: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe MargemLiquidaEvaluator para avaliar o indicador Margem Líquida
class MargemLiquidaEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula da Margem Líquida
    def __init__(self):
        # Define string multilinha explicando o índice Margem Líquida
        self.definicao = '''
        A Margem Líquida mede a rentabilidade final da empresa, calculada como
        (Lucro Líquido / Receita Líquida) * 100. É um indicador de eficiência que mostra a porcentagem da receita que resta após todos os custos, despesas, juros e impostos. Uma margem líquida alta sugere forte lucratividade e eficiência geral, enquanto valores baixos indicam pressão de custos ou baixa rentabilidade.
        '''
        # Define a categoria de agrupamento como "Rentabilidade"
        self.agrupador = 'Rentabilidade'
        # Define a fórmula da Margem Líquida
        self.formula = 'Margem Líquida (%) = (Lucro Líquido / Receita Líquida) * 100'

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

    # Avalia o valor da Margem Líquida e retorna um objeto ResultadoIND
    def avaliar(self, margem_liquida):
        # Tenta processar o valor da Margem Líquida
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(margem_liquida, (int, float)) and not (isinstance(margem_liquida, str) and margem_liquida.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Margem Líquida deve ser numérico.")
            # Converte a Margem Líquida para float para garantir que é numérico
            margem_liquida = float(margem_liquida)
            # Verifica se Margem Líquida é negativa, indicando prejuízo líquido
            if margem_liquida < 0:
                # Retorna ResultadoIND para Margem Líquida negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Margem Líquida < 0%',
                    descricao='Uma Margem Líquida negativa indica que a empresa está operando com prejuízo após todos os custos, despesas, juros e impostos. Isso sugere ineficiência operacional grave, altos encargos financeiros ou perdas extraordinárias, comum em empresas em crise ou setores com margens apertadas.',
                    riscos='Risco de insustentabilidade financeira, com potencial para falência, reestruturação ou diluição acionária. Pode haver aumento de endividamento para cobrir prejuízos ou perda de competitividade.',
                    referencia='Avalie evaluate_ebitda_margin para lucro operacional ajustado, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação de lucratividade. Priorize análise de custos, estrutura de capital e estratégias de turnaround.'
                )
            # Verifica se Margem Líquida está entre 0 e 5, indicando rentabilidade baixa
            elif 0 <= margem_liquida <= 5:
                # Retorna ResultadoIND para rentabilidade baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem Líquida <= 5%',
                    descricao='A Margem Líquida está baixa, sugerindo rentabilidade final limitada após todos os custos e despesas. Isso é comum em setores com alta concorrência, custos elevados ou baixa escala, como varejo ou indústrias intensivas, onde a precificação é pressionada ou há encargos financeiros elevados.',
                    riscos='Risco de margens comprimidas por aumento de custos, juros altos ou impostos elevados. Pode haver vulnerabilidade a choques econômicos ou dependência de economias de escala.',
                    referencia='Analise evaluate_margem_bruta para custos diretos, evaluate_ebit_margin para eficiência operacional e evaluate_debt_to_equity para alavancagem.',
                    recomendacao='Considere investir apenas se houver estratégias claras para redução de custos ou aumento de lucros. Verifique tendências de receita e competitividade setorial.'
                )
            # Verifica se Margem Líquida está entre 5 e 15, indicando rentabilidade moderada
            elif 5 < margem_liquida <= 15:
                # Retorna ResultadoIND para rentabilidade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5 < Margem Líquida <= 15%',
                    descricao='A Margem Líquida está em uma faixa moderada, indicando rentabilidade final razoável após todos os custos. Essa faixa é comum em empresas com controle de despesas decente, mas sem forte poder de precificação, como manufatura ou serviços com margens estáveis.',
                    riscos='Risco de volatilidade nas margens devido a flutuações nos custos, encargos financeiros ou mudanças tributárias. Pode haver limitações em financiar crescimento sem comprometer lucros.',
                    referencia='Compare com evaluate_margem_ebitda para lucro ajustado, evaluate_roe para rentabilidade sobre patrimônio e evaluate_market_share para posição competitiva.',
                    recomendacao='Avalie o histórico de lucros e estratégias de otimização antes de investir. Pode ser uma boa opção para investidores que buscam equilíbrio entre risco e retorno.'
                )
            # Verifica se Margem Líquida está entre 15 e 25, indicando boa rentabilidade
            elif 15 < margem_liquida <= 25:
                # Retorna ResultadoIND para boa rentabilidade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='15 < Margem Líquida <= 25%',
                    descricao='A Margem Líquida está em uma faixa alta, sugerindo boa rentabilidade final e eficiência geral. Essa faixa é comum em empresas com forte poder de precificação, controle de custos ou operações otimizadas, como tecnologia, bens de consumo de marca ou serviços especializados.',
                    riscos='Risco de dependência de mercados premium ou produtos chave. Aumento de custos regulatórios, juros ou impostos pode reduzir margens no futuro.',
                    referencia='Verifique evaluate_margem_operacional para eficiência geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão de receita.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade das margens e a força competitiva da empresa.'
                )
            # Verifica se Margem Líquida excede 25, indicando rentabilidade excepcional
            elif margem_liquida > 25:
                # Retorna ResultadoIND para rentabilidade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem Líquida > 25%',
                    descricao='A Margem Líquida é extremamente alta, indicando rentabilidade final excepcional e eficiência superior. Essa faixa é típica de empresas com marcas premium, baixa concorrência ou modelos de negócios escaláveis, como software, tecnologia ou bens de luxo, onde os lucros líquidos são robustos.',
                    riscos='Risco de sobredependência de nichos de mercado ou inovações específicas. Mudanças regulatórias, entrada de concorrentes ou saturação podem impactar margens futuras.',
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
                Ocorreu um erro ao processar a Margem Líquida: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe MargemEBITDAEvaluator para avaliar o indicador Margem EBITDA
class MargemEBITDAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula da Margem EBITDA
    def __init__(self):
        # Define string multilinha explicando o índice Margem EBITDA
        self.definicao = '''
        A Margem EBITDA mede a rentabilidade operacional ajustada da empresa, calculada como
        (EBITDA / Receita Líquida) * 100. É um indicador de eficiência que mostra a porcentagem da receita que resta após custos operacionais, antes de juros, impostos, depreciação e amortização. Uma margem EBITDA alta sugere forte geração de caixa operacional, enquanto valores baixos indicam ineficiência ou pressão de custos.
        '''
        # Define a categoria de agrupamento como "Eficiência Operacional"
        self.agrupador = 'Eficiência Operacional'
        # Define a fórmula da Margem EBITDA
        self.formula = 'Margem EBITDA (%) = (EBITDA / Receita Líquida) * 100'

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

    # Avalia o valor da Margem EBITDA e retorna um objeto ResultadoIND
    def avaliar(self, margem_ebitda):
        # Tenta processar o valor da Margem EBITDA
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(margem_ebitda, (int, float)) and not (isinstance(margem_ebitda, str) and margem_ebitda.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Margem EBITDA deve ser numérico.")
            # Converte a Margem EBITDA para float para garantir que é numérico
            margem_ebitda = float(margem_ebitda)
            # Verifica se Margem EBITDA é negativa, indicando prejuízo operacional ajustado
            if margem_ebitda < 0:
                # Retorna ResultadoIND para Margem EBITDA negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Margem EBITDA < 0%',
                    descricao='Uma Margem EBITDA negativa indica que os custos operacionais, mesmo antes de depreciação e amortização, excedem a receita bruta, resultando em prejuízo operacional ajustado. Isso sugere ineficiência grave, altos custos fixos ou problemas de mercado, comum em empresas em crise ou setores altamente competitivos.',
                    riscos='Risco de insustentabilidade financeira, com potencial para falência, reestruturação ou necessidade de capital externo. Pode haver aumento de endividamento para cobrir déficits operacionais ou perda de competitividade.',
                    referencia='Avalie evaluate_margem_bruta para custos diretos, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa ajustada.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação no EBITDA. Priorize análise de eficiência operacional, redução de custos e estratégias de recuperação.'
                )
            # Verifica se Margem EBITDA está entre 0 e 10, indicando eficiência baixa
            elif 0 <= margem_ebitda <= 10:
                # Retorna ResultadoIND para eficiência baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem EBITDA <= 10%',
                    descricao='A Margem EBITDA está baixa, sugerindo eficiência operacional limitada e fraca geração de caixa ajustada. Isso é comum em setores com alta concorrência, custos operacionais elevados ou baixa escala, como varejo ou indústrias de commodities, onde as margens são comprimidas.',
                    riscos='Risco de margens reduzidas por aumento de custos ou queda na receita. Pode haver vulnerabilidade a choques econômicos, como inflação de insumos, ou dependência de economias de escala.',
                    referencia='Analise evaluate_margem_ebit para lucro operacional puro, evaluate_cost_structure para composição de despesas e evaluate_pricing_power para capacidade de repasse.',
                    recomendacao='Considere investir apenas se houver estratégias claras para redução de custos ou aumento de receita. Verifique tendências de mercado e competitividade setorial.'
                )
            # Verifica se Margem EBITDA está entre 10 e 20, indicando eficiência moderada
            elif 10 < margem_ebitda <= 20:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='10 < Margem EBITDA <= 20%',
                    descricao='A Margem EBITDA está em uma faixa moderada, indicando eficiência operacional razoável e geração de caixa adequada. Essa faixa é comum em empresas com controle de custos decente, mas sem forte poder de precificação, como manufatura ou serviços com margens estáveis.',
                    riscos='Risco de volatilidade nas margens devido a flutuações nos custos operacionais ou concorrência crescente. Pode haver limitações em financiar crescimento sem comprometer a geração de caixa.',
                    referencia='Compare com evaluate_margem_bruta para eficiência inicial, evaluate_roe para rentabilidade sobre patrimônio e evaluate_market_share para posição competitiva.',
                    recomendacao='Avalie o histórico de margens e estratégias de otimização antes de investir. Pode ser uma boa opção para investidores que buscam equilíbrio entre risco e estabilidade operacional.'
                )
            # Verifica se Margem EBITDA está entre 20 e 30, indicando boa eficiência
            elif 20 < margem_ebitda <= 30:
                # Retorna ResultadoIND para boa eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='20 < Margem EBITDA <= 30%',
                    descricao='A Margem EBITDA está em uma faixa alta, sugerindo boa eficiência operacional e forte geração de caixa ajustada. Essa faixa é comum em empresas com poder de precificação sólido ou operações otimizadas, como tecnologia, bens de consumo de marca ou serviços especializados.',
                    riscos='Risco de dependência de produtos premium ou mercados específicos. Aumento de custos regulatórios ou entrada de concorrentes pode reduzir margens no futuro.',
                    referencia='Verifique evaluate_ebit_margin para eficiência sem depreciação, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão de receita.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade das margens e a força competitiva da empresa.'
                )
            # Verifica se Margem EBITDA excede 30, indicando eficiência excepcional
            elif margem_ebitda > 30:
                # Retorna ResultadoIND para eficiência excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem EBITDA > 30%',
                    descricao='A Margem EBITDA é extremamente alta, indicando eficiência operacional excepcional e forte geração de caixa. Essa faixa é típica de empresas com marcas premium, baixa concorrência ou modelos de negócios escaláveis, como software, tecnologia ou bens de luxo, onde os lucros operacionais ajustados são robustos.',
                    riscos='Risco de sobredependência de nichos de mercado ou inovações específicas. Mudanças regulatórias, entrada de concorrentes ou saturação podem impactar margens futuras.',
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
                Ocorreu um erro ao processar a Margem EBITDA: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


# Define a classe MargemEBITEvaluator para avaliar o indicador Margem EBIT
class MargemEBITEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula da Margem EBIT
    def __init__(self):
        # Define string multilinha explicando o índice Margem EBIT
        self.definicao = '''
        A Margem EBIT mede a rentabilidade operacional da empresa, calculada como
        (EBIT / Receita Líquida) * 100. É um indicador de eficiência que mostra a porcentagem da receita que resta após custos operacionais, antes de juros e impostos. Uma margem EBIT alta sugere forte desempenho operacional, enquanto valores baixos indicam ineficiência ou pressão de custos.
        '''
        # Define a categoria de agrupamento como "Eficiência Operacional"
        self.agrupador = 'Eficiência Operacional'
        # Define a fórmula da Margem EBIT
        self.formula = 'Margem EBIT (%) = (EBIT / Receita Líquida) * 100'

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

    # Avalia o valor da Margem EBIT e retorna um objeto ResultadoIND
    def avaliar(self, margem_ebit):
        # Tenta processar o valor da Margem EBIT
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(margem_ebit, (int, float)) and not (isinstance(margem_ebit, str) and margem_ebit.replace('.', '', 1).isdigit()):
                raise ValueError("O valor da Margem EBIT deve ser numérico.")
            # Converte a Margem EBIT para float para garantir que é numérico
            margem_ebit = float(margem_ebit)
            # Verifica se Margem EBIT é negativa, indicando prejuízo operacional
            if margem_ebit < 0:
                # Retorna ResultadoIND para Margem EBIT negativa
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Margem EBIT < 0%',
                    descricao='Uma Margem EBIT negativa indica que os custos operacionais excedem a receita bruta, resultando em prejuízo antes de juros e impostos. Isso pode sinalizar ineficiência grave, altos custos fixos ou problemas de precificação, comum em empresas em crise ou setores com margens apertadas.',
                    riscos='Risco de insustentabilidade financeira, com potencial para falência ou reestruturação. Pode haver aumento de endividamento para cobrir prejuízos ou perda de competitividade no mercado.',
                    referencia='Avalie evaluate_ebitda_margin para lucro ajustado, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa operacional.',
                    recomendacao='Evite investir até que a empresa demonstre controle de custos e retorno ao positivo. Priorize análise de eficiência operacional e estratégias de turnaround.'
                )
            # Verifica se Margem EBIT está entre 0 e 5, indicando eficiência baixa
            elif 0 <= margem_ebit <= 5:
                # Retorna ResultadoIND para eficiência baixa
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= Margem EBIT <= 5%',
                    descricao='A Margem EBIT está baixa, sugerindo eficiência operacional limitada. Isso é comum em setores com alta concorrência, custos elevados ou baixa escala, como manufatura intensiva ou varejo, onde a precificação é pressionada e os lucros operacionais são mínimos.',
                    riscos='Risco de margens comprimidas por flutuações nos custos ou demanda fraca. Pode haver dependência de economias de escala ou vulnerabilidade a choques econômicos como inflação.',
                    referencia='Analise evaluate_margem_bruta para custos diretos, evaluate_cost_structure para composição de despesas e evaluate_pricing_power para capacidade de repasse.',
                    recomendacao='Considere investir apenas se houver planos claros para melhoria de margens ou redução de custos. Verifique tendências de receita e competitividade setorial.'
                )
            # Verifica se Margem EBIT está entre 5 e 15, indicando eficiência moderada
            elif 5 < margem_ebit <= 15:
                # Retorna ResultadoIND para eficiência moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='5 < Margem EBIT <= 15%',
                    descricao='A Margem EBIT está em uma faixa moderada, indicando eficiência operacional razoável. Essa faixa é comum em empresas com controle de custos decente, mas sem grande poder de precificação, como serviços ou indústrias com margens estáveis e operações otimizadas moderadamente.',
                    riscos='Risco de volatilidade nas margens devido a custos variáveis ou concorrência crescente. Pode haver limitações em investir em inovação sem comprometer os lucros operacionais.',
                    referencia='Compare com evaluate_ebit_margin para eficiência, evaluate_roe para rentabilidade sobre patrimônio e evaluate_market_share para posição competitiva.',
                    recomendacao='Avalie o histórico de margens e estratégias de otimização antes de investir. Pode ser uma boa opção para investidores que buscam equilíbrio entre risco e estabilidade operacional.'
                )
            # Verifica se Margem EBIT está entre 15 e 25, indicando boa eficiência
            elif 15 < margem_ebit <= 25:
                # Retorna ResultadoIND para boa eficiência
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='15 < Margem EBIT <= 25%',
                    descricao='A Margem EBIT está em uma faixa alta, sugerindo boa eficiência operacional e controle de despesas. Essa faixa é comum em empresas com forte poder de precificação ou operações otimizadas, como tecnologia ou bens de consumo, onde os lucros operacionais são robustos.',
                    riscos='Risco de dependência de mercados premium ou produtos chave. Aumento de custos regulatórios ou perda de eficiência pode reduzir margens no futuro.',
                    referencia='Verifique evaluate_margem_operacional para análise geral, evaluate_roic para retorno sobre capital e evaluate_growth_rate para expansão de receita.',
                    recomendacao='Considere investir para crescimento ou renda, mas monitore a sustentabilidade das margens e a força competitiva da empresa.'
                )
            # Verifica se Margem EBIT excede 25, indicando eficiência excepcional
            elif margem_ebit > 25:
                # Retorna ResultadoIND para eficiência excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Margem EBIT > 25%',
                    descricao='A Margem EBIT é extremamente alta, indicando eficiência operacional excepcional e forte poder de precificação. Essa faixa é típica de empresas com marcas premium, baixa concorrência ou modelos de negócios escaláveis, como software ou serviços especializados, onde os lucros operacionais são elevados.',
                    riscos='Risco de sobredependência de nichos de mercado ou inovações específicas. Mudanças regulatórias, entrada de concorrentes ou saturação podem impactar margens futuras.',
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
                Ocorreu um erro ao processar a Margem EBIT: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


# Define a classe MargemBrutaEvaluator para avaliar o indicador Margem Bruta
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
# Define a classe EVEBITDAEvaluator para avaliar o indicador EV/EBITDA
class EVEBITDAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do EV/EBITDA
    def __init__(self):
        # Define string multilinha explicando o índice EV/EBITDA
        self.definicao = '''
        O EV/EBITDA (Enterprise Value / EBITDA) mede o valor da empresa em relação ao seu lucro antes de juros, impostos, depreciação e amortização (EBITDA). É calculado
        como (Enterprise Value / EBITDA), onde Enterprise Value = Valor de Mercado + Dívida Líquida - Caixa. É um indicador de valuation que avalia se a empresa está cara ou barata,
        ajustado para depreciação e amortização. Um EV/EBITDA baixo sugere subvalorização, enquanto valores altos indicam sobrevalorização ou expectativas de crescimento.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do EV/EBITDA
        self.formula = 'EV/EBITDA = Enterprise Value / EBITDA'

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

    # Avalia o valor EV/EBITDA e retorna um objeto ResultadoIND
    def avaliar(self, ev_ebitda):
        # Tenta processar o valor EV/EBITDA
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(ev_ebitda, (int, float)) and not (isinstance(ev_ebitda, str) and ev_ebitda.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de EV/EBITDA deve ser numérico.")
            # Converte o EV/EBITDA para float para garantir que é numérico
            ev_ebitda = float(ev_ebitda)
            # Verifica se EV/EBITDA é negativo, indicando prejuízo operacional ajustado
            if ev_ebitda < 0:
                # Retorna ResultadoIND para EV/EBITDA negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='EV/EBITDA < 0',
                    descricao='Um EV/EBITDA negativo indica que o EBITDA é negativo, sugerindo prejuízo operacional antes de depreciação e amortização. Isso pode sinalizar ineficiência grave, altos custos fixos ou perdas operacionais persistentes, tornando a valuation irrelevante e indicando instabilidade financeira extrema.',
                    riscos='Risco de falência, reestruturação ou venda de ativos forçada. Pode haver endividamento insustentável ou falta de competitividade, com impacto em liquidez e confiança do mercado.',
                    referencia='Avalie evaluate_ebit para lucro antes de juros e impostos, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa operacional.',
                    recomendacao='Evite investir até que a empresa demonstre EBITDA positivo e recuperação operacional. Priorize análise de custos fixos e eficiência antes de qualquer consideração.'
                )
            # Verifica se EV/EBITDA está entre 0 e 4, indicando subvalorização forte
            elif 0 <= ev_ebitda <= 4:
                # Retorna ResultadoIND para subvalorização forte
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= EV/EBITDA <= 4',
                    descricao='O EV/EBITDA está baixo, sugerindo que a empresa está fortemente subvalorizada em relação ao seu lucro operacional ajustado. Essa faixa indica oportunidades de compra atraentes, comum em empresas com EBITDA sólido, mas preço de mercado depreciado devido a ciclos econômicos, baixa visibilidade ou setores subestimados.',
                    riscos='Risco de EBITDA instável ou ativos superavaliados no EV. Pode haver desafios setoriais, como commoditização ou baixa crescimento, que justificam o desconto no valuation.',
                    referencia='Analise evaluate_p_ebitda para comparação setorial, evaluate_roe para rentabilidade sobre patrimônio e evaluate_debt_to_ebitda para alavancagem ajustada.',
                    recomendacao='Considere investir, mas verifique a sustentabilidade do EBITDA e a composição do EV (dívida vs. caixa). Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se EV/EBITDA está entre 4 e 8, indicando valuation equilibrado
            elif 4 < ev_ebitda <= 8:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='4 < EV/EBITDA <= 8',
                    descricao='O EV/EBITDA está em uma faixa equilibrada, sugerindo que a empresa tem um valuation razoável em relação ao seu lucro operacional ajustado. Essa faixa é comum em empresas estáveis com crescimento moderado e EBITDA consistente, refletindo confiança do mercado sem excesso de otimismo ou pessimismo.',
                    riscos='Risco de estagnação no EBITDA devido a concorrência intensa ou custos crescentes. Pode haver dependência de fatores macroeconômicos que afetem o lucro operacional ajustado.',
                    referencia='Compare com evaluate_evebit para valuation sem depreciação, evaluate_margem_ebitda para eficiência e evaluate_peg_ratio para crescimento ajustado.',
                    recomendacao='Avalie o histórico de EBITDA e planos de expansão antes de investir. Pode ser uma boa opção para investidores de longo prazo com foco em estabilidade financeira.'
                )
            # Verifica se EV/EBITDA está entre 8 e 12, indicando valuation moderado
            elif 8 < ev_ebitda <= 12:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='8 < EV/EBITDA <= 12',
                    descricao='O EV/EBITDA está moderadamente elevado, refletindo um prêmio pago pelo mercado pelo lucro operacional ajustado. Essa faixa sugere expectativas de crescimento futuro ou confiança na gestão, mas também uma avaliação cautelosa em setores com potencial moderado ou riscos operacionais.',
                    riscos='Risco de correção se o EBITDA não crescer conforme esperado. Setores cíclicos podem enfrentar volatilidade, e o prêmio pode não ser justificado por fundamentos fracos ou alta dívida no EV.',
                    referencia='Verifique evaluate_p_l para lucros, evaluate_beta para volatilidade e evaluate_cash_conversion_cycle para ciclo de caixa operacional.',
                    recomendacao='Considere esperar por melhores condições de mercado ou sinais de crescimento sustentável. Combine com análise de margens EBITDA e fluxo de caixa.'
                )
            # Verifica se EV/EBITDA está entre 12 e 16, indicando sobrevalorização
            elif 12 < ev_ebitda <= 16:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Elevado',
                    faixa='12 < EV/EBITDA <= 16',
                    descricao='O EV/EBITDA está consideravelmente elevado, indicando sobrevalorização em relação ao lucro operacional ajustado. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado se não suportado por fundamentos.',
                    riscos='Risco de queda no preço se o EBITDA declinar ou expectativas não se realizarem. Pode haver alavancagem excessiva no EV ou bolhas setoriais, com impacto em volatilidade.',
                    referencia='Combine com evaluate_psr para receita, evaluate_roic para retorno sobre capital investido e evaluate_current_ratio para liquidez ajustada.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com EBITDA crescente e baixa dívida líquida.'
                )
            # Verifica se EV/EBITDA excede 16, indicando sobrevalorização extrema
            elif ev_ebitda > 16:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Excessivo',
                    faixa='EV/EBITDA > 16',
                    descricao='O EV/EBITDA é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de crescimento. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço desconecta dos fundamentos operacionais ajustados.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de fatores intangíveis, risco de fraudes em valuation ou alta dívida inflando o EV.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_p_ativo para ativos e evaluate_growth_rate para taxas de crescimento projetadas.',
                    recomendacao='Não invista devido ao risco elevado. Considere vender posições existentes e buscar alternativas com valuation mais razoável e EBITDA sustentável.'
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
                Ocorreu um erro ao processar o EV/EBITDA: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )
# Define a classe EVEBITEvaluator para avaliar o indicador EV/EBIT
class EVEBITEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do EV/EBIT
    def __init__(self):
        # Define string multilinha explicando o índice EV/EBIT
        self.definicao = '''
        O EV/EBIT (Enterprise Value / EBIT) mede o valor da empresa em relação ao seu lucro antes de juros e impostos (EBIT). É calculado
        como (Enterprise Value / EBIT), onde Enterprise Value = Valor de Mercado + Dívida Líquida - Caixa. É um indicador de valuation que avalia
        se a empresa está cara ou barata, considerando sua dívida e caixa. Um EV/EBIT baixo sugere subvalorização, enquanto valores altos indicam sobrevalorização ou expectativas de crescimento.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do EV/EBIT
        self.formula = 'EV/EBIT = Enterprise Value / EBIT'

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

    # Avalia o valor EV/EBIT e retorna um objeto ResultadoIND
    def avaliar(self, ev_ebit):
        # Tenta processar o valor EV/EBIT
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(ev_ebit, (int, float)) and not (isinstance(ev_ebit, str) and ev_ebit.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de EV/EBIT deve ser numérico.")
            # Converte o EV/EBIT para float para garantir que é numérico
            ev_ebit = float(ev_ebit)
            # Verifica se EV/EBIT é negativo, indicando prejuízo operacional
            if ev_ebit < 0:
                # Retorna ResultadoIND para EV/EBIT negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='EV/EBIT < 0',
                    descricao='Um EV/EBIT negativo indica que o EBIT é negativo, sugerindo prejuízo operacional antes de juros e impostos. Isso pode sinalizar ineficiência operacional, altos custos ou perdas extraordinárias, tornando a valuation irrelevante ou indicando grave instabilidade financeira.',
                    riscos='Risco de falência ou reestruturação, com possível diluição acionária ou venda de ativos. Pode haver endividamento crescente ou falta de competitividade no mercado.',
                    referencia='Avalie evaluate_ebitda para lucro operacional ajustado, evaluate_roa para rentabilidade dos ativos e evaluate_cash_flow para geração de caixa.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação operacional e EBIT positivo. Priorize análise de custos e eficiência antes de considerar qualquer posição.'
                )
            # Verifica se EV/EBIT está entre 0 e 6, indicando subvalorização forte
            elif 0 <= ev_ebit <= 6:
                # Retorna ResultadoIND para subvalorização forte
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= EV/EBIT <= 6',
                    descricao='O EV/EBIT está baixo, sugerindo que a empresa está subvalorizada em relação ao seu lucro operacional. Essa faixa indica oportunidades de compra, comum em empresas com EBIT sólido, mas preço de mercado depreciado devido a ciclos econômicos ou baixa visibilidade.',
                    riscos='Risco de EBIT instável ou ativos superavaliados no EV. Pode haver desafios setoriais ou baixa crescimento que justifiquem o desconto no valuation.',
                    referencia='Analise evaluate_p_ebit para comparação setorial, evaluate_roe para rentabilidade sobre patrimônio e evaluate_debt_to_ebitda para alavancagem.',
                    recomendacao='Considere investir, mas verifique a sustentabilidade do EBIT e a composição do EV (dívida vs. caixa). Avalie se a subvalorização é temporária ou estrutural.'
                )
            # Verifica se EV/EBIT está entre 6 e 10, indicando valuation equilibrado
            elif 6 < ev_ebit <= 10:
                # Retorna ResultadoIND para valuation equilibrado
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='6 < EV/EBIT <= 10',
                    descricao='O EV/EBIT está em uma faixa equilibrada, sugerindo que a empresa tem um valuation razoável em relação ao seu lucro operacional. Essa faixa é comum em empresas estáveis com crescimento moderado e EBIT consistente, refletindo confiança do mercado sem excesso de otimismo.',
                    riscos='Risco de estagnação no EBIT devido a concorrência ou custos crescentes. Pode haver dependência de fatores macroeconômicos que afetem o lucro operacional.',
                    referencia='Compare com evaluate_evebitda para valuation ajustado, evaluate_margem_ebit para eficiência e evaluate_peg_ratio para crescimento.',
                    recomendacao='Avalie o histórico de EBIT e planos de expansão antes de investir. Pode ser uma boa opção para investidores de longo prazo com foco em estabilidade.'
                )
            # Verifica se EV/EBIT está entre 10 e 15, indicando valuation moderado
            elif 10 < ev_ebit <= 15:
                # Retorna ResultadoIND para valuation moderado
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='10 < EV/EBIT <= 15',
                    descricao='O EV/EBIT está moderadamente elevado, refletindo um prêmio pago pelo mercado pelo lucro operacional. Essa faixa sugere expectativas de crescimento futuro ou confiança na gestão, mas também uma avaliação cautelosa do mercado em setores com potencial moderado.',
                    riscos='Risco de correção se o EBIT não crescer conforme esperado. Setores cíclicos podem enfrentar volatilidade, e o prêmio pode não ser justificado por fundamentos fracos.',
                    referencia='Verifique evaluate_p_l para lucros, evaluate_beta para volatilidade e evaluate_cash_conversion para ciclo de caixa.',
                    recomendacao='Considere esperar por sinais de crescimento ou redução no EV antes de investir. Combine com análise de margens e fluxo de caixa para validar o prêmio.'
                )
            # Verifica se EV/EBIT está entre 15 e 20, indicando sobrevalorização
            elif 15 < ev_ebit <= 20:
                # Retorna ResultadoIND para sobrevalorização
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='15 < EV/EBIT <= 20',
                    descricao='O EV/EBIT está consideravelmente elevado, indicando sobrevalorização em relação ao lucro operacional. Essa faixa é comum em empresas com altas expectativas de crescimento ou em setores premium, mas o preço reflete otimismo significativo que pode ser arriscado.',
                    riscos='Risco de queda no preço se o EBIT declinar ou expectativas não se realizarem. Pode haver alavancagem excessiva no EV ou bolhas setoriais.',
                    referencia='Combine com evaluate_psr para receita, evaluate_roic para retorno sobre capital e evaluate_current_ratio para liquidez.',
                    recomendacao='Monitore catalisadores de crescimento e relatórios trimestrais. Invista com cautela, priorizando empresas com EBIT crescente e baixa dívida.'
                )
            # Verifica se EV/EBIT excede 20, indicando sobrevalorização extrema
            elif ev_ebit > 20:
                # Retorna ResultadoIND para sobrevalorização extrema
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='EV/EBIT > 20',
                    descricao='O EV/EBIT é extremamente elevado, sugerindo forte sobrevalorização ou expectativas irreais de crescimento. Essa faixa é típica de bolhas de mercado, empresas de alto crescimento especulativo ou narrativas hype, onde o preço desconecta dos fundamentos operacionais.',
                    riscos='Alto risco de correção acentuada no preço, com potencial para perdas significativas. Pode haver dependência de fatores intangíveis ou risco de fraudes em valuation.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_p_ativo para ativos e evaluate_growth_rate para taxas de crescimento.',
                    recomendacao='Não invista devido ao risco elevado. Considere vender posições existentes e buscar alternativas com valuation mais razoável.'
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
                Ocorreu um erro ao processar o EV/EBIT: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )


# Define a classe DivLiquidaEBITDAEvaluator para avaliar o indicador Dívida Líquida / EBITDA
class DivLiquidaEBITDAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do Dívida Líquida / EBITDA
    def __init__(self):
        # Define string multilinha explicando o índice Dívida Líquida / EBITDA
        self.definicao = '''
        A Dívida Líquida / EBITDA mede o nível de endividamento da empresa em relação ao seu lucro operacional antes de juros, impostos, depreciação e amortização (EBITDA). É calculado
        como (Dívida Líquida / EBITDA). É um indicador de solvência que avalia a capacidade da empresa de pagar suas dívidas com sua geração de caixa operacional. Um valor baixo sugere baixa alavancagem,
        enquanto valores altos indicam risco financeiro elevado.
        '''
        # Define a categoria de agrupamento como "Solvência"
        self.agrupador = 'Solvência'
        # Define a fórmula do Dívida Líquida / EBITDA
        self.formula = 'Dívida Líquida / EBITDA = (Dívida Total - Caixa e Equivalentes) / EBITDA'

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

    # Avalia o valor Dívida Líquida / EBITDA e retorna um objeto ResultadoIND
    def avaliar(self, div_ebitda):
        # Tenta processar o valor Dívida Líquida / EBITDA
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(div_ebitda, (int, float)) and not (isinstance(div_ebitda, str) and div_ebitda.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de Dívida Líquida / EBITDA deve ser numérico.")
            # Converte o Dívida Líquida / EBITDA para float para garantir que é numérico
            div_ebitda = float(div_ebitda)
            # Verifica se Dívida Líquida / EBITDA é negativo, indicando excesso de caixa
            if div_ebitda < 0:
                # Retorna ResultadoIND para Dívida Líquida / EBITDA negativo
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='Dívida Líquida / EBITDA < 0',
                    descricao='Um valor negativo indica que a empresa possui mais caixa e equivalentes do que dívidas, sugerindo uma posição financeira sólida com baixa alavancagem. Isso pode ocorrer em empresas com alta geração de caixa ou reservas elevadas, permitindo investimentos ou distribuições aos acionistas.',
                    riscos='Risco de ineficiência no uso de capital, como excesso de caixa ocioso que poderia ser investido ou distribuído. Pode haver oportunidades perdidas de crescimento ou baixa rentabilidade sobre ativos.',
                    referencia='Avalie evaluate_roic para retorno sobre capital investido, evaluate_cash_flow para geração de caixa e evaluate_dividend_yield para distribuição de lucros.',
                    recomendacao='Considere investir se a empresa demonstrar eficiência no uso de caixa. Verifique planos de investimento ou retorno aos acionistas para maximizar valor.'
                )
            # Verifica se Dívida Líquida / EBITDA está entre 0 e 1, indicando baixa alavancagem
            elif 0 <= div_ebitda <= 1:
                # Retorna ResultadoIND para baixa alavancagem
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= Dívida Líquida / EBITDA <= 1',
                    descricao='A dívida líquida é baixa em relação ao EBITDA, indicando que a empresa pode pagar suas dívidas com menos de um ano de lucro operacional. Isso sugere solvência forte e baixa dependência de financiamento externo, comum em empresas maduras com fluxo de caixa estável.',
                    riscos='Risco de subalavancagem, onde a empresa perde oportunidades de crescimento via dívida barata. Pode haver conservadorismo excessivo ou setores com baixa necessidade de capital.',
                    referencia='Analise evaluate_roe para rentabilidade sobre patrimônio, evaluate_ebitda_margin para margens operacionais e evaluate_capex para investimentos em capital.',
                    recomendacao='Considere investir para estabilidade financeira. Avalie se a baixa dívida permite expansão ou aquisições sem diluição acionária.'
                )
            # Verifica se Dívida Líquida / EBITDA está entre 1 e 2, indicando alavancagem moderada
            elif 1 < div_ebitda <= 2:
                # Retorna ResultadoIND para alavancagem moderada
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='1 < Dívida Líquida / EBITDA <= 2',
                    descricao='A dívida líquida é moderada em relação ao EBITDA, sugerindo que a empresa pode quitar suas dívidas em até dois anos de lucro operacional. Essa faixa é equilibrada, permitindo alavancagem para crescimento sem risco excessivo, comum em empresas em expansão controlada.',
                    riscos='Risco de aumento nos custos de juros se as taxas subirem ou EBITDA cair. Pode haver dependência de financiamento para operações ou investimentos.',
                    referencia='Compare com evaluate_debt_to_equity para estrutura de capital, evaluate_interest_coverage para cobertura de juros e evaluate_current_ratio para liquidez.',
                    recomendacao='Avalie o histórico de EBITDA e planos de redução de dívida. Pode ser uma boa opção para investidores que buscam equilíbrio entre risco e retorno.'
                )
            # Verifica se Dívida Líquida / EBITDA está entre 2 e 3, indicando alavancagem elevada
            elif 2 < div_ebitda <= 3:
                # Retorna ResultadoIND para alavancagem elevada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='2 < Dívida Líquida / EBITDA <= 3',
                    descricao='A dívida líquida é elevada em relação ao EBITDA, indicando que a empresa precisaria de até três anos de lucro operacional para quitar suas dívidas. Essa faixa sugere alavancagem moderada-alta, comum em setores capital-intensivos como infraestrutura ou manufatura.',
                    riscos='Risco de pressão financeira se o EBITDA declinar devido a recessões ou custos crescentes. Pode haver limitações em novos investimentos ou distribuições de lucros.',
                    referencia='Verifique evaluate_peg_ratio para crescimento ajustado, evaluate_evebitda para valuation e evaluate_beta para volatilidade.',
                    recomendacao='Considere investir com cautela, monitorando a geração de caixa e redução de dívida. Priorize empresas com EBITDA estável.'
                )
            # Verifica se Dívida Líquida / EBITDA está entre 3 e 4, indicando risco financeiro alto
            elif 3 < div_ebitda <= 4:
                # Retorna ResultadoIND para risco financeiro alto
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='3 < Dívida Líquida / EBITDA <= 4',
                    descricao='A dívida líquida é alta em relação ao EBITDA, sugerindo que a empresa precisaria de até quatro anos de lucro operacional para pagar suas dívidas. Essa faixa indica risco financeiro significativo, comum em empresas em recuperação ou com investimentos pesados.',
                    riscos='Risco de default em dívidas se houver desaceleração econômica ou aumento de juros. Pode haver restrições de credores ou diluição acionária para levantar capital.',
                    referencia='Combine com evaluate_psr para receita, evaluate_margem_liquida para eficiência e evaluate_cash_conversion_cycle para ciclo de caixa.',
                    recomendacao='Evite investir a menos que haja planos claros de desalavancagem. Monitore relatórios trimestrais para sinais de melhoria.'
                )
            # Verifica se Dívida Líquida / EBITDA excede 4, indicando risco financeiro crítico
            elif div_ebitda > 4:
                # Retorna ResultadoIND para risco financeiro crítico
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='Dívida Líquida / EBITDA > 4',
                    descricao='A dívida líquida é extremamente alta em relação ao EBITDA, indicando que a empresa precisaria de mais de quatro anos de lucro operacional para quitar suas dívidas. Essa faixa sugere alavancagem excessiva e vulnerabilidade financeira, comum em empresas em crise ou com aquisições agressivas.',
                    riscos='Alto risco de insolvência, reestruturação de dívida ou falência. Pode haver custos elevados de juros, redução de investimentos e impacto negativo na cotação das ações.',
                    referencia='Analise evaluate_dividend_yield para rendimentos, evaluate_beta para volatilidade e evaluate_p_l para lucros.',
                    recomendacao='Não invista devido ao risco elevado. Considere apenas se houver turnaround comprovado ou suporte externo (ex.: injeção de capital).'
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
                Ocorreu um erro ao processar o Dívida Líquida / EBITDA: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A',
            recomendacao='N/A'
        )




# Define a classe LPAEvaluator para avaliar o indicador LPA (Lucro por Ação)
class LPAEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do LPA
    def __init__(self):
        # Define string multilinha explicando o índice LPA
        self.definicao = '''
        O Lucro por Ação (LPA) mede a rentabilidade da empresa por ação, calculado
        como (Lucro Líquido / Número de Ações em Circulação). É um indicador chave de desempenho
        que mostra quanto lucro a empresa gera para cada ação. Um LPA alto sugere alta rentabilidade,
        enquanto valores negativos indicam prejuízos.
        '''
        # Define a categoria de agrupamento como "Rentabilidade"
        self.agrupador = 'Rentabilidade'
        # Define a fórmula do LPA
        self.formula = 'LPA = Lucro Líquido / Número de Ações em Circulação'

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

    # Avalia o valor LPA e retorna um objeto ResultadoIND
    def avaliar(self, lpa):
        # Tenta processar o valor LPA
        try:
            # Verifica se a entrada é numérica (int ou float) ou uma string que pode ser convertida
            if not isinstance(lpa, (int, float)) and not (isinstance(lpa, str) and lpa.replace('.', '', 1).isdigit()):
                raise ValueError("O valor de LPA deve ser numérico.")
            # Converte o LPA para float para garantir que é numérico
            lpa = float(lpa)
            # Verifica se LPA é negativo, indicando prejuízo
            if lpa < 0:
                # Retorna ResultadoIND para LPA negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='LPA < 0',
                    descricao='Um LPA negativo indica que a empresa registrou prejuízo no período, o que pode sinalizar problemas operacionais, altos custos ou perdas extraordinárias. Isso sugere baixa rentabilidade e potencial instabilidade financeira.',
                    riscos='Risco de diluição acionária, redução de dividendos ou falência se os prejuízos persistirem. Pode haver endividamento crescente ou ineficiência operacional.',
                    referencia='Avalie evaluate_roa para rentabilidade dos ativos, evaluate_roe para retorno sobre patrimônio e evaluate_ebitda para lucro operacional.',
                    recomendacao='Evite investir até que a empresa demonstre recuperação e lucros positivos. Priorize análise de fluxo de caixa e redução de custos.'
                )
            # Verifica se LPA está entre 0 e 1, indicando baixa rentabilidade
            elif 0 <= lpa <= 1:
                # Retorna ResultadoIND para baixa rentabilidade
                return self.gerar_resultado(
                    classificacao='Baixo',
                    faixa='0 <= LPA <= 1',
                    descricao='O LPA está baixo, sugerindo rentabilidade limitada por ação. Isso pode ocorrer em empresas em fase inicial, com altos investimentos ou em setores de baixa margem.',
                    riscos='Risco de estagnação no crescimento ou baixa capacidade de gerar valor para acionistas. Pode haver concorrência intensa ou custos operacionais elevados.',
                    referencia='Analise evaluate_margem_liquida para eficiência e evaluate_crescimento_lucros para tendências futuras.',
                    recomendacao='Considere investir se houver potencial de crescimento, mas verifique margens e estratégias de expansão.'
                )
            # Verifica se LPA está entre 1 e 3, indicando rentabilidade moderada
            elif 1 < lpa <= 3:
                # Retorna ResultadoIND para rentabilidade moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1 < LPA <= 3',
                    descricao='O LPA está em uma faixa moderada, indicando rentabilidade razoável por ação. Essa faixa é comum em empresas estáveis com lucros consistentes, mas sem crescimento excepcional.',
                    riscos='Risco de volatilidade em lucros devido a ciclos econômicos ou mudanças setoriais. Pode haver dependência de fatores externos como preços de commodities.',
                    referencia='Compare com evaluate_p_l para valuation e evaluate_dividend_yield para rendimentos.',
                    recomendacao='Avalie o histórico de lucros e dividendos antes de investir. Pode ser uma boa opção para investidores conservadores.'
                )
            # Verifica se LPA está entre 3 e 5, indicando boa rentabilidade
            elif 3 < lpa <= 5:
                # Retorna ResultadoIND para boa rentabilidade
                return self.gerar_resultado(
                    classificacao='Bom',
                    faixa='3 < LPA <= 5',
                    descricao='O LPA está em uma faixa boa, sugerindo alta rentabilidade por ação. Isso reflete eficiência operacional e geração de valor para acionistas, comum em empresas maduras com margens elevadas.',
                    riscos='Risco de saturação no mercado ou aumento de competição que reduza margens. Pode haver dependência de produtos chave ou mercados específicos.',
                    referencia='Verifique evaluate_peg_ratio para crescimento e evaluate_roic para retorno sobre capital investido.',
                    recomendacao='Considere investir para renda ou crescimento, mas monitore a sustentabilidade dos lucros.'
                )
            # Verifica se LPA excede 5, indicando rentabilidade excepcional
            elif lpa > 5:
                # Retorna ResultadoIND para rentabilidade excepcional
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='LPA > 5',
                    descricao='O LPA é extremamente alto, indicando rentabilidade excepcional por ação. Essa faixa é típica de empresas com alto crescimento, eficiência superior ou posições de mercado dominantes.',
                    riscos='Risco de sobrevalorização ou expectativas irreais de manutenção dos lucros. Pode haver volatilidade se houver mudanças regulatórias ou econômicas.',
                    referencia='Combine com evaluate_psr para receita e evaluate_beta para volatilidade.',
                    recomendacao='Invista se os fundamentos suportarem o crescimento contínuo, mas diversifique para mitigar riscos.'
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
                Ocorreu um erro ao processar o LPA: {mensagem}.
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
                    classificacao='Baixo',
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
                    classificacao='Baixo',
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
                    classificacao='Crítico',
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