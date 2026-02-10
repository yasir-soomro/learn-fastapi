
from fastapi import FastAPI
from typing import List

from fastapi.staticfiles import StaticFiles
from app.routes.product import router as read_products 

from app.routes.practice import router as upload_file 

app = FastAPI()

app.include_router(router=read_products)
app.include_router(router=upload_file)

app.mount("/static", StaticFiles(directory="app/uploads"), name="static")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Products API!"}

