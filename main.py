
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.product import router as read_products
from app.routes.practice import router as upload_file
from app.routes.student import router as student_router
app = FastAPI()

app.include_router(router=read_products)
app.include_router(router=upload_file)
app.include_router(router=student_router)

app.mount("/static", StaticFiles(directory="app/uploads"), name="static")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Products API!"}
