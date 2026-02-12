from fastapi import APIRouter, HTTPException
from app.data.mongo import db
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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
def create_student(student: student_type):
    try:
        students_collection = db["students"]

        data = student.model_dump()
        data["name"] = data["name"].lower()   # normalize name

        students_collection.insert_one(data)
        return {"message": "Student created successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{name}")
def get_student_by_name(name: str):
    try:
        student = None
        for s in db["students"].find({"name": name.lower()}, {"_id": 0}):
            student = s
            break

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"student": student}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{name}")
def delete_student(name: str):
    try:
        students_collection = db["students"]
        result = students_collection.delete_one({"name": name.lower()})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"message": "Student deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{name}")
def update_student(name: str, student: student_type):
    try:
        students_collection = db["students"]

        data = student.model_dump()
        data["name"] = data["name"].lower()  # keep normalized

        result = students_collection.update_one(
            {"name": name.lower()},
            {"$set": data}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"message": "Student updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
