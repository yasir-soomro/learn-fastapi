

from pydantic import BaseModel , Field


class product_type (BaseModel):
    name : str = Field (..., min_length=3)
    color : str = Field (..., min_length=3)
    price : int= Field (..., gt=0)

    

