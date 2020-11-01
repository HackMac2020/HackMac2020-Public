# Writeup

In order to complete this challenge, competitors must analyse the encryption script and identify it correctly as a simple XOR operation.

Once the encryption scheme is identified, a known plaintext attack must be performed in order to retrieve the secret key.

```
bash-4.4$ python3 secureEncrypt.py -i readme_encrypted.txt -o /tmp/out -k "$(cat readme.txt)" && cat /tmp/out
**********************************
*          DOING TOTALLY,        *
*  UNCRACKABLE & SECURE THINGS   *
**********************************
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |   ~~   HACKMAC 2020! ~~  |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Encrypting...
ClaudeSoainonClauceShannonClaudbShanionClaudeShannonClauceShannonClaudeShannonClaudeShan-bash-4.4$
```

This secret key is the root account's password and can be used to retrieve FLAG.txt located in /root.

```
bash-4.4# id
uid=0 gid=0 groups=0
bash-4.4# cat FLAG.txt
hackmac{Should_have_had_confusion_and_diffusion}
```
