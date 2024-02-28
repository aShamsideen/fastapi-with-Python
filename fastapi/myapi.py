from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {"name": "Adekunle",
        "age": 30,
        "level": "400 Level"
        },
    2: {
        "name": "Sunbo",
        "age": 25,
        "level": "500 Level"
    },
    3: {
        "name": "Shamsideen",
        "age": 35,
        "level": "500 Level"
    }
}

class Student(BaseModel):
    name: str
    age: int
    level: str

class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    level: Optional[str] = None 


# Get Method
@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you wish to view", gt=0, lt=5)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id : int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return{"Data": "Not found"}

# Request Body and The Post Method
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return{"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]

# Put (Update) Method
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : updateStudent):
    if student_id not in students:
        return {"Error": "This student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.level != None:
        students[student_id].level = student.level

    return students[student_id]

# Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error": "This student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}