from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from ui.Catalog import Catalog
from ui.Product import Product
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class cpu(BaseModel):
    pass

@app.get("/products/{product_cat}")
def get_products(product_cat: str, filter :Optional[str] = None, sort :Optional[str] = None):
    return Catalog.list(product_cat)

@app.delete("/admin/products/{product_cat}")
def delete_products(product_cat: str, product_id: int):
    return Product.delete(product_cat, product_id)

@app.put("/admin/products/{product_cat}")
def modify_product(product_cat: str, product_id: int, product_key: str, product_value):
    return Product.modify(product_cat, product_id, product_key, product_value)

