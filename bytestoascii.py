data = [b'\x1b\x11\x02\x15\x1d\x1a',b'\x1b',b'\x12',b'\x06\x06\x1b',b'\x1c\x0e',b'\x11\x0c',b'\x14',b'\x11\x1b',b'\x1d',b'\x1b\x11\x01']

for d in data:
	x = int.from_bytes(d,byteorder='big')
	print(x)
	digits = []
	while x:
		digits.append(int(x % 256))
		x//=256
	for i in range(len(range(x)) - len(digits)):
	    digits.append(0)

	character = []
	for i in digits:
	    character.append(chr(i))
	print(''.join(character))