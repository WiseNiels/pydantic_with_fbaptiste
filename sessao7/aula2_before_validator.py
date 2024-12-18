# Before Validator

from pydantic import BaseModel, Field, ValidationError, field_validator
from dateutil.parser import parse
from datetime import datetime
from typing import Any


class Model(BaseModel):
    dt: datetime

    @field_validator('dt', mode='before')
    @classmethod
    def parse_datetime(cls, value: Any):
        if isinstance(value, str):
            print('parsing string')
            try:
                return parse(value)
            except Exception as ex:
                raise ValueError(str(ex))
        print('pass through...')
        return value


print(Model(dt='2020/1/1 3pm'))
print(Model(dt=datetime.now())) #  A mensagem aqui e' diferente


# print(parse('2020/1/1 3pm'))
# print(type(parse('2020/1/1 3pm')))
