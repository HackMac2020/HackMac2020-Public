const fs = require("fs");
const express = require("express");
var cookieParser = require("cookie-parser");
const jsonwebtoken = require("jsonwebtoken");
var logger = require("morgan");
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
app.use(
    logger(
        ':remote-addr - :remote-user [:date[clf]] ":method :url HTTP/:http-version" :status :res[content-length] ":referrer" ":user-agent"'
    )
);

const initialUser = "hackymacky";

app.get("/", (req, res) => {
    if (!req.cookies.auth) {
        res.cookie(
            "auth",
            jsonwebtoken.sign({ user: initialUser }, "secret")
        ).send();

        return;
    }

    jwt = jsonwebtoken.decode(req.cookies.auth);
    console.log(jwt);

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
                    <h1 class="main-title">Hello admin! Here is your flag <span class="thin">${flag}</span></h1>
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
                        font-size: 4rem;
                        font-weight: 800;
                    }

                    .thin {
                        font-weight: 200;
                    }
                </style>
            </head>

            <body>
                <div id="large-header" class="large-header">
                    <h1 class="main-title">Hello <span class="thin">${jwt.user}</span></h1>
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
