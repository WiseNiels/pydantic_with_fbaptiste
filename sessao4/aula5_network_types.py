from pydantic import BaseModel, EmailStr, NameEmail, ValidationError, HttpUrl, IPvAnyAddress


class Model(BaseModel):
    email: EmailStr


m = Model(email='Wise@gmail.com')
print(m)


# try:
#     Model(email='Wise@gmailcom')
# except ValidationError as ex:
#     print(ex)


class Model(BaseModel):
    email: NameEmail


m = Model(email='Wise@gmail.com')
print(m)
print(m.email.name)
print(m.email.email)


class ExternalAPI(BaseModel):
    root_url: HttpUrl


api = ExternalAPI(root_url='https://www.google.com')
print(f'{api.root_url}user')


class IP(BaseModel):
    ip: IPvAnyAddress

ip = IP(ip='192.168.0.1')
print(ip)
 