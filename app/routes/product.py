

from app.schemas.product import product_type
from fastapi import APIRouter
from app.data.data import all_products
from typing import List


router = APIRouter(
    prefix="/Products",
    tags = ["Products"]
)

@router.get("/" , response_model=List[product_type])
def read_products ():
    return all_products







