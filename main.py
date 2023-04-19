from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from ui.Catalog import Catalog
from ui.Product import Product
from fastapi.middleware.cors import CORSMiddleware
import json
from urllib.parse import unquote

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
def get_products(product_cat: str, filter :Optional[str] = "", sort :Optional[int] = None):
    if filter:
        encoded_str = filter
        decoded_str = unquote(encoded_str)
        filter = json.loads(decoded_str)
        #!debug
        print(filter)
    return Catalog.list(product_cat, filter, sort)

@app.post("/admin/products/{product_cat}")
def add_products(product_cat: str, product: dict):
    return Product.add(product_cat, product)

@app.delete("/admin/products/{product_cat}")
def delete_products(product_cat: str, product_id: int):
    return Product.delete(product_cat, product_id)

@app.put("/admin/products/{product_cat}")
def modify_product(product_cat: str, product_id: int, product_key: str, product_value):
    return Product.modify(product_cat, product_id, product_key, product_value)

@app.get("/product/compare")
def compare(product_cat, product_id_1, product_id_2):
    pass
    