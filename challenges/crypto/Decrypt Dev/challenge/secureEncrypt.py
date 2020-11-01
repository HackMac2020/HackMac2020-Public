import sys
import argparse

#interesting choice of algorithm?
def encrypt(text, key):
    b1 = bytearray(text, encoding="utf-8")
    b2 = bytearray(key, encoding="utf-8")
    c = bytearray(len(b1))
    for i in range(len(b1)):
        c[i] = b1[i] ^ b2[i%len(b2)]
    
    return c.decode()

#Hah good one!
def decrypt(ciphertext, key):
    return "Dont be silly!"

parser = argparse.ArgumentParser(description='3ncrypt0R')                                                                                                                                               
parser.add_argument('-i',
                    metavar='InFile',
                    type=str,
                    required=False)

parser.add_argument('-o',
                    metavar='OutFile',
                    type=str,
                    required=False)

parser.add_argument('-k',
                    metavar='Key',
                    type=str,
                    required=False)

parser.add_argument('-d', action='store_true')

args = parser.parse_args()

banner = "**********************************\n"
banner+= "*          DOING TOTALLY,        *\n"
banner+= "*  UNCRACKABLE & SECURE THINGS   *\n"
banner+= "**********************************\n"
banner += " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
banner += " |   ~~   HACKMAC 2020! ~~  |\n"
banner += " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                            
print(banner)
if args.o == None or args.k == None or args.i == None:
    print("Oops, You missed something!")
else:
    if args.d:
        with open(args.i, 'r', encoding='UTF-8') as f:
            data = f.read()

        print("Decrypting??...")
        decrypted = decrypt(data, args.k)
        
        with open(args.o, 'w', encoding='UTF-8') as f:
            f.write(decrypted)
    else:
      
        with open(args.i, 'r', encoding='UTF-8') as f:
            data = f.read()

        print("Encrypting...")
        encrypted = encrypt(data, args.k)

        with open(args.o, 'w', encoding='UTF-8') as f:
            f.write(encrypted)

