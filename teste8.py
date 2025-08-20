# Função auxiliar assumida
def is_null_zero_or_spaces(value):
    """
    Verifica se o valor é nulo, zero ou contém apenas espaços.
    """
    return value is None or value == "0" or (isinstance(value, str) and value.strip() == "")


# Versão 1: Seu código (corrigido para não dividir percentuais por 100)
def tratamento_indicador_seu(indicador, stock=None, metricasts=None):
    """
    Trata o valor de um indicador, detectando automaticamente se é percentual ou float.

    Parâmetros:
    - indicador: valor a ser tratado (str, float, int, etc.)
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
            # Remove R$ e espaços
            cleaned = indicador.replace("R$", "").replace(" ", "").strip()
            # Se contém vírgula, remove pontos como separadores de milhar e substitui vírgula por ponto
            if "," in cleaned:
                cleaned = cleaned.replace(".", "").replace(",", ".")
            # Remove % sem dividir por 100
            if "%" in cleaned:
                return float(cleaned.strip('%'))
            return float(cleaned)
        return float(indicador)
    except Exception as e:
        print(f"Erro inesperado no tratamento: {e}, métrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0


# Versão 2: Meu código original (corrigido para não dividir percentuais por 100)
def tratamento_indicador_meu(indicador, stock=None, metricasts=None):
    """
    Trata indicadores, detectando automaticamente se é percentual ou float.

    Args:
        indicador: Valor do indicador a ser tratado
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
            # Remove R$ e espaços
            cleaned = indicador.replace("R$", "").replace(" ", "").strip()
            # Se contém vírgula, remove pontos como separadores de milhar e substitui vírgula por ponto
            if "," in cleaned:
                cleaned = cleaned.replace(".", "").replace(",", ".")
            # Remove % sem dividir por 100
            if "%" in cleaned:
                return float(cleaned.strip('%'))
            return float(cleaned)
        return float(indicador)
    except Exception as e:
        print(f"Erro inesperado no tratamento: {e}, metrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0
    finally:
        pass


# Versão 3: Versão combinada (corrigida para não dividir percentuais por 100)
def tratamento_indicador_combinado(indicador, stock=None, metricasts=None):
    """
    Trata o valor de um indicador, detectando automaticamente se é percentual ou float.

    Parâmetros:
    - indicador: Valor a ser tratado (str, float, int, etc.)
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
            # Remove R$ e espaços
            cleaned = indicador.replace("R$", "").replace(" ", "").strip()
            # Se contém vírgula, remove pontos como separadores de milhar e substitui vírgula por ponto
            if "," in cleaned:
                cleaned = cleaned.replace(".", "").replace(",", ".")
            # Remove % sem dividir por 100
            if "%" in cleaned:
                return float(cleaned.strip('%'))
            return float(cleaned)
        return float(indicador)
    except Exception as e:
        print(f"Erro inesperado no tratamento: {e}, metrica: {metricasts}, indicador: {indicador}, stock: {stock}")
        return 0.0


# Chamadas individuais para os valores fornecidos
if __name__ == '__main__':
    print("=== Testando tratamento_indicador_seu ===")
    print(f"Input: R$ 12,10 -> Resultado: {tratamento_indicador_seu('R$ 12,10')}")
    print(f"Input: -55,04% -> Resultado: {tratamento_indicador_seu('-55,04%')}")
    print(f"Input: -2,03 -> Resultado: {tratamento_indicador_seu('-2,03')}")
    print(f"Input: 1,17 -> Resultado: {tratamento_indicador_seu('1,17')}")
    print(f"Input: -% -> Resultado: {tratamento_indicador_seu('-%')}")
    print(f"Input: -R$ 63.526.000,00 -> Resultado: {tratamento_indicador_seu('-R$ 63.526.000,00')}")
    print(f"Input: 1,7 -> Resultado: {tratamento_indicador_seu('1,7')}")
    print(f"Input: 1.7 -> Resultado: {tratamento_indicador_seu('1.7')}")

    print("\n=== Testando tratamento_indicador_meu ===")
    print(f"Input: R$ 12,10 -> Resultado: {tratamento_indicador_meu('R$ 12,10')}")
    print(f"Input: -55,04% -> Resultado: {tratamento_indicador_meu('-55,04%')}")
    print(f"Input: -2,03 -> Resultado: {tratamento_indicador_meu('-2,03')}")
    print(f"Input: 1,17 -> Resultado: {tratamento_indicador_meu('1,17')}")
    print(f"Input: -% -> Resultado: {tratamento_indicador_meu('-%')}")
    print(f"Input: -R$ 63.526.000,00 -> Resultado: {tratamento_indicador_meu('-R$ 63.526.000,00')}")
    print(f"Input: 1,7 -> Resultado: {tratamento_indicador_meu('1,7')}")
    print(f"Input: 1.7 -> Resultado: {tratamento_indicador_meu('1.7')}")

    print("\n=== Testando tratamento_indicador_combinado ===")
    print(f"Input: R$ 12,10 -> Resultado: {tratamento_indicador_combinado('R$ 12,10')}")
    print(f"Input: -55,04% -> Resultado: {tratamento_indicador_combinado('-55,04%')}")
    print(f"Input: -2,03 -> Resultado: {tratamento_indicador_combinado('-2,03')}")
    print(f"Input: 1,17 -> Resultado: {tratamento_indicador_combinado('1,17')}")
    print(f"Input: -% -> Resultado: {tratamento_indicador_combinado('-%')}")
    print(f"Input: -R$ 63.526.000,00 -> Resultado: {tratamento_indicador_combinado('-R$ 63.526.000,00')}")
    print(f"Input: 1,7 -> Resultado: {tratamento_indicador_combinado('1,7')}")
    print(f"Input: 1.7 -> Resultado: {tratamento_indicador_combinado('1.7')}")