from fastapi import FastAPI
from models import product

app = FastAPI()


@app.get("/")
def greet():
    return "Welcom to learning of fastapi"

products=[
    product(id=1,name="Mobile",description="phone",price=12333,quantity=2),
    product(id=2,name="desktop",description="syy",price=12888,quantity=3),
]

@app.get("/products")
def get_all_products():
    return products

@a