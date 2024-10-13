from pydantic import BaseModel, PositiveInt, ValidationError


class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: PositiveInt = 1 # Permite valores acima de zero
    

c = Circle(center=(2,3), radius=2)
print(c)

try:
    Circle(center=(2,6), radius=0)
except ValidationError as ex:
    print(ex)
