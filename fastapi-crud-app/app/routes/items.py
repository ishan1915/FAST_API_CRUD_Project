from fastapi import APIRouter, HTTPException
from app.models import Item
from app.schemas import ItemCreate, ItemUpdate
from app.database import items_db

router = APIRouter()

@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    new_item = Item(id=len(items_db) + 1, **item.model_dump())
    items_db.append(new_item)
    return new_item

@router.get("/", response_model=list[Item])
def read_items():
    return items_db

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = next((i for i in items_db if i.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemUpdate):
    item = next((i for i in items_db if i.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = item_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int):
    global items_db
    item = next((i for i in items_db if i.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db = [i for i in items_db if i.id != item_id]
    return {"message": "Item deleted"}