vec1 = [0xc5, 0xe6, 0x61, 0x87]
vec2 = [0x01, 0x00, 0x00, 0x00]

index = 0

while index < 4:
    
    print(hex(vec1[index] ^ vec2[index]), end= " ")
    index+=1


