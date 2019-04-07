import pyDes

def decrypt(key, data):
	data = open('keys.txt', 'rb')
	if len(key) == 1:
		key*=8
	k = pyDes.des(key)
	return k.encrypt(data.read())

def formatter(data):
	x = int.from_bytes(data,byteorder='big')
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

weakKeys = [b'\xff',b'\x00',b'\x01',b'\x10',b'\xE1',b'\x1E',b'\xFE',b'\xEF']
semiWeakKeys = [(b'\x01\x1F\x01\x1F\x01\x0E\x01\x0E',b'\x1F\x01\x1F\x01\x0E\x01\x0E\x01'), (b'\x01\xE0\x01\xE0\x01\xF1\x01\xF1',b'\xE0\x01\xE0\x01\xF1\x01\xF1\x01'), (b'\x01\xFE\x01\xFE\x01\xFE\x01\xFE',b'\xFE\x01\xFE\x01\xFE\x01\xFE\x01'), (b'\x1F\xE0\x1F\xE0\x0E\xF1\x0E\xF1',b'\xE0\x1F\xE0\x1F\xF1\x0E\xF1\x0E'), (b'\x1F\xFE\x1F\xFE\x0E\xFE\x0E\xFE',b'\xFE\x1F\xFE\x1F\xFE\x0E\xFE\x0E'), (b'\xE0\xFE\xE0\xFE\xF1\xFE\xF1\xFE',b'\xFE\xE0\xFE\xE0\xFE\xF1\xFE\xF1')]

for key in weakKeys:
	data = open('keys.txt', 'rb')
	formatter(decrypt(key, data))

for key1, key2 in semiWeakKeys:
	data = open('keys.txt', 'rb')
	formatter(decrypt(bytes(key1), decrypt(bytes(key2), data)))
