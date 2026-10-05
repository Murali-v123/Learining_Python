from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import session

import database_models
from database import SessionLocal, engine
from models import product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def greet():
    return "Welcom to learning of fastapi"


products = [
    product(id=1, name="Mobile", description="phone", price=12333, quantity=2),
    product(id=2, name="desktop", description="syy", price=12888, quantity=3),
    product(id=3, name="hat", description="fashion", price=1000, quantity=13),
    product(
        id=4, name="box", description="used for storing food", price=500, quantity=9
    ),
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    count = db.query(database_models.product).count()
    if count == 0:
        for prod in products:
            db.add(database_models.product(**prod.model_dump()))

        db.commit()


init_db()


@app.get("/products")
def get_all_products(db: session = Depends(get_db)):  # noqa: B008
    db_product=db.query(database_models.product).all()
    # db.query()
    return db_product


@app.get("/products/{id}")
def get_prod_by_id(id: int ,db: session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        return db_product
    return "product not found sorry"


@app.post("/products")
def add_product(prod: product , db: session = Depends(get_db)):
    # products.append(prod)
    db.add(database_models.product(**prod.model_dump()))
    db.commit()
    return prod


@app.put("/products/{id}")
def update_prod(id: int, prod: product , db: session = Depends(get_db) ):
    db_product = db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        db_product.name = prod.name
        db_product.description = prod.description
        db_product.price = prod.price
        db_product.quantity = prod.quantity
        db.commit()
        return "Product Updated"
    else:
        return "No product found" 

    


@app.delete("/products/{id}")
def delete_prod(id: int,db: session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted sucessfully"
    else:
        return "Product Not found"
