from pydantic import BaseModel, ConfigDict, Field, ValidationError, AliasChoices
from pydantic.alias_generators import to_camel


class Persons(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(validation_alias="FirstName", alias="firstName")


p = Persons(FirstName="Wise")
print(p.model_dump())
print(p.model_dump_json(by_alias=True))


data = {"GivenName": "Wise", "lastName": "Muronha"}


class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    first_name: str = Field(
        validation_alias=AliasChoices("FirstName", "GivenName"), #aqui podemos usar tanto FirstName como GivenName no deserializer
        serialization_alias="givenName",
    )
    last_name: str


m = Model.model_validate(data)
print(m)
