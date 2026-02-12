


from app.data.mongo import db


from fastapi import APIRouter, HTTPException

from pymongo import MongoClient
from app.schemas.student import student_type


router = APIRouter(
    prefix="/students",
    tags=["students"]
)


@router.get("/")
def get_students():
    try:
        students_collection = db["students"]
        students = list(students_collection.find({}, {"_id": 0}))
        return {"students": students}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/")
def create_student(student: student_type):
    try:
        students_collection = db["students"]
        students_collection.insert_one(student.model_dump())
        return {"message": "Student created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    