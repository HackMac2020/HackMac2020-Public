To solve the challenge, the competitor should start off by analysing all files provided and carefully check their metadata. this will give them several clues. Clues such as :

File crack_me.exe being a PNG image file instead of a Windows executable file. They will discover that the PNG file is actually a dissassembly of a C executable code . This image file contains the register information of a small part of a C execuatble file.

After analysis the metadata of Spring.jpg, the competitor should discover a clue that states out what they would have to do for the next steps. Which is that they need to find my hidden password, the password format and also what sort of encryption has been used on the secret.bin file and how they would have to access it.

Next up the competitor should attempt at uncovering the hidden information in the Spring.jpg image file. They should attempt at using several steganalysis techniques to uncover the hidden text file in the Spring.jpg image file. Ideally they should employ stegcracker to do this using the rock-you.txt dictionary of passwords. The passwords used to encrypt the hidden text file are up the file so this shouldnt take much time as the program runs sequentially.

After uncovering the text file, the competitor will discover that it contains a function dissassembly of a C executable. Now together with the first dissassebly containing the register information they should be able to uncover the hidden password. To uncover this password they would need to be familiar with C and assembly language. However, this would not have to be to a deeper level. They should perform several techniwues of stepping through the code in a manner that does not lead to a bomb explosion, but rather to the end of the function where it returns. They will have to uncover 3 numbers which they would need to use as input to do this.

The competitor is also ideally expected to run stegcracker on the .wav file which contains a hidden .java file which is to be used to decrypt secret.bin.

After this the competitor simply has to use the hints and information gathered to fill in 3 lines of code which have been explicitly pointed out in decrypt.java to make the code executable. After inputting these lines of code which are:

128 for the key size and and AES/ECB/.... which specifies the encryption / decryption style.

The competitor should be able to compile the file and decrypt secret.bin to uncover the flag


The final pin to decrypt secret.bin is "0 22 15"
Whilst the password to decrypt the hidden information in Spring.jpg is "impossible"
The password to decrypt the hidden information in Changes- 2PAC.wav file is "iloveu"