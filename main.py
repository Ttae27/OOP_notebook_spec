from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import unquote
import json
import requests

from ui.catalog import Catalog
from ui.product import Product
from ui.compare import Compare

from user.account import Account


app = FastAPI()

# Create instance
product = Product()
catalog = Catalog(product)
compare = Compare()
account = Account()

#Create base model for request body
class User(BaseModel):
    id: int
    username: str
    password: str
    delivery_address: str
    phone: str
# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

#***************************************<<product>>******************************************

@app.get("/products/{product_cat}")
def get_products(product_cat: str, filter = None):
    if filter:
        encoded_str = filter
        decoded_str = unquote(encoded_str)
        filter = json.loads(decoded_str)
    return catalog.list(product_cat, filter)

@app.get("/products/{product_cat}/{id}")
def get_product_spec(product_cat: str, product_id: int):
    return catalog.get_item(product_cat, product_id)

#*Admin access only
@app.post("/admin/products/{product_cat}")
def add_product(product_cat: str, new_product: dict):
    return product.add_product(product_cat, new_product)

@app.delete("/admin/products/{product_cat}")
def delete_product(product_cat: str, product_id: int):
    return product.delete_product(product_cat, product_id)

@app.put("/admin/products/{product_cat}")
def update_price(product_cat: str, product_id: int, new_price: int):
    return product.update_price_product(product_cat, product_id, new_price)

#***************************************<<catalog>>******************************************

@app.get("/product/compare")
def compare_spec():
    return compare.compare_spec()

@app.post("/product/compare")
def add_product_compare(cat: str, product_id: int, compare_number: int):
    return compare.add_item(catalog.get_item(cat, product_id)[0], compare_number)

@app.delete("/product/compare")
def delete_product_compare(compare_number: int):
    return compare.remove_item(compare_number)

#***************************************<<user>>******************************************

@app.post("/signup")
def signup(user_data: dict):
    user_data = tuple(user_data.values())
    return account.sign_up(user_data)

@app.post("/signin")
def signin(credential: dict):
    usr = credential['username']
    passwd = credential['password']
    return account.sign_in(usr, passwd)

@app.put("/{user_id}/update")
def update(user_id, type, new_data: str):
    return account.update_user(int(user_id), type, new_data)

@app.delete("/{user_id}/delete")
def delete(user_id):
    return account.delete_user(int(user_id))

#! debug
@app.get("/test_acc")
def get_all_acc():
    lst = []
    for acc in account.allaccount:
        lst.append(vars(acc))
    return lst

