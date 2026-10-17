from pydantic import BaseModel, EmailStr, AnyUrl ,Field
from typing import List, Dict, Optional,Annotated


class patient(BaseModel):
    name:  Annotated[str,Field(max_length=25,title="Name of the Patient",description="Enter the name of the patient within 25 letters.",examples=["Murali","Hello"])]
    age: int = Field(gt = 0 , lt = 80 ,strict=True)
    email: EmailStr
    # linkedinurl:AnyUrl
    weight: float = False
    allergies: Optional[List[str]] = None
    married: Annotated[bool,Field(default=None)]
    contact_details: Dict[str, str]


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
    "age": 12,
    "email": "muralivmuralv89@gmail.com",
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

# patient2=patient(**info1)
# insert(patient2)

# info={"name":"murali",
#     "age":"twenty"}

# patient2=patientstr(**info)
# insert(patient2)
