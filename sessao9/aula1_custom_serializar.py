from pydantic import BaseModel, ValidationError, BeforeValidator, AfterValidator, field_serializer, PlainSerializer
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


# DateTime = Annotated[datetime, BeforeValidator(
#     parse_datetime), AfterValidator(make_utc)]


# class Model(BaseModel):
#     dt: DateTime

#     @field_serializer('dt', when_used='json-unless-none')
#     def dt_json_serializer(self, dt: datetime) -> str:
#         return dt.strftime('%Y/%m/%d %I:%M %p (UTC)')


# m = Model(dt='2020/1/1 3pm')
# print(m)
# print(m.model_dump_json())

def dt_json_serializer(dt: datetime) -> str:
    return dt.strftime('%Y/%m/%d %I:%M %p (UTC)')


DateTime = Annotated[datetime,
                     BeforeValidator(parse_datetime),
                     AfterValidator(make_utc),
                     # sempre que for feita a serializacao sera chamada essa funcao
                     PlainSerializer(dt_json_serializer, when_used='json-unless-none')]


class Model(BaseModel):
    dt: DateTime


m = Model(dt='2020/1/1 3pm')
print(m)
print(m.model_dump_json())