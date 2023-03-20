from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from fastapi.encoders import jsonable_encoder

app = FastAPI()
error_404 = str("Animal not found")


animals = {
    "Napo" : {"name" : "Napo", "species" : "Cat", "height" : 25.5},
    "Parlanchin" : {"name" : "Parlanchin" , "species" : "Parrot", "day_of_register" : 2022-9-15},
    "Stuart" : {"name" : "Stuart", "species" : "Mouse", "age" : 4, "weight" : 0.33},
    "Yeti" : {"name" : "Yeti", "species" : "Dog", "weight" : 25.6, "age" : 5, "day_of_register" : 2021-7-14 }
}

class Animal(BaseModel):
    name : str
    species : str
    age : int  | None = None
    weight : float  | None = None
    height : float | None = None
    owner_name : str | None = None
    day_of_register : date  | None = None


@app.post("/new_register/")
async def create_item(new_animal : Animal):
    new_animal_encoded =jsonable_encoder(new_animal)
    animals[new_animal.name] = new_animal_encoded
    return animals[new_animal.name]


@app.get("/view_register/{name}", response_model=Animal)
async def read_items(name : str):
    if name not in animals:
        raise HTTPException(status_code=404, detail= error_404)
    return animals[name]

@app.put("/update_register/{name}")
async def update_item(name : str, animal : Animal):
    if name not in animals:
        raise HTTPException(status_code=404, detail= error_404)
    update_animal_encoded = jsonable_encoder(animal)
    animals[name] = update_animal_encoded
    return update_animal_encoded

@app.delete("/delete/{name}")
async def remove(name : str):
    if name not in animals:
        raise HTTPException(status_code=404, detail=error_404)
    del animals[name]
    delete_message = str("Animal correctly deleted")
    return delete_message

