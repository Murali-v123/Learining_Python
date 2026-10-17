from pydantic import BaseModel, EmailStr, AnyUrl ,Field ,field_validator
from typing import List, Dict, Optional,Annotated


class patient(BaseModel):
    name:  str
    age: int 
    email: EmailStr
    weight: float = False
    allergies: Optional[List[str]] = None
    married: bool
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid=['hdfc.com','kbl.com']

        domain_name=value.split('@')[-1]
        if domain_name not in valid:
            raise ValueError ("Not a valid domain")

        return value

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()

    @field_validator('age' ,mode = 'after')
    @classmethod
    def age_validator(cls, value):
        if 0<value<100:
            return value
        else:
            return ValueError("Invalid age")


class patientstr(BaseModel):
    name: str
    age: str


def insert(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("sucesss")


def update(patient: patient):
    print(patient.name)
    print(patient.age)
    print("update sucesss")


info = {
    "name": "murali",
    "age": '12',
    "email": "muralivmuralv89@kbl.com",
    "weight": 59.6,
    "allergies": ["cough", "cold"],
    "married": True,
    "contact_details": {"phone_no": "9663609014"},
}
info1 = {
    "name": "murali",
    "age": 12,
    "contact_details": {"phone_no": "9663609014", "email": "muralivmuralv89@gmail.com"},
}

patient1 = patient(**info)
insert(patient1)