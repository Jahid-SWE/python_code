Bytes = [15,161,122,111] # bytes also contains valo between 0 and 255
b = bytes(Bytes)
m = bytearray(Bytes)
m[0]= 90
print(type(b))
print(m[0])