import unittest


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


# Versão 2: Meu código original
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
    indicador2 = indicador
    try:
        if indicador2 in ["-", "--", "--%"] or indicador2 is None or is_null_zero_or_spaces(
                indicador2) or indicador2 == "":
            return 0.0
        if tipo_tratamento == 'percent':
            indicador2 = float(indicador2.strip('%')) / 100
        else:
            indicador2 = float(indicador2)
        return indicador2
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


# Testes unitários
class TestTratamentoIndicador(unittest.TestCase):
    def test_seu_codigo(self):
        """Testes para a versão do código do usuário"""
        # Casos inválidos
        self.assertEqual(tratamento_indicador_seu("-"), 0.0, "Falha ao tratar '-'")
        self.assertEqual(tratamento_indicador_seu("--"), 0.0, "Falha ao tratar '--'")
        self.assertEqual(tratamento_indicador_seu("--%"), 0.0, "Falha ao tratar '--%'")
        self.assertEqual(tratamento_indicador_seu(None), 0.0, "Falha ao tratar None")
        self.assertEqual(tratamento_indicador_seu(""), 0.0, "Falha ao tratar string vazia")
        self.assertEqual(tratamento_indicador_seu(" "), 0.0, "Falha ao tratar espaço")
        self.assertEqual(tratamento_indicador_seu("0"), 0.0, "Falha ao tratar '0'")

        # Casos numéricos
        self.assertEqual(tratamento_indicador_seu("123"), 123.0, "Falha ao converter string numérica")
        self.assertEqual(tratamento_indicador_seu(123), 123.0, "Falha ao converter número")
        self.assertEqual(tratamento_indicador_seu("123.45"), 123.45, "Falha ao converter decimal")

        # Casos percentuais
        self.assertEqual(tratamento_indicador_seu("25%", percentual=True), 0.25, "Falha ao tratar percentual")
        self.assertEqual(tratamento_indicador_seu("-25%", percentual=True), -0.25,
                         "Falha ao tratar percentual negativo")
        self.assertEqual(tratamento_indicador_seu("25%", percentual=False), 0.0,
                         "Falha ao tratar percentual sem modo ativado")

        # Casos de erro
        self.assertEqual(tratamento_indicador_seu("abc", stock="TESTE", metricasts="METRICA"), 0.0,
                         "Falha ao tratar string inválida")
        self.assertEqual(tratamento_indicador_seu("abc%", percentual=True), 0.0, "Falha ao tratar percentual inválido")

    def test_meu_codigo(self):
        """Testes para a versão original do Grok"""
        # Casos inválidos
        self.assertEqual(tratamento_indicador_meu("-"), 0.0, "Falha ao tratar '-'")
        self.assertEqual(tratamento_indicador_meu("--"), 0.0, "Falha ao tratar '--'")
        self.assertEqual(tratamento_indicador_meu("--%"), 0.0, "Falha ao tratar '--%'")
        self.assertEqual(tratamento_indicador_meu(None), 0.0, "Falha ao tratar None")
        self.assertEqual(tratamento_indicador_meu(""), 0.0, "Falha ao tratar string vazia")
        self.assertEqual(tratamento_indicador_meu(" "), 0.0, "Falha ao tratar espaço")
        self.assertEqual(tratamento_indicador_meu("0"), 0.0, "Falha ao tratar '0'")

        # Casos numéricos
        self.assertEqual(tratamento_indicador_meu("123"), 123.0, "Falha ao converter string numérica")
        self.assertEqual(tratamento_indicador_meu(123), 123.0, "Falha ao converter número")
        self.assertEqual(tratamento_indicador_meu("123.45"), 123.45, "Falha ao converter decimal")

        # Casos percentuais
        self.assertEqual(tratamento_indicador_meu("25%", tipo_tratamento='percent'), 0.25, "Falha ao tratar percentual")
        self.assertEqual(tratamento_indicador_meu("-25%", tipo_tratamento='percent'), -0.25,
                         "Falha ao tratar percentual negativo")
        self.assertEqual(tratamento_indicador_meu(123, tipo_tratamento='percent'), 0.0,
                         "Falha ao tratar número no modo percentual")

        # Casos de erro
        self.assertEqual(tratamento_indicador_meu("abc", stock="TESTE", metricasts="METRICA"), 0.0,
                         "Falha ao tratar string inválida")
        self.assertEqual(tratamento_indicador_meu("abc%", tipo_tratamento='percent'), 0.0,
                         "Falha ao tratar percentual inválido")

    def test_combinado_codigo(self):
        """Testes para a versão combinada"""
        # Casos inválidos
        self.assertEqual(tratamento_indicador_combinado("-"), 0.0, "Falha ao tratar '-'")
        self.assertEqual(tratamento_indicador_combinado("--"), 0.0, "Falha ao tratar '--'")
        self.assertEqual(tratamento_indicador_combinado("--%"), 0.0, "Falha ao tratar '--%'")
        self.assertEqual(tratamento_indicador_combinado(None), 0.0, "Falha ao tratar None")
        self.assertEqual(tratamento_indicador_combinado(""), 0.0, "Falha ao tratar string vazia")
        self.assertEqual(tratamento_indicador_combinado(" "), 0.0, "Falha ao tratar espaço")
        self.assertEqual(tratamento_indicador_combinado("0"), 0.0, "Falha ao tratar '0'")

        # Casos numéricos
        self.assertEqual(tratamento_indicador_combinado("123"), 123.0, "Falha ao converter string numérica")
        self.assertEqual(tratamento_indicador_combinado(123), 123.0, "Falha ao converter número")
        self.assertEqual(tratamento_indicador_combinado("123.45"), 123.45, "Falha ao converter decimal")

        # Casos percentuais
        self.assertEqual(tratamento_indicador_combinado("25%", tipo_tratamento='percent'), 0.25,
                         "Falha ao tratar percentual")
        self.assertEqual(tratamento_indicador_combinado("-25%", tipo_tratamento='percent'), -0.25,
                         "Falha ao tratar percentual negativo")
        self.assertEqual(tratamento_indicador_combinado("25%", tipo_tratamento='float'), 0.0,
                         "Falha ao tratar percentual sem modo ativado")
        self.assertEqual(tratamento_indicador_combinado(123, tipo_tratamento='percent'), 123.0,
                         "Falha ao tratar número no modo percentual")

        # Casos de erro
        self.assertEqual(tratamento_indicador_combinado("abc", stock="TESTE", metricasts="METRICA"), 0.0,
                         "Falha ao tratar string inválida")
        self.assertEqual(tratamento_indicador_combinado("abc%", tipo_tratamento='percent'), 0.0,
                         "Falha ao tratar percentual inválido")


if __name__ == '__main__':
    unittest.main()