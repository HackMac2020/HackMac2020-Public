

with open("original with flag.jpg", "rb") as image:
    f = image.read()
    b = bytearray(f)

sqlite = "53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 33 00"
sqlite = sqlite.split(" ")
sqlite = [ int(i,16) for i in sqlite ]

for i in reversed(sqlite):
    b.insert(0,i)

with open("Joker.db","wb") as out:
    out.write(b)

