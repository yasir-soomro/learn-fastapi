
from app.data.data import all_products 
from app.schemas.product import product_type
from fastapi import HTTPException


def create_product(product : product_type):
    for pr in all_products:
        if   pr["name"]  == product.name:
            raise HTTPException(
            status_code=400,
                detail="this product already exits"
            )

    all_products.append(product.model_dump())
    return   all_products
    
    
