from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# data structure defining 

class Tea(BaseModel):
    id: int
    name: str
    origin: str
    
teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"Message": "Welcome to the TEA HOUSE"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    global teas
    new_teas = [tea for tea in teas if tea.id != tea_id]
    if len(new_teas) == len(teas):
        return {"error": "Tea not found"}
    teas = new_teas
    return {"message": f"Tea with id {tea_id} deleted."}


