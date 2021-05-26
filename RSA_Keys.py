#Creating Public and Secret Keys with the RSA Algorithm
import random
import math
from math import gcd

#generate 2 random prime numbers with mills equation
'''C = 1.3063778838630806904686144926
n = random.randint(1,5)
m = random.randint(1,5)
p = math.floor(C**(3**n))
q = math.floor(C**(3**m))'''

pn = []

import math

def primeNr(interval):
    print("Prime numbers from 2 to ", interval)

    for i in range(2, interval + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            pn.append(i)

primeNr(500)

p = random.choice(pn)
q = random.choice(pn)
print(p)
print(q)


#solve for N
N = p * q
print("N:", N)

#solve for phi(N)
phiN = (p-1)*(q-1)
print("phi(N):", phiN)

#solve for e given 1<e<phiN and e is coprime w N and phi(N)

'''coprimes = []
def solveCoprime():
    for e in range(2, phiN):
        if gcd(e, phiN) == 1 and gcd(e, N) == 1:
            coprimes.append(e)'''

#(solveCoprime())
e = 3 #(random.choice(coprimes))

print("e:", e)

print("Public Key:", "(", e, "-", N, ")")

#de % phi(N) = 1

solveD = []
def calcD():
    for i in range(2,10000000):
        if (i*(e))%phiN == 1:
            solveD.append(i)
calcD()

d = solveD[0]

print("Private Key: (", d, "-", N, ")")



