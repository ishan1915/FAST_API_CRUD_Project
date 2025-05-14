from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class ItemUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None
