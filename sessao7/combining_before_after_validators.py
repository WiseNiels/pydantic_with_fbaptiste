from pydantic import BaseModel, Field, ValidationError, field_validator, BeforeValidator
from dateutil.parser import parse
from datetime import datetime
from typing import Any, Annotated
import pytz


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

    @field_validator('dt')  # after validator
    @classmethod
    def make_utc(cls, value: datetime) -> datetime:
        print('calling after validator')
        if value.tzinfo is None:
            dt = pytz.utc.localize(value)
        else:
            dt = value.astimezone(pytz.utc)
        return dt


print(Model(dt=100_000))
print(Model(dt='2020/1/1 3pm'))
