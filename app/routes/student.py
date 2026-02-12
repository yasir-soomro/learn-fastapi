from fastapi import APIRouter, HTTPException
from app.data.mongo import get_collection
from app.schemas.student import Student

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

COLLECTION_NAME = "students"


def normalize_name(name: str) -> str:
    return name.strip().lower()


@router.get("/")
def get_students():
    try:
        students_collection = get_collection(COLLECTION_NAME)
        students = list(students_collection.find({}, {"_id": 0}))
        return {"students": students}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
def create_student(student: Student):
    try:
        students_collection = get_collection(COLLECTION_NAME)
        data = student.model_dump()
        data["name"] = normalize_name(data["name"])

        existing = students_collection.find_one(
            {"name": data["name"]},
            {"_id": 0},
        )
        if existing:
            raise HTTPException(status_code=400, detail="Student already exists")

        students_collection.insert_one(data)
        return {"student": data}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{name}")
def get_student_by_name(name: str):
    try:
        students_collection = get_collection(COLLECTION_NAME)
        student = students_collection.find_one(
            {"name": normalize_name(name)},
            {"_id": 0},
        )

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
        students_collection = get_collection(COLLECTION_NAME)
        result = students_collection.delete_one({"name": normalize_name(name)})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"message": "Student deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{name}")
def update_student(name: str, student: Student):
    try:
        students_collection = get_collection(COLLECTION_NAME)
        data = student.model_dump()
        data["name"] = normalize_name(data["name"])

        result = students_collection.update_one(
            {"name": normalize_name(name)},
            {"$set": data}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

        return {"student": data}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
