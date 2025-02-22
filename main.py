from fastapi import FastAPI
from enum import Enum 
from pydantic import BaseModel 





app = FastAPI() # for now am not going to pass any parameter to the Fastapi class 

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: str | None = None 
    price: float
    tax: float| None = None 


@app.get("/")
async def root():
    return {"messange":"hello world"}
# path paramter 

@app.get("/items/{item_id}") # item_id -> is a path paramter 
async def return_item(item_id:int): # this mean item_id is an iteger 
    return {"item_id":item_id} 


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "messange": "Deep Leaning ftw!"}
    if model_name.value  == "lenet":
        return {"model_name":model_name, "messange": "LeCCN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}



@app.get("/items/{item_id}")
async def read_itme(item_id: str, q: str | None = None):
    if q:  
        ... 
        return 
    return item_id 

@app.post("/items/")
async def create_item(item:Item):
    return item 



