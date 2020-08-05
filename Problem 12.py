import math
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n%i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def number_divisors(n):
    primeFactors = prime_factors(n)
    l = len(primeFactors)
    cantidad = []
    counter = 2
    for i in range(0,l-1):
        if primeFactors[i] == primeFactors[i+1]:
            counter += 1
        else:
            cantidad.append(counter)
            counter = 2
    cantidad.append(counter)
    l = len(cantidad)
    resultado = 1
    for i in range(0,l):
        resultado = resultado * cantidad[i]
    return resultado

contador = 1
num = 1
while number_divisors(num) <= 500:
    contador = contador + 1
    num = num + contador
    print(num)

