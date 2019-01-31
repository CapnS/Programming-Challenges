number = 72
remainders = []
while number != 0:
    number, remainder = divmod(number, 16)
    remainders.append(remainder)
remainders = remainders[::-1]
hexadecimal = "0x"
for x in remainders:
    hexadecimal = hexadecimal + str(x)
print(hexadecimal)