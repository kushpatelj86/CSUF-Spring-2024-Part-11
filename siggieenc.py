from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto import Random
import base64
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import binascii
import Crypto.Signature.pkcs1_15 
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Cipher import AES

# The private key
prKey = None

# THe public key
puKey = None

# Load the public key
with open ("private.pem", "rb") as prv_file:
	
	contents = prv_file.read()
	prKey = RSA.importKey(contents)


# Load the public key
with open ("public.pem", "rb") as pub_file:
	contents = pub_file.read()
	puKey = RSA.importKey(contents)

###############################################
# Returns the signature of the message
# @param msg - the message
# @return - the message with the signature
# The message begins with the three bytes 
# indicating the length of the signature
# that is appended to the end of the message
# The format is
# |3-byte signature length||Message||Signature|
###############################################
def addSignature(msg, privKey):

	# Compute the hash of the message
	hash = SHA256.new(msg.encode())
	
	# The signer class
	signer = Crypto.Signature.pkcs1_15.new(privKey)
	
	# The signature
	signature = signer.sign(hash)
	
	# Get the length of the signature
	sigLen = len(signature)

	# Convert the length to string and to bytes
	sigLenBytes = str(sigLen).encode()

	# Prepad with the three bytes
	while len(sigLenBytes) < 3:
		
		sigLenBytes = b'0' + sigLenBytes 

	return sigLenBytes + msg.encode() + signature


####################################################
# Extracts a message from the signed message
# verifies the digital signature, and returns
# the original message
# @param msg - the original message on success and None
# on faliure
# |3 byte signature length header|message|signature
###################################################

def extractMsgAndVerifySig(msg, pubKey):
	
	# The return value
	retVal = None
	
	# Get the leading three bytes indicating the
	# signature length
	sigLen = int(msg[:3])
	
	# Get the message
	justMsg = msg[3:len(msg) - sigLen]
	
	# Get the signature
	signature = msg[len(msg) - sigLen:]
	
	# Compute the hash of the message
	hash = SHA256.new(justMsg)
		
	# The veification class
	verifier = Crypto.Signature.pkcs1_15.new(pubKey)
	
	# Verify the signature
	try:
		verifier.verify(hash,signature)
		
		# Save the return message
		retVal = justMsg
		
		print("The RSA signature is valid!");
	# The verification failed
	except ValueError:
		print("Verification failed")
	
	
	return retVal


msg = "hello"

# Sign the message
signed = addSignature(msg, prKey)

print(len(signed))
print(len(pad(signed, 16)))

# The 16-byte key for AES
key = "you got this :-)"

cipher = AES.new(key.encode(), AES.MODE_ECB)

# Pad the message to 16 bytes and encrypt
signedAndEncrypted = cipher.encrypt(pad(signed, 16))



###############################################################
# Now let's decrypt and verify
decrypted = cipher.decrypt(signedAndEncrypted)

# Remove the padding
unpadded = unpad(decrypted, 16)

# Verify the signature and extract the message
msg = extractMsgAndVerifySig(unpadded, puKey)

# Print the message if the signature was succeffu
if msg:
    print(msg)


