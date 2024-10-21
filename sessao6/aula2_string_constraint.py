from pydantic import Field, BaseModel, StringConstraints
from typing import Annotated, TypeVar


StandardString = Annotated[
    str, StringConstraints(to_lower=True, min_length=2, strip_whitespace=True)
]


class Model(BaseModel):
    code: StandardString | None = None
    
    
print(Model())
print(Model(code='ABCD   '))