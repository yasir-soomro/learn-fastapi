from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., gt=0)
    grade: str = Field(..., min_length=1)

    
