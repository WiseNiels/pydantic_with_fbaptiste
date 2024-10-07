from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        str_to_upper=True
    )  # faz com que todos os campos str sejam aplicados o metodo strip() do python

    field: str


m = Model(field="      wise")

print(m)
