from typing import Union
from fastapi import FastAPI

from ui.Product import *
from ui.Build import Build
import glob
from user.user import User
from user.admin import Admin
from ui.Catalog import Catalog

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Pearwa"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}