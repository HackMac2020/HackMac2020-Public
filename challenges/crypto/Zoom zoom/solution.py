import socket
import base64

# IP and PORT of the service
HOST = "chal.hackmac.xyz"
PORT = 30201

# Characters to bruteforce through
CHARS = [chr(i) for i in range(1, 256)]

def weak_decrypt(encodedMessage, key):
    # Base64 decode
    encrypted = base64.b64decode(encodedMessage).decode("UTF-8")
    # XOR Decrypt
    plaintext = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])
    return plaintext

# Check string is human readable
def is_readable(s):
    return all(31 < ord(c) < 127 for c in s)

def countNewlines(s):
    count = 0
    for c in s:
        if c == "\n":
            count += 1
    return count

# Ignore initial message and return encrypted sentence
def recvMessage(s):
    data = s.recv(4096, socket.MSG_PEEK)
    while countNewlines(data.decode("UTF-8")) < 2:
        data = s.recv(4096, socket.MSG_PEEK)

    data = s.recv(4096)
    return data.decode("UTF-8").split("\n")[1]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        # Encrypted sentence returned as string 
        encryptedData = recvMessage(s)

        # Check if we want to disconnect
        if not encryptedData or any(x in encryptedData for x in ["Server Disconnected", "hackmac", "Please stop"]):
            print(f"Server: {encryptedData}")
            break

        print(f"Server: {encryptedData}")

        # Bruteforce XOR
        possibleAnswers = []
        tempIndex = 0
        for char in CHARS:
            tempAnswer = weak_decrypt(bytes(encryptedData, "UTF-8"), char)
            if is_readable(tempAnswer):
                possibleAnswers.append(tempAnswer)
                print(f"{tempIndex} - {tempAnswer}")
                tempIndex += 1

        if len(possibleAnswers) == 0:
            print("WTF no answers?")
            break

        chosenIndex = int(input("Which index? "))
        s.send(bytes(possibleAnswers[chosenIndex], "UTF-8"))

print("Client closed")
