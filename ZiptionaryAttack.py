import zipfile
import sys

target = zipfile.ZipFile(sys.argv[1], 'r')

wordlist = open(sys.argv[2], 'rb').readlines()

for name in target.namelist():
	for pwd in wordlist:
		try:
			print(pwd.strip('\n'))
			target.read(name, pwd=pwd.strip())
			print("Password for "+name+": "+pwd)
			break
		except:
			pass
