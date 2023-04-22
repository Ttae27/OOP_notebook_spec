from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from ui.Catalog import Catalog
from ui.Product import Product
from ui.compare import Compare
from fastapi.middleware.cors import CORSMiddleware
import json
from urllib.parse import unquote

app = FastAPI()

# Create instance
product = Product()
catalog = Catalog(product)
compare = Compare()

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
def get_products(product_cat: str, filter = None):
    if filter:
        encoded_str = filter
        decoded_str = unquote(encoded_str)
        filter = json.loads(decoded_str)
        #!debug
        print(filter)
    return catalog.list(product_cat, filter)

@app.post("/admin/products/{product_cat}")
def add_products(product_cat: str, new_product: dict):
    return product.add_product(product_cat, new_product)

@app.delete("/admin/products/{product_cat}")
def delete_products(product_cat: str, product_id: int):
    return product.delete_product(product_cat, product_id)

@app.put("/admin/products/{product_cat}")
def update_price(product_cat: str, product_id: int, new_price: int):
    return product.update_price_product(product_cat, product_id, new_price)

@app.get("/product/compare")
def compare_spec():
    return compare.compare_spec()

@app.post("/product/compare")
def add_product_compare(cat: str, product_id: int, compare_number: int):
    return compare.add_item(catalog.get_item(cat, product_id)[0], compare_number)

@app.delete("/product/compare")
def delete_product_compare(compare_number: int):
    return compare.remove_item(compare_number)

@app.get("/signup")
def signup():
    pass