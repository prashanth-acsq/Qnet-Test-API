import os
import sys
import json
import string
import random as r

from sanic import Sanic
from sanic.request import Request
from sanic.response import JSONResponse
from sanic.exceptions import SanicException

HOST: str = "0.0.0.0"
PORT: int = 47111

db = json.load(open(os.path.join("static", "db.json"), "r"))

app = Sanic("Sanic-Qnet-Test-API")
app.static("/static", "./static")


@app.get("/")
async def get_root(request: Request) -> JSONResponse:
    return JSONResponse(
        body={"statusText": "Root Endpoint of Qnet Test API"},
        status=200,
    )


@app.get("/random")
async def get_random(request: Request):
    return JSONResponse(
        body={
            "statusText": "Random Data Generation Endpoint of Q-net Test API",
        },
        status=200,
    )


@app.get("/random/<mode:str>")
async def get_random_data(request: Request, mode: str):
    if mode == "strings":
        return JSONResponse(
            body={
                "statusText": "Random String Generation Successful",
                "data": [
                    "".join(r.choices(string.ascii_letters, k=15)),
                    "".join(r.choices(string.ascii_letters, k=15)),
                    "".join(r.choices(string.ascii_letters, k=15)),
                ],
            },
            status=200,
        )

    elif mode == "number":
        return JSONResponse(
            body={
                "statusCode": 200,
                "statusText": "Random Number Generation Successful",
                "data": r.random(),
            },
            status=200,
        )

    elif mode == "person":
        num = r.randint(0, len(db["DB"]) - 1)
        return JSONResponse(
            body={
                "statusCode": 200,
                "statusText": "Random Person Fetch Successful",
                "data": {
                    "Name": db["DB"][num]["Name"],
                    "Phone Number": db["DB"][num]["Phone Number"],
                    "Job": db["DB"][num]["Job"],
                },
            },
            status=200,
        )

    else:
        raise SanicException(message="Endpoint Not Found", status_code=404)


@app.get("/custom-format")
async def custom_format(request: Request):
    return JSONResponse(
        body=[
            {
                "value": "Text 1",
                "font": {
                    "family": "Monospace",
                    "height": "60",
                    "color": "red",
                },
            },
            {
                "value": "Text 2",
                "font": {
                    "family": "Arial",
                    "height": "35",
                    "color": "green",
                },
                "background": {"color": "lightgray"},
            },
        ],
        status=200,
    )


if __name__ == "__main__":
    args_1: tuple = ("-m", "--mode")
    args_2: tuple = ("-p", "--port")
    args_3: tuple = ("-w", "--workers")

    mode: str = "local-machine"
    port: int = 9090
    workers: int = 1

    if args_1[0] in sys.argv:
        mode = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv:
        mode = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv:
        port = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv:
        port = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv:
        workers = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv:
        workers = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    if mode == "local-machine":
        app.run(host="localhost", port=port, dev=True, workers=workers)

    elif mode == "local":
        app.run(host="0.0.0.0", port=port, dev=True, workers=workers)

    elif mode == "render":
        app.run(host="0.0.0.0", port=port, single_process=True, access_log=True)

    elif mode == "prod":
        app.run(host="0.0.0.0", port=port, dev=False, workers=workers, access_log=True)

    else:
        raise ValueError("Invalid Mode")
