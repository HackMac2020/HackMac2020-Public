const fs = require("fs");
const express = require("express");
const serveIndex = require("serve-index");
const cookieParser = require("cookie-parser");
const jsonwebtoken = require("jsonwebtoken");
const logger = require("morgan");
const app = express();
const port = 1337;

var flag = "";
fs.readFile("FLAG.txt", "utf8", (err, data) => {
    if (err) {
        return console.error(err);
    }

    flag = data;
});

app.use(cookieParser());
// Expose the public key
app.use("/pki", express.static(__dirname + "/pki"));
app.use("/pki", serveIndex(__dirname + "/pki"));
app.use(
    logger(
        ':remote-addr - :remote-user [:date[clf]] ":method :url HTTP/:http-version" :status :res[content-length] ":referrer" ":user-agent"'
    )
);

const initialUser = "hackymacky";

app.get("/", (req, res) => {
    if (!req.cookies.auth) {
        var privateKey = fs.readFileSync("real_private_key.pem");
        res.cookie(
            "auth",
            jsonwebtoken.sign(
                { user: initialUser },
                { key: privateKey, passphrase: "hackmac" },
                {
                    algorithm: "RS256",
                }
            )
        ).send(
            res.send(`
        <html>
            <head>
                <link href='https://fonts.googleapis.com/css?family=Raleway:200,400,800' rel='stylesheet' type='text/css'>
                <style>
                    .large-header {
                        display: flex;
                        height: 100%;
                        justify-content: center;
                        align-items: center;
                        font-family: 'Raleway', Calibri, Arial, sans-serif;
                    }
                    .main-title {
                        font-size: 3rem;
                        font-weight: 800;
                    }
                    .thin {
                        font-weight: 200;
                    }
                </style>
            </head>
            <body>
                <div id="large-header" class="large-header">
                    <h1 class="main-title">Hello again <span class="thin">${initialUser}</span></h1>
                </div>
            </body>
        </html>
        `)
        );

        return;
    }

    var publicKey = fs.readFileSync("./pki/public_key.pem");
    var jwt;
    try {
        jwt = jsonwebtoken.verify(req.cookies.auth, publicKey, {
            // Here is the bug - Shouldn't include both symmetric and assymetric algos here
            algorithms: ["RS256", "HS256"],
        });
        console.log(jwt);
    } catch (error) {
        console.error("Invalid JWT.");
        res.status(400).send({ error: "Invalid JWT", jwt: req.cookies.auth });
        return;
    }

    if (jwt.user === "admin") {
        res.send(`
            <html>
                <head>
                    <link href='https://fonts.googleapis.com/css?family=Raleway:200,400,800' rel='stylesheet' type='text/css'>
                    <style>
                        .large-header {
                            display: flex;
                            height: 100%;
                            justify-content: center;
                            align-items: center;
                            font-family: 'Raleway', Calibri, Arial, sans-serif;
                        }
                        .main-title {
                            font-size: 3rem;
                            font-weight: 800;
                        }
                        .thin {
                            font-weight: 200;
                        }
                    </style>
                </head>
                <body>
                    <div id="large-header" class="large-header">
                        <h1 class="main-title">Hello again admin! Here is your flag <span class="thin">${flag}</span></h1>
                    </div>
                </body>
            </html>
        `);
    } else {
        res.send(`
        <html>
            <head>
                <link href='https://fonts.googleapis.com/css?family=Raleway:200,400,800' rel='stylesheet' type='text/css'>
                <style>
                    .large-header {
                        display: flex;
                        height: 100%;
                        justify-content: center;
                        align-items: center;
                        font-family: 'Raleway', Calibri, Arial, sans-serif;
                    }
                    .main-title {
                        font-size: 3rem;
                        font-weight: 800;
                    }
                    .thin {
                        font-weight: 200;
                    }
                </style>
            </head>
            <body>
                <div id="large-header" class="large-header">
                    <h1 class="main-title">Hello again <span class="thin">${jwt.user}</span></h1>
                </div>
            </body>
        </html>
        `);
    }
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});

process.on("SIGINT", function () {
    console.log("Caught interrupt signal");

    if (i_should_exit) process.exit();
});
