const fs = require("fs");
const express = require("express");
const logger = require("morgan");
const app = express();
const port = 3000;
const serveIndex = require("serve-index");


// Read flag from file
var flag = "";
fs.readFile("/app/flag.txt", "utf8", (err, data) => {
    if (err) {
        return console.error(err);
    }

    flag = data;
});

// Logging
app.use(
    logger(
        'NODE - :remote-addr - :remote-user [:date[clf]] ":method :url HTTP/:http-version" :status :res[content-length] ":referrer" ":user-agent"'
    )
);

// Routes
app.get("/nothing_zone/../flag.txt", (req, res) => {
    res.send(flag);
});

// Error
app.use(function (err, req, res, next) {
    res.status(500).send("Bad user!");
});


// Run
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});

// Static serve
app.use("/nothing_zone", express.static("/app/src/public"));
app.use("/nothing_zone/..", serveIndex(__dirname + "/../"));

// Handle ctrl+c
process.on("SIGINT", function () {
    console.log("Caught interrupt signal");
    process.exit();
});
