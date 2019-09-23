import subprocess
import sys

fileName = str(sys.argv[1]) 

for hashfunction in ['md4', 'md5', 'mdc2', 'rmd160', 'sha', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
    digest = subprocess.check_output(['openssl', hashfunction, fileName]).decode("utf-8").split()[-1]
    if digest in open(sys.argv[2], 'rb'):
        print('match: '+hashfunction)


