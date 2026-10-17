from typing import List, Dict, Optional
from pydantic import BaseModel,EmailStr,model_validator


class patient(BaseModel):
    name:  str
    age: int 
    email: EmailStr
    weight: Optional[float]=None
    allergies: Optional[List[str]] = None
    married: bool
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Oh, the patient age is above 60, he must have an emergency contact.')
        return model


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
    "age": '60',
    "email": "muralivmuralv89@kbl.com",
    "weight": 59.6,
    "allergies": ["cough", "cold"],
    "married": True,
    # "contact_details": {"phone_no": "9663609014","emergency":"121435234"}
    "contact_details": {"phone_no": "9663609014"}
}
info1 = {
    "name": "murali",
    "age": 12,
    "contact_details": {"phone_no": "9663609014", "email": "muralivmuralv89@gmail.com"},
}

patient1 = patient(**info)
insert(patient1)