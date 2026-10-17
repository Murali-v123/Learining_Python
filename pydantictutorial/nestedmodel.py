from pydantic import BaseModel

class Address(BaseModel):
    city:str
    pincode:str
    state:str

class patient(BaseModel):
    name:str
    address:Address

def insert(patient:patient):
    print(patient.name)
    print(patient.address.pincode)
    print(patient.address.state)
    print(patient.address.city)

address_dict={'city':'bpt','pincode':'563114','state':'KA'}
address1=Address(**address_dict)

patient_dict={'name':'murali','address':address1}
patient1=patient(**patient_dict)
# insert(patient1)

# temp=patient1.model_dump()
# temp=patient1.model_dump(include=['name'])
# temp=patient1.model_dump(exclude=['name'])
temp=patient1.model_dump(exclude={'address':['state']})
print(temp)