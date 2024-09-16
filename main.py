import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    curso: str
    active: bool


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@app.get("/functiontest")
async def functiontest():
    return {"test": True, "random_number": random.randint(0, 20000)}


@app.post("/students/register")
async def create_student(student: Student):
    return student


@app.put("/student/update/{id_student}")
async def update_student(id_student: int):
    return {"updated": id_student > 0}


@app.delete("student/delete/{id_student}")
async def delete_student(id_student: int):
    return id_student > 0
