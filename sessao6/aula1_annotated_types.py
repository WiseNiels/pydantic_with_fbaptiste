from pydantic import Field, BaseModel
from typing import Annotated, TypeVar


class Model(BaseModel):
    x: int = Field(gt=0, le=100)
    y: int = Field(gt=0, le=100)


BoundInt = Annotated[int, Field(gt=0, le=100)]


class Model2(BaseModel):

    x: BoundInt
    y: BoundInt


# Os Model e MOdel2 sao equivalentes
print(Model.model_fields)
print(Model2.model_fields)

#  Se quisermos criar uma tipgame mais generica podemos fazer como kostra abaixo:

T = TypeVar('T')

BoundList = Annotated[list[T], Field(max_length=10)]

print(BoundList[int])


class Model3(BaseModel):
    integers: BoundList[int] = []
    strings: BoundList[str] = list('python')


print(Model3())