from fastapi import FastAPI
from enum import Enum 




app = FastAPI() # for now am not going to pass any parameter to the Fastapi class 

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"




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

