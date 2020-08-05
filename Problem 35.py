"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def rotations(n):
    lista = []
    string = str(n)
    l = len(string)
    for i in range(l):
        nuevoString = string[i:] + string[:i]
        lista.append(int(nuevoString))
    return lista

primesAnd0 = []
for i in range(1,1000000):
    if isPrime(i):
        primesAnd0.append(i)
    else:
        primesAnd0.append(0)
#primesAnd0 es la lista de primos del 1 al 999.999, si no es primo, hay un 0.

for prime in primesAnd0:
    string = str(prime)
    if "0" in string or "2" in string or "4" in string or "5" in string or "6" in string or "8" in string:
        primesAnd0[prime-1] = 0
        prime = 0
    if prime != 0:
        rotaciones = rotations(prime)
        todosPrimos = True
        for rotacion in rotaciones:
            if not isPrime(rotacion):
                todosPrimos = False
                break
        if not todosPrimos:
            for rotacion in rotaciones:
                primesAnd0[rotacion-1] = 0
print(primesAnd0)
contador = 1
for numero in primesAnd0:
    if numero != 0:7
        contador += 1

print(contador)




