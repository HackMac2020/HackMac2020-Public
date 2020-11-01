from pwn import *

p = remote('localhost', 1337)
print(p.recv())

p.sendline('COVID-2020_is_coming')
print(p.recv())
p.sendline('VAr2T9Zn%X6h3&2E-but-is this strong enough??')
print(p.recv())
p.sendline('19 76 513')
print(p.recv())
p.sendline('3 @ 1023')
print(p.recv())
p.sendline(p64(0x825a14a))
