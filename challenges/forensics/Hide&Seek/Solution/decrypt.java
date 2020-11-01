import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;


public class decrypt{

	private static final String progName = "FileDecryptor";
	private static final int bufSize = 128;

	public static void main(String[] args) {

		BufferedInputStream in = null;
		BufferedOutputStream out = null;
		SecretKeyFactory kf = null;
		KeySpec ks = null;
		byte[] salt = new byte[20];
		SecretKey key = null;
		Cipher cipher = null;
		SecretKeySpec keyspec = null;
		int bytesRead = 0;			
		
		if(args.length != 4) {
			printUsageMessage(); System.exit(1);
		}

		try {
			in = new BufferedInputStream(new FileInputStream(args[1]));
		} catch (FileNotFoundException e) {
			printErrorMessage("Unable to open input file: " + args[1], null);
			System.exit(1);
		}

		try {
			out = new BufferedOutputStream(new FileOutputStream(args[2]));
		} catch (FileNotFoundException e) {
			printErrorMessage("Unable to open output file: " + args[2], e);
			System.exit(1);
		}

		try {
			kf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
		} catch (NoSuchAlgorithmException e) {
			printErrorMessage("No Such Algorithm Exception when creating SecretKeyFactory", e);
			System.exit(2);
		}

		//What Sort of keysize am i using?
		//You need to fill in the 000's
		try {
			ks = new PBEKeySpec(args[3].toCharArray(), salt, 4096, 000); 
			} catch (NullPointerException e) {
				printErrorMessage("Null Pointer Exception when generating KeySpec",e);
				System.exit(2);
			} catch (IllegalArgumentException e) {
				printErrorMessage("Illegal Argument Exception when generating KeySpec",e);
				System.exit(2);
			}

		try {
			key = kf.generateSecret(ks);
		} catch (InvalidKeySpecException e) {
			printErrorMessage("Invalid KeySpec Exception when generating key", e);
			System.exit(2);
		}
		

		byte[] aeskey = key.getEncoded();
		
		//What Encryption or Decryption style am i using here ?
		//You need to fill in the xxx's
		try {
			cipher = Cipher.getInstance("xxx/xxx/PKCS5Padding");
		} catch (NoSuchAlgorithmException e) {
			printErrorMessage("No Such Algorithm Exception when creating main cipher", e);
			System.exit(2);
		} catch (NoSuchPaddingException e) {
			printErrorMessage("No Such Padding Exception when creating main cipher",e);
			System.exit(2);
		}

		int cipherMode = -1;
		char mode = Character.toLowerCase(args[0].charAt(0));
		switch (mode) {
			case 'd' : cipherMode = Cipher.DECRYPT_MODE; break;
			default: printUsageMessage(); System.exit(1);
		}

		try {
			keyspec = new SecretKeySpec(aeskey,"AES");
		} catch (IllegalArgumentException e) {
			printErrorMessage("Illegall Argument Exception when creating SecretKey", e);
			System.exit(2);
		}
		
		try {
			cipher.init(cipherMode, keyspec);
		} catch (InvalidKeyException e) {
			printErrorMessage("Invalid Key Spec",e); System.exit(2);
		} 

		byte[] inputBuffer = new byte[bufSize];
		byte[] outputBuffer = null;
		
		try {
			bytesRead = in.read(inputBuffer);
		} catch (IOException e) {
			printErrorMessage("Error reading input file " + args[1],e); System.exit(1);
		}

		while (bytesRead > 0) {

			try {
				outputBuffer = cipher.update(inputBuffer,0,bytesRead);
				} catch (IllegalStateException e5) {
					printErrorMessage("Illegal Statement Exception found ", e5);
					System.exit(2);
				}

			try {
				out.write(outputBuffer);
			} catch (IOException e) {
				printErrorMessage("Error writing to output file " + args[2],e); System.exit(1);
			}

			try {
				bytesRead = in.read(inputBuffer);
			} catch (IOException e) {
				printErrorMessage("Error reading input file " + args[1],e); System.exit(1);
			}
		}
		
		try {
			outputBuffer = cipher.doFinal();
		} catch (IllegalBlockSizeException e) {
			printErrorMessage("Illegal Block Size when doing final ", e);
			System.exit(1);
		} catch (BadPaddingException e) {
			printErrorMessage("Bad Padding when doing final ", e);
			System.exit(2);
		}
		
		try {
			out.write(outputBuffer);
		} catch (IOException e) {
			printErrorMessage("Error on final write to output file " + args[2],e); System.exit(1);
		}

		try {
			in.close();
			out.close();
		} catch (IOException e) {
			printErrorMessage("Error closing file", e);
		}
	}

	private static void printErrorMessage(String errMsg, Exception e) {
		System.err.println(errMsg);
		if (e != null) 
			System.err.println(e.getMessage());
	}
	//Print Program Usage
	private static void printUsageMessage() {
		System.out.println(progName + "Usage: " + progName + " D infile outfile passphrase");
	}
	
}
