from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def create_student(student: schemas.EstudanteCreate, db: Session =  Depends(get_db)):
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudantes/', response_model=List[schemas.EstudanteResponse])
def read_studentes(db: Session = Depends(get_db())):
    students = db.query(models.Estudante).all()
    return students