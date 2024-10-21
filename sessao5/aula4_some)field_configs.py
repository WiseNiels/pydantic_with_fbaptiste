from pydantic import BaseModel, Field, ConfigDict, ValidationError


class Model(BaseModel):
    # Quando for serializado, sera excluido
    key: str = Field(default='Python', exclude=True)
    field: int = 23


print(Model())
print(Model().model_dump())
