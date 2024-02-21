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
    let port = process.env.port || 9090

    cmd_line_args = process.argv.slice(2)

    if (cmd_line_args.includes("--host")) {
    	host = cmd_line_args[cmd_line_args.indexOf("--host") + 1]
  	}

  	if (cmd_line_args.includes("-h")) {
    	host = cmd_line_args[cmd_line_args.indexOf("-h") + 1]
  	}

  	if (cmd_line_args.includes("--port")) {
    	port = cmd_line_args[cmd_line_args.indexOf("--port") + 1]
  	}

  	if (cmd_line_args.includes("-p")) {
    	port = cmd_line_args[cmd_line_args.indexOf("-p") + 1]
 	}

    const express = require("express")
    const app = express()
    app.use("/static", express.static(path.join(__dirname, "static")))


    let db = JSON.parse(fs.readFileSync(path.join(__dirname, "static/db.json")))["DB"]

    //  curl -X GET -L "http://localhost:9090" -s
    app.get("/", (request, response) => {
        response.status(200)
        response.json({
            "statusText" : "Root Endpoint of Q-net Test API",
        })
    })

    // curl -X GET -L "http://localhost:9090/random" -s
    app.get("/random", (request, response) => {
        response.status(200)
        response.json({
            "statusText" : "Random Data Generation Endpoint of Q-net Test API",
        })
    })

    // curl -X GET -L "http://localhost:9090/random/strings" -s
    // curl -X GET -L "http://localhost:9090/random/number" -s
    // curl -X GET -L "http://localhost:9090/random/person" -s
    app.get("/random/:mode", (request, response) => {
        mode = request.params.mode
        if (mode === "strings"){
            response.status(200)
            response.json({
                "statusText" : "Random String Generation Successful",
                "strings" : [getRandomString(15), getRandomString(15), getRandomString(15)],
            })
        }

        else if (mode === "number"){
            response.status(200)
            response.json({
                "statusText" : "Random Number Generation Successful",
                "number" : Math.random(),
            })
        }

        else if (mode === "person"){
            response.status(200)
            response.json({
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
        response.status(200)
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
        console.log("\n" + "*".repeat(50) + "\n")
    	console.log(`Server running at http://${host}:${port}`)
		console.log("\n" + "*".repeat(50) + "\n")
    })
}

main()