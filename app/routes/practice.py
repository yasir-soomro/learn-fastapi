from fastapi import File, UploadFile, Form, APIRouter
import shutil, os, uuid
from pathlib import Path

UPLOAD_FOLDER = "app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

router = APIRouter(
    prefix="/upload",
    tags=["file upload"]
)

@router.post("/")
async def upload_file(
    file: UploadFile = File(...),
    description: str = Form(...)
):
    safe_name = Path(file.filename).name
    filename = f"{uuid.uuid4()}_{safe_name}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Uploaded",
        "filename": filename,
        "description": description,
        "url": f"/static/{filename}"
    }
