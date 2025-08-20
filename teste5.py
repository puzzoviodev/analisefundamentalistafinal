# Função auxiliar assumida
def is_null_zero_or_spaces(value):
    """
    Verifica se o valor é nulo, zero ou contém apenas espaços.
    """
    return value is None or value == "0" or (isinstance(value, str) and value.strip() == "")


# Versão 1: Seu código (ajustado para vírgula e R$)
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
        if indicador in ["-", "--", "--%", "-%"] or indicador is None or is_null_zero_or_spaces(
                indicador) or indicador == "":
            return 0.0
        if isinstance(indicador, str):
            # Remove R$ e substitui vírgula por ponto
            indicador = indicador.replace("R$", "").replace(".", "").replace(",", ".").strip()
            if percentual and "%" in indicador:
                return float(indicador.strip('%')) / 100
        return float(indicador)
    except Exception as e:
        print(f"Erro inesperado no tratamento: {e}, métrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0


# Versão 2: Meu código original (corrigido e ajustado para vírgula e R$)
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
        if indicador in ["-", "--", "--%", "-%"] or indicador is None or is_null_zero_or_spaces(
                indicador) or indicador == "":
            return 0.0
        if isinstance(indicador, str):
            # Remove R$ e substitui vírgula por ponto
            indicador = indicador.replace("R$", "").replace(".", "").replace(",", ".").strip()
            if tipo_tratamento == 'percent' and "%" in indicador:
                return float(indicador.strip('%')) / 100
        return float(indicador)
    except Exception as e:
        print(
            f"Erro inesperado no tratamento ({tipo_tratamento}): {e}, metrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0
    finally:
        pass


# Versão 3: Versão combinada (ajustada para vírgula e R$)
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
        if indicador in ["-", "--", "--%", "-%"] or indicador is None or is_null_zero_or_spaces(
                indicador) or indicador == "":
            return 0.0
        if isinstance(indicador, str):
            # Remove R$ e substitui vírgula por ponto
            indicador = indicador.replace("R$", "").replace(".", "").replace(",", ".").strip()
            if tipo_tratamento == 'percent' and "%" in indicador:
                return float(indicador.strip('%')) / 100
        return float(indicador)
    except Exception as e:
        print(
            f"Erro inesperado no tratamento ({tipo_tratamento}): {e}, metrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0


# Chamadas individuais para os valores fornecidos
if __name__ == '__main__':
    print("=== Testando tratamento_indicador_seu ===")
    print(f"Input: R$ 12,10, Percentual: False -> Resultado: {tratamento_indicador_seu('R$ 12,10', percentual=False)}")
    print(f"Input: -55,04%, Percentual: True -> Resultado: {tratamento_indicador_seu('-55,04%', percentual=True)}")
    print(f"Input: -2,03, Percentual: False -> Resultado: {tratamento_indicador_seu('-2,03', percentual=False)}")
    print(f"Input: 1,17, Percentual: False -> Resultado: {tratamento_indicador_seu('1,17', percentual=False)}")
    print(f"Input: -%, Percentual: True -> Resultado: {tratamento_indicador_seu('-%', percentual=True)}")
    print(
        f"Input: -R$ 63.526.000,00, Percentual: False -> Resultado: {tratamento_indicador_seu('-R$ 63.526.000,00', percentual=False)}")

    print("\n=== Testando tratamento_indicador_meu ===")
    print(f"Input: R$ 12,10, Tipo: float -> Resultado: {tratamento_indicador_meu('R$ 12,10', tipo_tratamento='float')}")
    print(
        f"Input: -55,04%, Tipo: percent -> Resultado: {tratamento_indicador_meu('-55,04%', tipo_tratamento='percent')}")
    print(f"Input: -2,03, Tipo: float -> Resultado: {tratamento_indicador_meu('-2,03', tipo_tratamento='float')}")
    print(f"Input: 1,17, Tipo: float -> Resultado: {tratamento_indicador_meu('1,17', tipo_tratamento='float')}")
    print(f"Input: -%, Tipo: percent -> Resultado: {tratamento_indicador_meu('-%', tipo_tratamento='percent')}")
    print(
        f"Input: -R$ 63.526.000,00, Tipo: float -> Resultado: {tratamento_indicador_meu('-R$ 63.526.000,00', tipo_tratamento='float')}")

    print("\n=== Testando tratamento_indicador_combinado ===")
    print(
        f"Input: R$ 12,10, Tipo: float -> Resultado: {tratamento_indicador_combinado('R$ 12,10', tipo_tratamento='float')}")
    print(
        f"Input: -55,04%, Tipo: percent -> Resultado: {tratamento_indicador_combinado('-55,04%', tipo_tratamento='percent')}")
    print(f"Input: -2,03, Tipo: float -> Resultado: {tratamento_indicador_combinado('-2,03', tipo_tratamento='float')}")
    print(f"Input: 1,17, Tipo: float -> Resultado: {tratamento_indicador_combinado('1,17', tipo_tratamento='float')}")
    print(f"Input: -%, Tipo: percent -> Resultado: {tratamento_indicador_combinado('-%', tipo_tratamento='percent')}")
    print(
        f"Input: -R$ 63.526.000,00, Tipo: float -> Resultado: {tratamento_indicador_combinado('-R$ 63.526.000,00', tipo_tratamento='float')}")