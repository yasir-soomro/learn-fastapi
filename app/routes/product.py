

from app.schemas.product import product_type
from fastapi import APIRouter , Depends
from app.data.data import all_products
from typing import List
from app.services.product import create_product

router = APIRouter(
    prefix="/Products",
    tags = ["Products"]
)

@router.get("/" , response_model=List[product_type])
def read_products ():
    return all_products

@router.post("/")
def create_product_ (dep = Depends(create_product)):
    return dep







