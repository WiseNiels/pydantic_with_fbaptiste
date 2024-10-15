from uuid import uuid4
from pydantic import BaseModel, Field, UUID4, ValidationError

# print(uuid4())


class Person(BaseModel):
    id: UUID4


p = Person(id=uuid4())
p2 = Person(id=uuid4())
print(p, p2)
# print(p.model_dump_json())


class Person(BaseModel):
    id: UUID4 = Field(default_factory=uuid4) # essa propriedade chama a funcao uuid4 sempre que nova instancia da class e' criada