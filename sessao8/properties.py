from pydantic import BaseModel, Field, ValidationError
from math import pi
from functools import cached_property


class Circle(BaseModel):
    center: tuple[float, float] = (0, 0)
    radius: int = Field(default=1, gt=0)

    @property
    def area(self):
        return pi * self.radius**2


c = Circle(center=(2, 5), radius=2)

print(c.model_dump())
print(c.area)
print(c.model_fields) #nessemomento a property area nao vai aparecer na lista


class Circle(BaseModel):
    center: tuple[float, float] = (0, 0)
    radius: int = Field(default=1, gt=0, frozen=True)

    @cached_property
    def area(self):
        print('Calculando a area')
        return pi * self.radius**2
    
    

print(c.model_dump())
print(c.area)