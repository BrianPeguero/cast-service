from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session
from app.db.pg_db import SessionLocal

from app.schemas.cast import CastIn, CastOut
from app.db import db_manager

casts = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@casts.post('/', response_model=CastOut, status_code=201)
def create_cast(payload: CastIn, db:Session=Depends(get_db)):
    cast_id = db_manager.add_cast(payload, db)

    response = {
        'id': cast_id,
        **payload.dict()
    }

    return response

@casts.get('/{id}/', response_model=CastOut)
def get_cast(id: int, db:Session=Depends(get_db)):
    cast = db_manager.get_cast(id, db)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return cast