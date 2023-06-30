from pydantic import BaseModel


class user(BaseModel):
    username: str
    password: str
    email: str
    phone_no: str


class Roombooking(BaseModel):
    name: str
    place: str
    number: str
