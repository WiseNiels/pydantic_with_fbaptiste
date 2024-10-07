from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    field_1: int


# Nesse caso os extra fields sao totalmente ignorados
m = Model(field_1=10, field_2=20, field_3=30, field_4=40)

print(m)


class Model2(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )  # o nome dessa propriedadde deve ser exatamente essa
    field_1: int


# # Nesse caso os extra fields vao lancar uma excecao
# try:

#     Model2(field_1=10, field_2=20, field_3=30, field_4=40)
# except ValidationError as ex:
#     print(ex)


class Model3(BaseModel):

    model_config = ConfigDict(
        extra='allow' 
    )  # o nome dessa propriedadde deve ser exatamente essa
    field_1: int



m3 = Model3(field_1=10, field_2=20, field_3=30, field_4=40)

print(m3)
print(m3.model_fields_set)
print(m3.model_extra) # esta propriedade mostra os extra fields adicionados na instanciacao
print(Model3.model_config)