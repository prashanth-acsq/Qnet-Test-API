import os
import json
import string
import random as r

from fastapi import FastAPI, status, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse

STATIC_PATH = "static"

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

db = json.load(open(os.path.join(STATIC_PATH, "db.json"), "r"))


@app.get("/")
async def get_root():
    return JSONResponse({
        "statusCode" : status.HTTP_200_OK,
        "statusText" : "Root Endpoint of Q-net Test API"
    }) 


@app.get("/random")
async def get_random():
    return JSONResponse({
        "statusCode" : status.HTTP_200_OK,
        "statusText" : "Random Data Generation Endpoint of Q-net Test API"
    }) 


@app.get("/random/{mode}")
async def get_random_data(mode: str):
    if mode == "strings":
        return JSONResponse({
                "statusCode" : 200,
                "statusText" : "Random String Generation Successful",
                "strings" : [
                    "".join(r.choices(string.ascii_letters, k=15)), \
                    "".join(r.choices(string.ascii_letters, k=15)), \
                    "".join(r.choices(string.ascii_letters, k=15))
                ]
        })
            
    elif mode == "number":
        return JSONResponse({
            "statusCode" : 200,
            "statusText" : "Random Number Generation Successful",
            "number" : r.random(),
        })

    elif mode == "person":
        num = r.randint(0, len(db["DB"])-1)
        return JSONResponse({
            "statusCode" : 200,
            "statusText" : "Random Person Fetch Successful",
            "Person Info" : {
                "Name" : db["DB"][num]["Name"],
                "Phone Number" : db["DB"][num]["Phone Number"],
                "Job" : db["DB"][num]["Job"],
            },
        })

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
       

@app.get("/custom-format")
async def custom_format():
    return JSONResponse([{ 
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
        },])
