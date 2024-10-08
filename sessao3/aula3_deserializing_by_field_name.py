from pydantic import BaseModel, ValidationError, Field, ConfigDict


class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True) # permite que na instanciacao do model, possamos passar o nome do field e nao somente o alias
    id_: int = Field(alias='id')
    first_name: str = Field(alias='firstName')



print(Model(id=1, first_name='Wise')) #deserializing