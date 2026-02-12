


from pydantic import BaseModel, Field


class student_type (BaseModel):
    name : str = Field (..., min_length=3)
    age : int = Field (..., gt=0)
    grade : str = Field (..., min_length=1)

    