getRandomString = (length) => {
    const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    const charLength = chars.length;
    let result = "";
    for ( var i = 0; i < length; i++ ) {
        result += chars.charAt(Math.floor(Math.random() * charLength));
    }
    return result;
 }


getRandomInt = (max) => {
    return Math.floor(Math.random() * max);
}


main = () => {
    const fs = require("fs")
    const path = require("path")

    let host = "localhost"
    let port = process.env.port || 5000

    cmd_line_args = process.argv.slice(2)

    if (cmd_line_args[0] == "--host" || cmd_line_args[0] == "-h"){
        host = cmd_line_args[1]
    }

    if (cmd_line_args[2] == "--port" || cmd_line_args[2] == "-p"){
        port = cmd_line_args[3]
    }

    const express = require("express")
    const app = express()
    app.use("/static", express.static(path.join(__dirname, "static")))


    let db = JSON.parse(fs.readFileSync(path.join(__dirname, "static/db.json")))["DB"]

    app.get("/", (request, response) => {
        response.json({
            "statusCode" : 200,
            "statusText" : "Root Endpoint of Q-net Test API",
        })
    })

    app.get("/random", (request, response) => {
        response.json({
            "statusCode" : 200,
            "statusText" : "Random Data Generation Endpoint of Q-net Test API",
        })
    })

    app.get("/random/:mode", (request, response) => {
        mode = request.params.mode
        if (mode === "strings"){
            response.json({
                "statusCode" : 200,
                "statusText" : "Random String Generation Successful",
                "strings" : [getRandomString(15), getRandomString(15), getRandomString(15)],
            })
        }

        else if (mode === "number"){
            response.json({
                "statusCode" : 200,
                "statusText" : "Random Number Generation Successful",
                "number" : Math.random(),
            })
        }

        else if (mode === "person"){
            response.json({
                "statusCode" : 200,
                "statusText" : "Random Person Fetch Successful",
                "Person Info" : {
                    "Name" : db[getRandomInt(db.length)]["Name"],
                    "Phone Number" : db[getRandomInt(db.length)]["Phone Number"],
                    "Job" : db[getRandomInt(db.length)]["Job"],
                }
            })
        }

        else{
            response.contentType(".html").sendStatus(404)      
        }
    })

    app.get("/custom-format", (request, response) => {
        response.json([
            { 
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
            },
        ])
    })

    app.listen(port, host, () => {
        console.log(`Server running at http://${host}:${port}/`)
    })
}

main()