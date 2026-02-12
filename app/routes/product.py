
from fastapi import APIRouter, Depends
from app.schemas.product import Product
from app.data.data import all_products
from typing import List
from app.services.product import create_product

router = APIRouter(
    prefix="/Products",
    tags=["Products"]
)

@router.get("/", response_model=List[Product])
def read_products():
    return all_products

@router.post("/")
def create_product_(dep=Depends(create_product)):
    return dep







