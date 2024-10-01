# install pydantic - pip install pydantic

from pydantic import BaseModel  
from pydantic import ValidationError

class Person(BaseModel):
    # as variaveis de classes sao chamadas de fields
    first_name: str
    last_name: str
    age: int
    
p = Person(first_name='Wise', last_name='Muronha', age=27)

print(str(p))
print(repr(p))
print(p)

# obter os campos/fields
print(p.model_fields)

# Pydantic classes sao classes comuns do python - significa que podemos criar metodos e proprety

class King(BaseModel):
    first_name: str
    last_name: str
    age: int 
    
    
    @property
    def display_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
kg = King(first_name='Wise', last_name='Muronha', age=34)
print(kg.display_name)
print(kg.age)
print(kg.first_name)


try:
    Person(first_name='Wise', last_name='Muronha', age="Vinte")
except ValidationError as ex:
    print(ex)
    
