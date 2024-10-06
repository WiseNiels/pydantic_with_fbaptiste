from pydantic import BaseModel, ValidationError, ConfigDict




class Model(BaseModel):
    model_config = ConfigDict(validate_default=True) # faz a validacao dos valores por default
    field_1: int = None
    field_2 : str = 100



try:
    Model()
except ValidationError as ex:
    print(ex)
