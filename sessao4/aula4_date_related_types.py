from pydantic import BaseModel, ConfigDict, PastDate, PastDatetime, AwareDatetime, NaiveDatetime, ValidationError


class Model(BaseModel):
    dt: NaiveDatetime


