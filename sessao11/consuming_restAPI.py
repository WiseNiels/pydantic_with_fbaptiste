from pydantic import BaseModel, ConfigDict, IPvAnyAddress, field_validator, Field
import requests


class IPGeo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ip: IPvAnyAddress
    country: str | None = None
    country_code: str | None = Field(default=None, min_length=2, max_length=2)
    country_code3: str | None = Field(default=None, min_length=2, max_length=3)
    city: str | None = None
    region: str | None = None
    timezone: str | None = None
    organization_name: str | None = None

    @field_validator("organization_name", mode="after")
    @classmethod
    def set_unknown_to_none(cls, value: str):
        if value.casefold() == "unknown":
            return None
        return value


# ip_ = IPGeo(
#     ip="8.8.8.8", country="test", country_code3="USA", organization_name="Unknown"
# )
# print(ip_)

url_query = "https://get.geojs.io/v1/geo/{ip_address}.json"

url = url_query.format(ip_address="8.8.8.8")
response = requests.get(url)
status = response.raise_for_status()
response_json = response.json()
print(response_json)
# print(status)

data = IPGeo.model_validate(response.json())
print(data)
