from pydantic import BaseModel, Field
from typing import Annotated


def extract_first_char(s: str):
    if s is None:
        raise ValueError("argument cannot be None")
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    if len(s) == 0:
        raise ValueError("argument cannot be an empty string")
    return s[0]


try:
    extract_first_char(100)
except TypeError as ex:
    print(ex)
 