# Função auxiliar assumida
def is_null_zero_or_spaces(value):
    """
    Verifica se o valor é nulo, zero ou contém apenas espaços.
    """
    return value is None or value == "0" or (isinstance(value, str) and value.strip() == "")


# Versão 1: Seu código
def tratamento_indicador_seu(indicador, percentual=False, stock=None, metricasts=None):
    """
    Trata o valor de um indicador, convertendo para float e lidando com casos inválidos.

    Parâmetros:
    - indicador: valor a ser tratado (str, float, etc.)
    - percentual: se True, converte valores percentuais (ex: '25%') para decimais (0.25)
    - stock: Contexto para log de erro (opcional)
    - metricasts: Contexto para log de erro (opcional)

    Retorna:
    - float: valor tratado
    """
    try:
        if indicador in ["-", "--", "--%"] or indicador is None or is_null_zero_or_spaces(indicador) or indicador == "":
            return 0.0
        if percentual and isinstance(indicador, str) and "%" in indicador:
            return float(indicador.strip('%')) / 100
        return float(indicador)
    except Exception as e:
        print(f"Erro inesperado no tratamento: {e}, métrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0


# Versão 2: Meu código original (corrigido)
def tratamento_indicador_meu(indicador, tipo_tratamento='float', stock=None, metricasts=None):
    """
    Trata indicadores com base no tipo especificado, convertendo para float ou percentual.

    Args:
        indicador: Valor do indicador a ser tratado
        tipo_tratamento: 'percent' para tratar como percentual, 'float' para float direto
        stock: Contexto para log de erro (opcional)
        metricasts: Contexto para log de erro (opcional)

    Returns:
        float: Valor tratado do indicador
    """
    try:
        if indicador in ["-", "--", "--%"] or indicador is None or is_null_zero_or_spaces(indicador) or indicador == "":
            return 0.0
        if tipo_tratamento == 'percent' and isinstance(indicador, str) and "%" in indicador:
            return float(indicador.strip('%')) / 100
        return float(indicador)
    except Exception as e:
        print(
            f"Erro inesperado no tratamento ({tipo_tratamento}): {e}, metrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0
    finally:
        pass


# Versão 3: Versão combinada
def tratamento_indicador_combinado(indicador, tipo_tratamento='float', stock=None, metricasts=None):
    """
    Trata o valor de um indicador, convertendo para float ou percentual.

    Parâmetros:
    - indicador: Valor a ser tratado (str, float, etc.)
    - tipo_tratamento: 'float' para conversão direta, 'percent' para percentuais
    - stock: Contexto para log de erro (opcional)
    - metricasts: Contexto para log de erro (opcional)

    Retorna:
    - float: Valor tratado
    """
    try:
        if indicador in ["-", "--", "--%"] or indicador is None or is_null_zero_or_spaces(indicador) or indicador == "":
            return 0.0
        if tipo_tratamento == 'percent' and isinstance(indicador, str) and "%" in indicador:
            return float(indicador.strip('%')) / 100
        return float(indicador)
    except Exception as e:
        print(
            f"Erro inesperado no tratamento ({tipo_tratamento}): {e}, metrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0


# Chamadas individuais para o valor "14%"
if __name__ == '__main__':
    print("=== Testando tratamento_indicador_seu ===")
    resultado_seu = tratamento_indicador_seu("14%", percentual=True)
    print(f"Input: 14%, Percentual: True -> Resultado: {resultado_seu}")

    print("\n=== Testando tratamento_indicador_meu ===")
    resultado_meu = tratamento_indicador_meu("14%", tipo_tratamento='percent')
    print(f"Input: 14%, Tipo: percent -> Resultado: {resultado_meu}")

    print("\n=== Testando tratamento_indicador_combinado ===")
    resultado_combinado = tratamento_indicador_combinado("14%", tipo_tratamento='percent')
    print(f"Input: 14%, Tipo: percent -> Resultado: {resultado_combinado}")