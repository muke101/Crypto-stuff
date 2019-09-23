import re

data = open('Decode.txt', 'r')

output = open('Decode2.txt', 'w')

output.write(re.sub('-','+', re.sub('_', '/', data.read())))
