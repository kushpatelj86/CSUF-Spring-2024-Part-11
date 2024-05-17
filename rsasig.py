from Cryptodome.PublicKey import RSA
from Cryptodome.Signature.pkcs1_15 import PKCS115_SigScheme
from Cryptodome.Hash import SHA256
import binascii
import Cryptodome.Signature.pkcs1_15 


# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
print(keyPair)
# Get just the public key
justPubKey = keyPair.publickey()
print(justPubKey)

# The good message
msg = b'hello'

# The tempered message
msg1 = b'tempered'

# Compute the hashes of both messages
hash = SHA256.new(msg)
hash1 = SHA256.new(msg1)

# Sign the hash
sig1 = Cryptodome.Signature.pkcs1_15.new(keyPair)
signature = sig1.sign(hash)

##################### On the arrival side #########################

# Note, we will have to take the decrypted message, hash it and then provide the hash and the signature to the 
# verify function

verifier = Cryptodome.Signature.pkcs1_15.new(justPubKey)

# If the verification succeeds, nothing is returned.  Otherwise a ValueError exception is raised
# Let's try this with the valid message
try:
    verifier.verify(hash, signature)
    print("The signature is valid!")
except ValueError:    
    print("The signature is not valid!")

hash = hash1

# Now with the invalid message
try:
    verifier.verify(hash1, signature)
    print("The signature is valid!")
except ValueError:    
    print("The signature is not valid!")
