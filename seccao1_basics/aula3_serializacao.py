# Serializacao consiste em pegar um model python/pydantic e transformar em dict ou json


from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    # as variaveis de classes sao chamadas de fields
    first_name: str
    last_name: str
    age: int
    


galois = Person(first_name='Evariste', last_name='Galois', age=20)



print(galois.__dict__)
print(vars(galois))

# serializar em dicionario
print(galois.model_dump())

# serializar para json

print(galois.model_dump_json())
print(galois.model_dump_json(indent=2))
# podemos escolher o que serializar
 
print(galois.model_dump_json(indent=2, exclude=['first_name']))
print(galois.model_dump_json(indent=2, include=['first_name']))