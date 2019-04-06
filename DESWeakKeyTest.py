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
semiWeakKeys = [(b'\x011F011F010E010E',b'\x1F011F010E010E01'), (b'\x01E001E001F101F1',b'\xE001E001F101F101'), (b'\x01FE01FE01FE01FE',b'\xFE01FE01FE01FE01'), (b'\x1FE01FE00EF10EF1',b'\xE01FE01FF10EF10E'), (b'\x1FFE1FFE0EFE0EFE',b'\xFE1FFE1FFE0EFE0E'), (b'\xE0FEE0FEF1FEF1FE',b'\xFEE0FEE0FEF1FEF1')]

for key in weakKeys:
	data = open('keys.txt', 'rb')
	formatter(decrypt(key, data))

for key1, key2 in semiWeakKeys:
	data = open('keys.txt', 'rb')
	formatter(decrypt(key1, decrypt(key2, data)))
