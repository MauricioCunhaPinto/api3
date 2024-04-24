from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import connect_to_db
from models.item import ItemModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

conn = connect_to_db()
item_model = ItemModel(conn)

@app.post("/items/", response_model=Item)
def create_item_endpoint(item: Item):
    return item_model.create_item(item)

@app.get("/items/{item_id}", response_model=Item)
def read_item_endpoint(item_id: int):
    return item_model.read_item(item_id)

@app.put("/items/{item_id}", response_model=Item)
def update_item_endpoint(item_id: int, item: Item):
    return item_model.update_item(item_id, item)

@app.delete("/items/{item_id}", response_model=Item)
def delete_item_endpoint(item_id: int):
    return item_model.delete_item(item_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
