import Path, fastapi
from typing import Optional
from pydantic import BaseModel

app = fastapi

class cpu(BaseModel):
    pass

@app.get("/products/{product_cat}")
def get_products(product_cat: str, filter :Optional[str] = None, sort :Optional[str] = None):
    pass