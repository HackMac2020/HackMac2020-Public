const express = require("express");
var morgan = require("morgan");
const app = express();
const serveIndex = require("serve-index")
const publicPath = "./build";
const port = 1337;

app.use(morgan("combined"));
app.use(express.static(publicPath, {dotfiles:"allow"}));
app.use("/.git.bak", serveIndex(publicPath + "/.git.bak", {hidden:true}))


/*
// Don't need this crap I'm pretty sure just keep incase
app.use("*", express.static(publicPath));

app.get("*", (req, res) => {
    console.log("Hello")
    res.sendFile(path.join(publicPath, "index.html"));
});
*/

app.listen(port, () => {
    console.log(`Server is up on port ${port}`);
});
