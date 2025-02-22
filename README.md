# fastapi

fastapi generates a shema with allyour API using the OpenAPI standard for defining APIs.

**what is openAPI for**

the openapi shema is what powers the two interactive documentations systems inclued. 

and there are dozens of alternatives all based on openapi . you could easlity add andy of those alternatives to your applications built with fastapi. 

you could also use it to generate code automatically, for clients that communicates with yor api . for example , fronted , mobile or IOT applications. 

## PREDEFINED VALUES 

if you have a paht operation that receives a path parameter, but you want the possilbe valid path parameter values to be predefined, you can use a standard python Enum. 


## understanding Enum in fastapi 

in python, Enum (short for enumeration) is a way to define a set of named values. it is useful when you want to restrict a variabl to a predefined set of values. in fastapi , enum is commonly used on path parameters to ensure that only valid options are passed. 

## understanding path parameters contianing paths in fastpi 

*the proplem*

normally hwne defining a path parameter n fastapi , the parameter captures everythign up to the next / in the url. 

```py
@app.get("files/{file_path}")
asyncy def read_file(fie_path:str):
    return {"file_path":file_path}
```
if you were to make request using `GEt /files/home/johndoe/myfile.txt`

you will get an error 

to solve this do the following 

```py
from fastapi import Fastapi

app = Fastapi()

@app.get(/files/{file_path:path}")
...
```

**why openapi doest support it**
- openapi expects path parameters to be single segments 
- allowing paths inside parameters makes it harder for documentation tools to predict request structres. 

so when you use path paramter excpect no support form openapi docs


## query parameters 


when you declare other function parameters that are not part of the part paraeters, they are automatically interpreted as query paramters.



```py
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

```
the query is the set of key-values pairs that go after ? in the url, seperated by & characters. 

for example in the url 

`http://127.0.0.1:8000/items/?skip=0&limit=10`


