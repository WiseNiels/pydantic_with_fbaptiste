from pydantic import BaseModel, ValidationError, ConfigDict
from enum import Enum


class Color(Enum):
    red = 'Red'
    green = 'Green'
    blue = 'Blue'


class Model(BaseModel):
    color: Color


print(Model(color=Color.red))

data_json = """
{
    "color":"Red"
}
"""
# deserializacao
m = Model.model_validate_json(data_json)
print(m)

# Serializacao

print(m.model_dump()) #serializar pra dixionario
print(m.model_dump_json()) #serializar pra json


class Model2(BaseModel):
    model_config = ConfigDict(use_enum_values=True) # quando desejamos que os values do enum sejma retornados e nao os membros do enum
    color: Color


m2 = Model2(color=Color.green)
print(m2)
print(m2.model_dump())


class Model3(BaseModel):
    model_config = ConfigDict(use_enum_values=True, validate_default=True) # quando desejamos que os values do enum sejma retornados e nao os membros do enum
    color: Color = Color.red

print(Model3())