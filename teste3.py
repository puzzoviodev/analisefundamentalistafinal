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


# Exemplos de chamadas individuais
if __name__ == '__main__':
    # Inputs para teste
    inputs = [
        ("-", False, None, None),  # Caso inválido
        ("--", False, None, None),  # Caso inválido
        ("--%", False, None, None),  # Caso inválido
        (None, False, None, None),  # Caso inválido
        ("", False, None, None),  # Caso inválido
        (" ", False, None, None),  # Caso inválido
        ("0", False, None, None),  # Caso inválido
        ("123", False, None, None),  # Numérico (string)
        (123, False, None, None),  # Numérico (int)
        ("123.45", False, None, None),  # Numérico (string decimal)
        ("25%", True, None, None),  # Percentual
        ("-25%", True, None, None),  # Percentual negativo
        ("abc", False, "TESTE", "METRICA"),  # Erro (string inválida)
        ("abc%", True, None, None),  # Erro (percentual inválido)
    ]

    # Funções a serem testadas
    funcoes = [
        ("tratamento_indicador_seu", tratamento_indicador_seu),
        ("tratamento_indicador_meu", tratamento_indicador_meu),
        ("tratamento_indicador_combinado", tratamento_indicador_combinado)
    ]

    # Executa cada função com cada input
    for nome_funcao, funcao in funcoes:
        print(f"\n=== Testando {nome_funcao} ===")
        for indicador, percentual, stock, metricasts in inputs:
            # Ajusta o parâmetro para tratamento_indicador_meu e combinado
            tipo_tratamento = 'percent' if percentual else 'float'
            params = {'percentual': percentual} if nome_funcao == "tratamento_indicador_seu" else {
                'tipo_tratamento': tipo_tratamento}
            resultado = funcao(indicador, stock=stock, metricasts=metricasts, **params)
            print(
                f"Input: {indicador}, Percentual/Tipo: {params}, Stock: {stock}, Metricasts: {metricasts} -> Resultado: {resultado}")