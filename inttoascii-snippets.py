#I2OSP:
digits = []
x = int.from_bytes(d,byteorder='big') #may or may not need
while x:
	digits.append(int(x % 256))
	x//=256
for i in range(len(range(x)) - len(digits)):
    digits.append(0)

character = []
for i in digits:
    character.append(chr(i))
print(''.join(character))

#OS2IP
xLen = len(X)
X = X[::-1]
x = 0
for i in range(xLen):
    x += X[i] * 256^i
return x

#bitwise one liners that do the same as I2OSP and OS2IIP:
#num2bytes
bytes(data >> (8 * i) & 0xff for i in range(size))
#bytes2num
sum(x << (8 * i) for i, x in enumerate(data))

#bytes to ascii
chr(int.from_bytes(d,byteorder='big'))
