from pydantic import BaseModel
from pydantic import ValidationError
from typing import Union, Optional


class Model(BaseModel):
    field: int | None  # Assim o field e' um Nullable mas nao Optional


class Model2(BaseModel):
    field: int | None = None  # Assim o field e' um Nullable e Optional

# para as versoes anteriores a 3.10


class Model2(BaseModel):
    field: Union[int, None] = None  # Assim o field e' um Nullable e Optional
    
class Model3(BaseModel):
    field: Optional[int]  # Assim o field e' um Nullable e nao Optional
class Model4(BaseModel):
    field: Optional[int] = None # Assim o field e' um Nullable e Optional

print(Model4.model_fields)
Model4()

