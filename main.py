from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

# Crea las tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/dailies/")
def create_daily(daily: schemas.DailyCreate, db: Session = Depends(get_db)):
    db_daily = models.Daily(**daily.model_dump(), created_by=1)  # ejemplo: admin ID 1
    db.add(db_daily)
    db.commit()
    db.refresh(db_daily)
    return db_daily

@app.post("/responses/")
def create_response(response: schemas.DailyResponseCreate, db: Session = Depends(get_db)):
    db_response = models.DailyResponse(**response.model_dump())
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    return db_response
