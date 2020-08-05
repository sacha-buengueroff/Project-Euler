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
