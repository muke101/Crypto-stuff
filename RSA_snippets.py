#open key
from Crypto.PublicKey import RSA

f = open('key.pub','rb')
key = RSA.importKey(f.read())
print(key.e)
print(key.n)

#multiplicative inverse modulus
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mulinv(a, b):
	"""return x such that (x * a) % b == 1"""
	g, x, _ = egcd(a, b)
	if g == 1:
		return x % bs

#chinese remainder decryption
qinv = mulinv(q,p)
m1 = pow(c,dp,p)
m2 = pow(c,dq,q)
h = (qinv*(m1-m2))%p
m = m2 + h * q

#weiner attack
def cf_expansion(n, d):
	e = []

	q = n // d
	r = n % d
	e.append(q)

	while r != 0:
		n, d = d, r
		q = n // d
		r = n % d
		e.append(q)
	return e

def convergents(e):
	n = []
	d = []

	for i in range(len(e)):
		if i == 0:
			ni = e[i]
			di = 1
		elif i == 1:
			ni = e[i]*e[i-1] + 1
			di = e[i]
		else:
			ni = e[i]*n[i-1] + n[i-2]
			di = e[i]*d[i-1] + d[i-2]

		n.append(ni)
		d.append(di)
		yield (ni, di)