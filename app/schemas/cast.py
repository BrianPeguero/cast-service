from pydantic import BaseModel

class CastBase(BaseModel):
    id:int
    name:str
    nationality:str


class CastIn(CastBase):
    class Config:
        orm_mode=True

class CastOut(CastBase):
    class Config:
        orm_mode=True