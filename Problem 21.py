"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisores(n):
    divisores = []
    for i in range(1,n):
        if n%i == 0:
            divisores.append(i)
    return divisores

def sumarLista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    return resultado

def d(n):
    resultado = sumarLista(divisores(n))
    return resultado

lista1 = []
for i in range(1,10000):
    x = (i,d(i))
    if x[0] != x[1]:
        lista1.append(x)

def darVuelta(x):
    a = x[0]
    b = x[1]
    return (b,a)

resultado = 0
for par in lista1:
    if darVuelta(par) in lista1:
        print(par)
        resultado = resultado + par[0]

print(resultado)

