# Permutation and translation tables for DES
__pc1 = [56, 48, 40, 32, 24, 16,  8,
0, 57, 49, 41, 33, 25, 17,
9,  1, 58, 50, 42, 34, 26,
18, 10,  2, 59, 51, 43, 35,
62, 54, 46, 38, 30, 22, 14,
6, 61, 53, 45, 37, 29, 21,
13,  5, 60, 52, 44, 36, 28,
20, 12,  4, 27, 19, 11,  3
]

# number left rotations of pc1
__left_rotations = [
1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# permuted choice key (table 2)
__pc2 = [
13, 16, 10, 23,  0,  4,
2, 27, 14,  5, 20,  9,
22, 18, 11,  3, 25,  7,
15,  6, 26, 19, 12,  1,
40, 51, 30, 36, 46, 54,
29, 39, 50, 44, 32, 47,
43, 48, 38, 55, 33, 52,
45, 41, 49, 35, 28, 31
]

# initial permutation IP
__ip = [57, 49, 41, 33, 25, 17, 9,  1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7,
56, 48, 40, 32, 24, 16, 8,  0,
58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6
]

# Expansion table for turning 32 bit blocks into 48 bits
__expansion_table = [
31,  0,  1,  2,  3,  4,
3,  4,  5,  6,  7,  8,
7,  8,  9, 10, 11, 12,
11, 12, 13, 14, 15, 16,
15, 16, 17, 18, 19, 20,
19, 20, 21, 22, 23, 24,
23, 24, 25, 26, 27, 28,
27, 28, 29, 30, 31,  0
]

# S1
__sbox1 = [ 
[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

#S2
__sbox2 = [
[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

# S3
__sbox3 =[ 
[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
]

# S4
__sbox4 = [
[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

# S5
__sbox5 = [
[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

# S6
__sbox6 = [
[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

# S7
__sbox7 = [
[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

# S8
__sbox8 = [
[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]



# 32-bit permutation function P used on the output of the S-boxes
__p = [
15, 6, 19, 20, 28, 11,
27, 16, 0, 14, 22, 25,
4, 17, 30, 9, 1, 7,
23,13, 31, 26, 2, 8,
18, 12, 29, 5, 21, 10,
3, 24
]

# final permutation IP^-1
__fp = [
39,  7, 47, 15, 55, 23, 63, 31,
38,  6, 46, 14, 54, 22, 62, 30,
37,  5, 45, 13, 53, 21, 61, 29,
36,  4, 44, 12, 52, 20, 60, 28,
35,  3, 43, 11, 51, 19, 59, 27,
34,  2, 42, 10, 50, 18, 58, 26,
33,  1, 41,  9, 49, 17, 57, 25,
32,  0, 40,  8, 48, 16, 56, 24
]

##############################################
# Performs a XOR of two bit strings that have
# the same length. E.g., "1100" and "1111"
# @param fStr - the first string
# @param sStr - the second string
# @return - the string reprenting the
# XORing of bits of two strings
#############################################
def strXOR(fStr, sStr):
	
	# Make sure the strings are the same length	
	if len(fStr) != len(sStr):
		print("strXOR: the strings are not of the same length")
		exit(1)

	# The result
	result = ""
	
	# The index for performing XOR
	index = 0	
		
	# Compute the XOR
	while index < len(fStr):
		
		# Compare the two bits and do XOR
		if(fStr[index] == sStr[index]):
			result += "0"
		else:
			result += "1"
		
		index += 1

	return result
		

##########################################
# Converts an integer into a 4-bit string
# if possible.
# @param myInt - the integer
# @return - the 4-bit string
##########################################
def intTo4bitBin(myInt):

	# Convert to a binary string
	binary = bin(myInt)

	# Remove the first two characters ("0b")
	binary = binary[2:]

	# Make sure the number can be converted into a 4-bit quantity
	if len(binary) > 4:
		print("intTo4bitBin(): error, cannot convert ", myInt, " into a 4-bit number")
		exit(1)

	# Prepend 0's if necessary
	while len(binary) < 4:
		binary = "0" + binary

	return binary

##############################################
# Splits a 48-bit string into 8 6-bit groups
# @param bitString - the bit string
# @return - a list of 8-bit strings
##############################################
def split48BitString(bitString):
	
	# Split the string	
	group1 = bitString[:6]
	group2 = bitString[6:12]
	group3 = bitString[12:18]
	group4 = bitString[18:24]
	group5 = bitString[24:30]
	group6 = bitString[30:36]
	group7 = bitString[36:42]
	group8 = bitString[42:48]

	# return a result
	return [group1, group2, group3, group4, group5, group6, group7, group8]

###########################################
# Rotates a string to the left by the provided 
# amount
# @param str - the string to rotate
# @param rotAmount - how much to rotate
###########################################
def rotateStringLeft(str, rotAmount):

	# Rotate the string
	return str[rotAmount:] + str[:rotAmount]

##############################################
# Performs a substituion on DES IP, PC1, PC2,
# E, and P tables
# @param table - the table
# @param inputStr - the input string of bits
# (e.g., 1100000011101101110100011111000111111010101001011101100010010001)
# @return - the resulting substituion
##############################################
def doTable(table, inputStr):
	pass

##############################################################
# Performs an S-Box substituion
# @param sbox - the sbox table to use
# @param inputStr -  the 6 digit binary string (e.g., 011001)
##############################################################
def doSbox(sbox, inputStr):
	pass

###############################################################
# The round function
# @param rhs - the right-hand half of the plaintext
# @param roundKey - the round key
# @return - the transformed right-hand 
##############################################################
def roundFunction(rhs, roundKey):
	pass

##############################################################
# Uses the user key in order to derive the keys for each round
# @param key - the user key
# @return - a list of keys representing a key for each round
############################################################### 
def deriveAllRoundKeys(key):

	
