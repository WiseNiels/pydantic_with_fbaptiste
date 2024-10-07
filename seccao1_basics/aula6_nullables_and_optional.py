from pydantic import BaseModel
from pydantic import ValidationError
from typing import Union, Optional 

# Optional, Not Nullable
class Model(BaseModel):
    field: int = int()


print(Model())

