from pydantic import BaseModel, PositiveInt, ValidationError, conlist


class Esfera(BaseModel):
    center: conlist(int, min_length=2, max_length=3) = (0, 0) # Faz a validacao da lista, permitindo ter de 2 a 3 elementos
    radius: PositiveInt = 1  # Permite valores acima de zero


e = Esfera(center=(2,5))
print(e)

try:
    Esfera(center=(2,5, 4,7))
except ValidationError as ex:
    print(ex)