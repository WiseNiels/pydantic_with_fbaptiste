from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from time import sleep


class Logg(BaseModel):
    # Quando definimos um valor que seja padrao e seja proveniente de uma funcao, daefault factory vai sempre chamar o lambda a fim de sempre executar a funcao.
    dt: datetime = Field(default_factory=lambda: datetime.now())


print(Logg())
sleep(3)
print(Logg())
