#!/usr/bin/python

import bcrypt

# The password to hash
password = b'hello'

# Generate the salt value
salt = bcrypt.gensalt()

print("The salt is ", salt)

# Hash the password
hashed = bcrypt.hashpw(password, salt)

print("The hash is: ", hashed)

# Verify if the password matches
if bcrypt.checkpw(password, hashed):
    print("Passwords match!")
else:
    print("Passwords DO NOT match!")

