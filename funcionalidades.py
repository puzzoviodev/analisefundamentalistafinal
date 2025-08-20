import inspect
import analisefundamentalista  # substitua pelo nome do seu arquivo sem ".py"
import analiseativos

funcoes = [name for name, obj in inspect.getmembers(analiseativos, inspect.isfunction)]
print("Funções disponíveis:", funcoes)




classes = [name for name, obj in inspect.getmembers(analiseativos, inspect.isclass)]
print("Classes disponíveis:", classes)

import inspect
import analiseativos  # Certifique-se de que esse módulo está acessível

# Obtém todas as classes definidas no módulo
classes = [name for name, obj in inspect.getmembers(analiseativos, inspect.isclass)]

# Imprime cada classe separadamente
print("Classes disponíveis:")
for classe in classes:
    print(f" {classe}")


