import json
import string
import random as r

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse


STATIC_PATH = "static"


app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

db = json.load(open(STATIC_PATH + "/db.json", "r"))


@app.get("/")
async def root():
    return JSONResponse({
        "statusCode" : 200,
        "statusText" : "Root Page"
    }) 


@app.get("/wakeup")
async def wakeup():
    return JSONResponse({
        "statusCode" : 200,
        "statusText" : "Awake"
    })


@app.get("/random-strings")
async def random_strings():
    return "".join(r.choices(string.ascii_letters, k=5)), \
           "".join(r.choices(string.ascii_letters, k=5)), \
           "".join(r.choices(string.ascii_letters, k=5))


@app.get("/random-number")
async def random_number():
    return JSONResponse([str(r.randint(100, 10000)), ])


@app.get("/random-person")
async def random_person():
    num = r.randint(0, len(db["DB"])-1)
    return str(db["DB"][num]["Name"]), \
           str(db["DB"][num]["Phone Number"]), \
           str(db["DB"][num]["Job"])
    

@app.get("/custom-format")
async def custom_format():
    return [{ 
        "value" : "Text 1", 
        "font" : {
            "family" : "Monospace",
            "height" : "60", 
            "color" : "red", 
            },
        },
        { 
        "value" : "Text 2", 
        "font" : {
            "family" : "Arial",
            "height" : "35", 
            "color" : "green", 
            },
        "background": { 
            "color": "lightgray" 
            }, 
        },]

############################################################################################################
