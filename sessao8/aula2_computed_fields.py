from pydantic import BaseModel, computed_field, Field, PydanticUserError, ValidationError
from functools import cached_property
from math import pi


class Circle(BaseModel):
    center: tuple[float, float] = (0, 0)
    radius: int = Field(default=1, gt=0, frozen=True)

    @computed_field() #para usar esse decorador, a funcao precisa explicitamente ter o tipo de retorno
    @property
    def area(self) -> float:
        print('Calculando a area')
        return pi * self.radius**2


c = Circle()
print(c.model_dump())
print(c.area)
print(c.area)
print(c.area)
