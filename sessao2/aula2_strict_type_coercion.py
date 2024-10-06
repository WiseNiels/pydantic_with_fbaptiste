from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):
    model_config = ConfigDict(strict=True)
    field_1: str
    field_2: int
    field_3: list
    field_4: tuple


try:
    Model(field_1='abc', field_2=1, field_3=(1,2,3), field_4=[1,2,3])
except ValidationError as ex:
    print(ex)
