from pydantic import BaseModel, ValidationError, Field, ConfigDict
from pydantic.alias_generators import to_camel, to_snake, to_pascal


print(to_camel("last_name"))


def make_upper(in_str: str) -> str:
    return in_str.upper()


class Model(BaseModel):
    model_config = ConfigDict(
        alias_generator=make_upper
    )  # Esta onfiguracao faz com que o pydantic crie os alias com base no retorno da funcao passada
    id_: int
    first_name: str | None = None
    last_name: str
    age: int | None = None


# print(Model.model_fields)

# m = Model(id_=1, first_name='Wise', last_name='Muronha', age=45) # Lanca um erro


def make_alias(field_name) -> str:
    alias = to_camel(field_name)
    return alias.removesuffix("_")


class Person(BaseModel):
    model_config = ConfigDict(
        alias_generator=make_alias, populate_by_name=True
    )  # Esta onfiguracao faz com que o pydantic crie os alias com base no retorno da funcao passada
    id_: int
    filter_: bool | None = None
    first_name: str | None = None
    last_name: str
    age: int | None = None


print(Person.model_fields)
print(Person(id=2, firstName="WIse", lastName="NIels", age=45))
print(
    Person(id_=3, first_name="WIse", last_name="Paulo", age=34).model_dump_json(
        by_alias=True
    )
)
