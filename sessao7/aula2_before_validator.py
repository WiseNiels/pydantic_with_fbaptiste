# Before Validator

from pydantic import BaseModel, Field, ValidationError, field_validator
from dateutil.parser import parse
from datetime import datetime
from typing import Any



class Model(BaseModel):
    dt: datetime



# print(parse('2020/1/1 3pm'))
# print(type(parse('2020/1/1 3pm')))

 