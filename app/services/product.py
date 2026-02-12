
from app.data.data import all_products
from app.schemas.product import Product
from fastapi import HTTPException


def create_product(product: Product):
    for pr in all_products:
        if pr["name"] == product.name:
            raise HTTPException(
            status_code=400,
                detail="this product already exits"
            )

    all_products.append(product.model_dump())
    return all_products
    
    
