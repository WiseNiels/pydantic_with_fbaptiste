from pydantic import BaseModel, ValidationError

# type coercion e' quando pydantic tenta converter um dado tipo para o tipo definido na classe/model
class Point(BaseModel):
    # as variaveis de classes sao chamadas de fields
    x: float
    y:float
    


p1 = Point(x=1.1, y=2.2)

# aqui acontecera o type cpercion
p2 = Point(x=0, y='2.2')

print(p2) #x=0.0 y=2.2



    