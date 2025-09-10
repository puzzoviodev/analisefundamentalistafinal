import ast
import json

def extrair_classes_e_parametros(arquivo_codigo):
    """
    Analisa um arquivo Python usando AST para extrair classes, métodos e seus parâmetros.
    Retorna uma lista de dicionários com as informações.
    """
    with open('analiseativos.py', 'r', encoding='utf-8') as f:
        codigo_fonte = f.read()

    # Parsear o código fonte em uma AST
    arvore = ast.parse(codigo_fonte)

    resultados = []

    # Iterar sobre os nós da AST para encontrar definições de classes
    for no in ast.walk(arvore):
        if isinstance(no, ast.ClassDef):
            classe_info = {
                'classe': no.name,
                'metodos': []
            }

            # Iterar sobre os métodos da classe
            for corpo_no in no.body:
                if isinstance(corpo_no, ast.FunctionDef):
                    metodo_info = {
                        'metodo': corpo_no.name,
                        'parametros': []
                    }

                    # Extrair parâmetros do método
                    for arg in corpo_no.args.args:
                        param = arg.arg
                        # Verificar se há anotação de tipo (ex.: tipo: str)
                        tipo = ast.unparse(arg.annotation) if arg.annotation else None
                        # Verificar valor padrão (default)
                        default = None
                        if corpo_no.args.defaults:
                            idx = len(corpo_no.args.args) - len(corpo_no.args.defaults)
                            if arg == corpo_no.args.args[-idx:]:
                                default = ast.unparse(corpo_no.args.defaults.pop(0)) if corpo_no.args.defaults else None
                        metodo_info['parametros'].append({
                            'nome': param,
                            'tipo': tipo,
                            'default': default
                        })

                    classe_info['metodos'].append(metodo_info)

            resultados.append(classe_info)

    return resultados

# Exemplo de uso: substitua pelo caminho do seu arquivo
arquivo = 'D:\ccd.py"'  # Caminho para seu arquivo com 7.000 linhas
info_extraida = extrair_classes_e_parametros(arquivo)

# Exibir como JSON para facilitar a visualização
print(json.dumps(info_extraida, indent=4, ensure_ascii=False))