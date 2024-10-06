from pydantic import BaseModel, ValidationError, ConfigDict


# POr default number nao sao convertidos para str, principalmente em strict mode
class Model(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    field : str


m = Model(field=100)
print(m)