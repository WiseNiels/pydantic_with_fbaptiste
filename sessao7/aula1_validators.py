#  After Validator
from pydantic import BaseModel, Field, ValidationError, field_validator


class MOdel(BaseModel):
    number: int = Field(gt=0, lt=10)

    # Neste caso essa funcao correr depois da validacoes do tipos de dados pelo pydantic
    @field_validator('number')
    @classmethod
    def validate_even(cls, value):
        print('Running custom validator')
        print(f'{value=} {type(value)=} ')
        if value % 2 == 0:
            return value
        raise ValidationError('The value must be even')


print(MOdel(number=4 ))
print(MOdel(number='6'))
