from pydantic import BaseModel, ValidationError, Field, ConfigDict



response_json = """
{
    "ID":100,
    "FirstName":"Wise",
    "lastname":"Muronha"
}
"""


class Model(BaseModel):
    # model_config = ConfigDict(populate_by_name=True) # permite que na instanciacao do model, possamos passar o nome do field e nao somente o alias
    id_: int = Field(alias='ID')
    first_name: str = Field(alias='FirstName')
    last_name: str = Field(alias='lastname')


m = Model.model_validate_json(response_json)

print(m)
print(m.model_dump_json(by_alias=True))


class Model(BaseModel):
    # model_config = ConfigDict(populate_by_name=True) # permite que na instanciacao do model, possamos passar o nome do field e nao somente o alias
    id_: int = Field(alias='ID', serialization_alias='id')
    first_name: str = Field(alias='FirstName', serialization_alias='firstName')
    last_name: str = Field(alias='lastname', serialization_alias='lastName')


m = Model.model_validate_json(response_json)

print(m)
print(m.model_dump_json(by_alias=True))