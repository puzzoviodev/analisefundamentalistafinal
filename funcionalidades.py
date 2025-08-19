import inspect
import analisefundamentalista  # substitua pelo nome do seu arquivo sem ".py"
import analiseativos

funcoes = [name for name, obj in inspect.getmembers(analiseativos, inspect.isfunction)]
print("Funções disponíveis:", funcoes)




classes = [name for name, obj in inspect.getmembers(analiseativos, inspect.isclass)]
print("Classes disponíveis:", classes)

