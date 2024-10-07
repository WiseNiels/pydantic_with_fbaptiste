from pydantic import BaseModel, ValidationError, Field

class Model(BaseModel):
    id_: int  = Field(alias='id')
    last_name: str = Field(alias='lastName')
    


json_data = '''
{
    "id":100,
    "lastName":"Muronha"
}
'''

m = Model.model_validate_json(json_data)

print(m)
print(Model(id=200, lastName='Mopola')) # Nesse momento estamos a fazer um deserializacao, portanto, temod que usar os alias

# Mas para recuperar os dados a partir do objecto, usamos o nome dos fields definidos na class
print(m.last_name)


# Para definir o default

class Model(BaseModel):
    id_: int  = Field(alias='id', default=100)
    last_name: str = Field(alias='lastName')


m = Model(lastName="Nided") # Deserializando
print(m)

# Serializando

# NB: Quando usamos o alias, por default ele somente se aplica para a deserializacao, nao para a serializacao
print(m.model_dump())

class Model(BaseModel):
    id_: int = Field(alias='id')
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")
    age: int | None = None


wise = Model(id=1, firstName='Wise NIels', lastName='Muronha', age=27)

print(wise.model_dump())
print(wise.model_dump(by_alias=True)) # Com esse parametro a serializacao usa os alias
print(wise.model_dump_json(by_alias=True)) # Com esse parametro a serializacao usa os alias
print(Model.model_fields)