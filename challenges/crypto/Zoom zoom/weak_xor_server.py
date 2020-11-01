import socket
import threading
import json
import random
import base64

LISTENING = "0.0.0.0"
PORT = 1337
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LISTENING, PORT))

threads = []
ipThreads = {}

CHARS = [chr(i) for i in range(1, 256)]
FLAG = "hackmac{long_keys_are_for_the_weak}"
REQUIRED_CORRECT = 6

with open("sentences.json", "r") as f:
    SENTENCES = json.load(f)

# XOR then BASE64
def weak_encrypt(message, key):
    encrypted = ''.join([chr(ord(x) ^ ord(key)) for x in message])
    encoded = base64.b64encode(bytes(encrypted, "UTF-8"))
    return encoded

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        self.countCorrect = 0
        self.key = random.choice(CHARS)

    def run(self):
        print("Connection from : ", self.clientAddress)
        if ipThreads[self.clientAddress[0]] >= 5:
            self.csocket.send(bytes("Too many threads.\n Please stop before I ban you thanks.\n", 'UTF-8'))

            # Close connection
            self.csocket.send(bytes("Server disconnected\n", 'UTF-8'))
            print("Client at ", clientAddress, " disconnected...")

            # Close file descriptor
            self.csocket.close()
            threads.remove(self)
            ipThreads[self.clientAddress[0]] -= 1
            return

        self.csocket.send(bytes("Quick decode these messages NOW!\n", 'UTF-8'))

        # When 10 is correct
        while self.countCorrect < REQUIRED_CORRECT:
            try:
                # Send random encrypted message
                randomMessage = random.choice(SENTENCES)

                print(randomMessage)
                self.csocket.send(
                    bytes(f"{weak_encrypt(randomMessage , self.key).decode('UTF-8')}\n", "UTF-8"))

                # Change key after encrypting message
                self.key = random.choice(CHARS)

                data = self.csocket.recv(2048)
                # Take out newline from message
                msg = data.decode().rstrip()
                # If message empty then we close connection
                if not msg:
                    break

                if msg == randomMessage:
                    self.csocket.send(bytes("That looks right!\n", "UTF-8"))
                    self.countCorrect += 1
                else:
                    # When wrong we disconnect
                    self.csocket.send(
                        bytes("That doesn't look right...\n", 'UTF-8'))
                    break
            except socket.timeout:
                break

        # Check how many correct
        if self.countCorrect < REQUIRED_CORRECT:
            self.csocket.send(
                bytes("You're fired!\n", 'UTF-8'))
        else:
            self.csocket.send(
                bytes(f"Very nice! Here's your medal: {FLAG}\n", "UTF-8")
            )

        # Close connection

        self.csocket.send(bytes("Server disconnected\n", 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")

        # Close file descriptor
        self.csocket.close()
        threads.remove(self)
        ipThreads[self.clientAddress[0]] -= 1

    def forceStop(self):
        # Close connection. This is used to interrupt recv.
        # SHUT_RD is used to stop reading but allow writing to file descriptor
        self.csocket.shutdown(socket.SHUT_RD)




print(f"Server started on {LISTENING}:{PORT}")

try:
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()

        # Count threads for address
        if clientAddress[0] not in ipThreads:
            ipThreads[clientAddress[0]] = 1
        else:
            ipThreads[clientAddress[0]] += 1
        print(ipThreads)

        clientsock.settimeout(20)
        newthread = ClientThread(clientAddress, clientsock)
        threads.append(newthread)
        newthread.start()
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    for t in threads:
        t.forceStop()
    server.close()
