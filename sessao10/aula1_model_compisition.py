# Source
# https://github.com/fbaptiste/pydantic-essentials/blob/main/11%20-%20Complex%20Models/02%20-%20Model%20Composition.ipynb


from pydantic import BaseModel, ConfigDict, Field, ValidationError
from pydantic import EmailStr, PastDate
from pydantic.alias_generators import to_camel
from typing import Annotated
from pydantic import AfterValidator


class Point(BaseModel):
    x: float = 0
    y: float = 0


class Circle(BaseModel):
    center: Point  # Composicao
    radius: float = Field(default=1, gt=0)


c = Circle(center=Point(x=2, y=5), radius=3)
print(c.model_dump())  # serializacao

data = {'center': {'x': 2.0, 'y': 5.0}, 'radius': 3.0}

print(Circle.model_validate(data))  # deserializacao
print(c.center.x)  # obtendo a variavel


json_data = """
{
    "firstName": "David",
    "lastName": "Hilbert",
    "contactInfo": {
        "email": "d.hilbert@spectral-theory.com",
        "homePhone": {
            "countryCode": 49,
            "areaCode": 551,
            "localPhoneNumber": 123456789
        }
    },
    "personalInfo": {
        "nationality": "German",
        "born": {
            "date": "1862-01-23",
            "place": {
                "city": "Konigsberg",
                "country": "Prussia"
            }
        },
        "died": {
            "date": "1943-02-14",
            "place": {
                "city": "Gottingen",
                "country": "Germany"
            }
        }
    },
    "awards": ["Lobachevsky Prize", "Bolyai Prize", "ForMemRS"],
    "notableStudents": ["von Neumann", "Weyl", "Courant", "Zermelo"]
}
"""


class ContactInfo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    email: EmailStr | None = None


class PlaceInfo(BaseModel):
    city: str
    country: str


class PlaceDateInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    date_: PastDate = Field(alias="date")
    place: PlaceInfo


class PersonalInfo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    nationality: str
    born: PlaceDateInfo


# using an AfterValidator, so guaranteed value will be a list (empty or strings)
SortedStringList = Annotated[list[str], AfterValidator(
    lambda value: sorted(value, key=str.casefold))]


class Person(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel,
                              populate_by_name=True, extra="ignore")

    first_name: str
    last_name: str
    contact_info: ContactInfo
    personal_info: PersonalInfo
    # notable_students: list[str] = []
    notable_students: SortedStringList = Field(default=[], repr=False)


p = Person.model_validate_json(json_data)
print(p.model_dump_json())
