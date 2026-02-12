from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(..., min_length=3)
    color: str = Field(..., min_length=3)
    price: int = Field(..., gt=0)

    

