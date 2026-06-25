from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import  models, schemas, crud
from database import engine,get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student Grade Tracker", description="A simple API to track student grades", version="1.0.0")

# Create 
@app.post("/students/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate,  db: Session = Depends(get_db)):
    return crud.create_student(db,student)


#  read all
@app.get("/students/", response_model=List[schemas.StudentResponse])
def get_students( db: Session = Depends(get_db)):
    return crud.get_students(db)


# read one
@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

# update

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student = crud.update_student(db,student_id, data)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
# delete
@app.delete("/students/{student_id}", response_model=schemas.StudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {'message': 'Student deleted successfully'}
