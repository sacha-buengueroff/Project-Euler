"""
Euler discovered the remarkable quadratic formula:

It turns out that the formula will produce 40 primes for the consecutive integer values . However, when is divisible by 41, and certainly when

is clearly divisible by 41.

The incredible formula
was discovered, which produces 80 primes for the consecutive values

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

, where and

where
is the modulus/absolute value of
e.g. and

Find the product of the coefficients,
and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
"""

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primesUntil(n):
    primes = []
    for i in range(2,n+1):
        if isPrime(i):
            primes.append(i)
    return primes

lista = []
for a in range(-999,1000):
    for b in primesUntil(1000):
        i = 0
        while (isPrime(i**2+a*i+b)):
            i += 1
        lista.append([a,b,i])
print(lista)
lista2 = []
for terna in lista:
    lista2.append(terna[2])
n = max(lista2)
print(n)
for terna in lista:
    if terna[2] == n:
        print((terna[0],terna[1]))

for i in range(0,79):
    print((i**2-61*i+971),isPrime(i**2-61*i+971))
