
from fastapi import FastAPI
from typing import List
from app.routes.product import router as read_products 





app = FastAPI()

app.include_router(router=read_products)



@app.get("/")
def read_root():
    return {"message": "Welcome to the Products API!"}

