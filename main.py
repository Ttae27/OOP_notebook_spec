from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import unquote
import json

from ui.catalog import Catalog
from ui.product import Product
from ui.compare import Compare
from ui.build import Build
from user.account import Account
from ui.payment_processor import PaymentProcessor

app = FastAPI()

# Create instance
product = Product()
catalog = Catalog(product)
compare = Compare()
account = Account()
build = Build(product)
payment_process = PaymentProcessor(build)

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
async def get_products(product_cat: str, filter = None):
    if filter:
        encoded_str = filter
        decoded_str = unquote(encoded_str)
        filter = json.loads(decoded_str)
    return catalog.list_product(product_cat, filter)

@app.get("/products/{product_cat}/{id}")
async def get_product_spec(product_cat: str, product_id: int):
    return catalog.get_item(product_cat, product_id)

@app.get("/products/search/{product_cat}")
async def search_product(product_cat: str, product_name: str):
    return catalog.list_product(product_cat, {"full_name": product_name})

#*Admin access only
@app.post("/admin/products/{product_cat}")
async def add_product(product_cat: str, new_product: dict):
    return product.add_product(product_cat, new_product)

@app.delete("/admin/products/{product_cat}")
async def delete_product(product_cat: str, product_id: int):
    return product.delete_product(product_cat, product_id)

@app.put("/admin/products/{product_cat}")
async def update_price(product_cat: str, product_id: int, new_price: int):
    return product.update_price_product(product_cat, product_id, new_price)

#***************************************<<catalog>>******************************************

@app.get("/product/compare")
async def compare_spec():
    return compare.compare_spec()

@app.post("/product/compare")
async def add_product_compare(cat: str, product_id: int, compare_number: int):
    return compare.add_item(catalog.get_item(cat, product_id)[0], compare_number)

@app.delete("/product/compare")
async def delete_product_compare(compare_number: int):
    return compare.remove_item(compare_number)

#***************************************<<user>>******************************************

@app.post("/signup")
async def signup(user_data: dict):
    user_data = tuple(user_data.values())
    return account.sign_up(user_data)

@app.post("/signin")
async def signin(credential: dict):
    usr = credential['username']
    passwd = credential['password']
    return account.sign_in(usr, passwd)

@app.put("/{user_id}/update")
async def update(user_id, type, new_data: str):
    return account.update_user(int(user_id), type, new_data)

@app.delete("/{user_id}/delete")
async def delete(user_id):
    return account.delete_user(int(user_id))

@app.get("/transaction_history")
async def transac_his():
    return account.current_user.transaction_history

#! debug
@app.get("/test_acc")
async def get_all_acc():
    lst = []
    for acc in account.allaccount:
        lst.append(vars(acc))
    return lst

@app.get("/test_cur_acc")
async def get_cur_acc():
    lst = []
    lst.append(vars(account.current_user))
    return lst

#*****************************************<<build>>*******************************************

@app.get('/build')
async def show():
    return build.show_build()

@app.post("/build/add/{product_cat}")
async def build_com(product_cat: str, product: dict):
    product_id = product['id']
    return build.add_to_build(product_cat, product_id)

@app.get('/build/price')
async def total_price():
    return {'price': build.totalprice}

@app.delete('/build/remove')
async def delete_from_build(product: dict):
    product_id = int(product['id'])
    build.remove_from_build(product_id)
    return build.show_build()

#*******************************************<<payment>>***************************************
    
@app.post('/payment')
async def payment_processing(payment_method):
    return {'payment': payment_process.select_payment(payment_method)}

@app.post('/creditcard')
async def credit_card_payment(card_number,expiration_date,cvv): 
    return payment_process.process_credit_card_payment(card_number,expiration_date,cvv, account.current_user)

@app.post('/cashtransfer')
async def cash_transfer_payment(cash): 
    return payment_process.process_cash_Transfer_payment(cash, account.current_user)

