from sqlalchemy.orm import Session

from app.models.cast import Cast
from app.schemas.cast import CastIn, CastOut

def add_cast(payload: CastIn, db:Session):
    cast = Cast(
        id=payload.id,
        name=payload.name,
        nationality=payload.nationality
    )

    db.add(cast)
    db.commit()
    db.refresh()

    return cast

def get_cast(id, db:Session):

    cast = db.query(Cast).filter(Cast.id == id).first()

    return cast