from pydantic import BaseModel, ValidationError, BeforeValidator, AfterValidator
from dateutil.parser import parse
from datetime import datetime
from typing import Any, Annotated
import pytz


def parse_datetime(value: Any):
    if isinstance(value, str):
        print('parsing string')
        try:
            return parse(value)
        except Exception as ex:
            raise ValueError(str(ex))
    print('pass through...')
    return value


def make_utc(value: datetime) -> datetime:
    print('calling after validator')
    if value.tzinfo is None:
        dt = pytz.utc.localize(value)
    else:
        dt = value.astimezone(pytz.utc)
    return dt


DateTime = Annotated[datetime, BeforeValidator(parse_datetime), AfterValidator(make_utc)]


class Model(BaseModel):
    dt: DateTime


print(Model(dt='2020/1/1 3pm'))
