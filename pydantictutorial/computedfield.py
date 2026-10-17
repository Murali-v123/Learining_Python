from typing import Optional , List ,Dict

from pydantic import BaseModel, EmailStr, computed_field


class patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: Optional[float] = None  
    height:Optional[float] =None
    allergies: List[str] = None
    married: bool
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2))
        return bmi
   


class patientstr(BaseModel):
    name: str
    age: str


def insert(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print('bmi: ',patient.bmi)
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
    "age": "60",
    "email": "muralivmuralv89@kbl.com",
    "weight": 59.6,
    "height":2.5,
    "allergies": ["cough", "cold"],
    "married": True,
    # "contact_details": {"phone_no": "9663609014","emergency":"121435234"}
    "contact_details": {"phone_no": "9663609014"},
}


patient1 = patient(**info)
insert(patient1)
