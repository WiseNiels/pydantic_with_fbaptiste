from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    name: str = Field(min_length=1, max_length=20)


m = Model(name='Wise Niels')

print(m)

try:
    Model(name='@'*23)
except ValidationError as ex:
    print(ex)