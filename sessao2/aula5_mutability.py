from pydantic import BaseModel, ValidationError, ConfigDict

# POr defaullt os model pydantic sao mutaveis

class Model(BaseModel):
    field : int
    
m = Model(field=10)
m.field = 100 #modificamos o valor inicial

# Definindo a imutabilidade


class Model2(BaseModel):
    model_config = ConfigDict(frozen=True) # difinindo a imutabilidade
    field : int

m = Model2(field=10)
try:
    m.field = 100 #modificamos o valor inicial
except ValidationError as ex:
    print(ex)