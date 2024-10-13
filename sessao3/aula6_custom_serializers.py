from pydantic import BaseModel, field_serializer, FieldSerializationInfo
from datetime import datetime


class Model(BaseModel):
    dt: datetime | None = None

    @field_serializer('dt', when_used='always')
    # No momneto de serializacao essa funcao sempre sera chamada
    def serialize_name(self, value):
        print(f'type = {type(value)}')
        return value.date()


m = Model(dt='2024-10-11T13:00:00')
print(m)

print(m.model_dump())
print(m.model_dump_json())


class Model2(BaseModel):
    dt: datetime | None = None

    @field_serializer('dt', when_used='json-unless-none') # usando somente na serializacao para Json enquando o valor nao for None
    def serialize_name(self, value):
        print(f'type = {type(value)}')
        return value.strftime('%Y/%m/%d %I:%M %p')


m2 = Model2(dt='2024-10-11T13:00:00')
print(m2.model_dump_json())


class Model3(BaseModel):
    dt: datetime | None = None

    @field_serializer('dt', when_used='json-unless-none') # usando somente na serializacao para Json enquando o valor nao for None
    def serialize_name(self, value, info: FieldSerializationInfo): # o parametro info pode ser qualquer nome
        print(f'Info {info}')
        print(f'is_json = {info.mode_is_json()}')
        return value.strftime('%Y/%m/%d %I:%M %p')


m3 = Model3(dt='2024-10-11T13:00:00')
print(m3.model_dump_json()) 