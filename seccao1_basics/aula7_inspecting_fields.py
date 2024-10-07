from pydantic import BaseModel, ValidationError


class Circle(BaseModel):
    center_x: int = 0
    center_y: int = 0
    radius: int = 0
    name: str | None = None


print(Circle.model_fields)


c1 = Circle(radius=3)
print(c1.model_fields_set) # model_fields_set mostra todos os fields que foram setados na instanciacao do Model