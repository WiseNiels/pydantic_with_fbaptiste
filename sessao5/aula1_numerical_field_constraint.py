from pydantic import BaseModel, Field, ValidationError


class Mode(BaseModel):

    number: float = Field(gt=2, le=10, multiple_of=2)


m = Mode(number=4)

print(m)
print(Mode.model_fields)
