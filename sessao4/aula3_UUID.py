from uuid import uuid4
from pydantic import BaseModel, Field, UUID4, ValidationError

# print(uuid4())


class Person(BaseModel):
    id: UUID4


p = Person(id=uuid4())
print(p)
print(p.model_dump_json())