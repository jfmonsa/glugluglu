from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Creamos un diccionario para almacenar los "items"
fake_items_db = {}

# Creamos el modelo de datos (Producto)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Endpoint para crear un nuevo "item"
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_id = len(fake_items_db) + 1  # Generamos un ID único
    fake_items_db[item_id] = item
    return item

# Endpoint para listar todos los "items"
@app.get("/items/", response_model=List[Item])
async def get_items():
    return list(fake_items_db.values())

# Endpoint para obtener un "item" por ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

# Endpoint para actualizar un "item" por ID
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_items_db[item_id] = item
    return item

# Endpoint para eliminar un "item" por ID
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[item_id]
    return {"detail": "Item deleted successfully"}
