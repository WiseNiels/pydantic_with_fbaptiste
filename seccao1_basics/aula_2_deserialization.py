# Deserializacao e' pegar dados JSON, dict, etc e gerar um objecto pydantic, Pydantic model

from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    # as variaveis de classes sao chamadas de fields
    first_name: str
    last_name: str
    age: int
    
    


p = Person(first_name='Wise', last_name='Muronha', age=27)

data = {
    'first_name':'Niels',
    'last_name': 'Jenny',
    'age': 23
}

# Deserializando a partit de um dicionario python

p = Person.model_validate(data)

print(p)

data_json = '''
{
    
"first_name":"Wise",
"last_name":"Nided",
"age":23
}

'''

# Para fazer o deserializing de Json usamos o metodo model_validate_json()

p2 = Person.model_validate_json(data_json)
print(p2)