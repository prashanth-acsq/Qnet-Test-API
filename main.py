import json
import string
import random as r

from fastapi import FastAPI

############################################################################################################

db = json.load(open("db.json", "r"))

############################################################################################################

app = FastAPI()


@app.get("/")
async def root():
    return "Root Page", 


@app.get("/wakeup")
async def root():
    return "Awake", 


@app.get("/random-strings")
async def random_strings():
    return "".join(r.choices(string.ascii_letters, k=5)), \
           "".join(r.choices(string.ascii_letters, k=5)), \
           "".join(r.choices(string.ascii_letters, k=5))


@app.get("/random-number")
async def random_number():
    return str(r.randint(100, 10000)), 


@app.get("/random-person")
async def random_person():
    return str(db["DB"][r.randint(0, len(db["DB"])-1)]["Name"]), \
           str(db["DB"][r.randint(0, len(db["DB"])-1)]["Phone Number"]), \
           str(db["DB"][r.randint(0, len(db["DB"])-1)]["Job"])
    

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
