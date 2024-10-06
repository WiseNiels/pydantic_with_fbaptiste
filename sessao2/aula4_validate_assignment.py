from pydantic import BaseModel, ValidationError, ConfigDict

class Model(BaseModel):
    field : int


m = Model(field=100)

m.field = 'python' #por enquanto isso aceita a pesar do tipo ser um integer

print(m)

class Model2(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    field : int


m = Model2(field=100)

try: 
    m.field = 'python'

except ValidationError as ex:
    print(ex)