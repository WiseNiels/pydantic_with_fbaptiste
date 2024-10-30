from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict, BeforeValidator, AfterValidator, PlainSerializer
from typing import Annotated, Any
from datetime import datetime

from pydantic.alias_generators import to_camel


import pytz
from dateutil.parser import parse
from pydantic import AfterValidator, BeforeValidator, FieldSerializationInfo, field_serializer, PlainSerializer


def make_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt


def parse_datetime(value: Any):
    if isinstance(value, str):
        try:
            return parse(value)
        except Exception as ex:
            raise ValueError(str(ex))
    return value


def dt_serializer(dt, info: FieldSerializationInfo) -> datetime | str:
    if info.mode_is_json():
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return dt


DateTimeUTC = Annotated[
    datetime,
    BeforeValidator(parse_datetime),
    AfterValidator(make_utc),
    PlainSerializer(dt_serializer, when_used="unless-none")
]


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        alias_generator=to_camel,
        populate_by_name=True
    )


class RequestInfo(CustomBaseModel):
    query_id: uuid4 = Field(default_factory=uuid4)
    execution_dt: DateTimeUTC = Field(
        default_factory=lambda: datetime.now(pytz.utc))
    elapsed_time_secs: float


class ResponseBaseModel(CustomBaseModel):
    request_info: RequestInfo


class Users(ResponseBaseModel):
    users: list[str] = []


users = Users(request_info=RequestInfo(elapsed_time_secs=3.14),
              users=["Athos", "Porthos", "Aramis"])

print(users)