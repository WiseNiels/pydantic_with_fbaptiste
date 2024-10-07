from pydantic import BaseModel
from pydantic import ValidationError

from datetime import datetime as dt

class Circle(BaseModel):
    center: tuple[int, int] = (0,0) #this field now is optional
    radius: int
    


print(Circle.model_fields)

c= Circle(radius=5)

print(c)


# Quando python vee essa funcao, no momento de compilacao ele calcula/computa a lista e guarda no mesmo endereco de memoria, e toda vez que a funcao e' executado python usa  a mesma lista e faz a opercao.

# Code Smell
# Explique o porque a variavel horas_2 tem 2 elementos e o primeiro e' o elemento da variavel horas
def my_list(lista: list = []):
    lista.append(dt.now())
    return lista


horas = my_list()
print(horas)

horas_3 = my_list([])
print(horas_3)

horas_2 = my_list()
print(horas_2)



