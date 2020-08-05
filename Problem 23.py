"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def divisores(n):
    divisores = []
    for i in range(1,int(n/2)+1):
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

abundantes = []
for i in range(12,28124):
    if i < d(i):
        abundantes.append(i)

suma_de_abundantes = [0]*28124

for i in abundantes:
    for j in abundantes:
        if ((i+j) <= 28123):
            if (suma_de_abundantes[i+j] == 0):
                suma_de_abundantes[i+j] = i+j


ans = 0

for i in range(1,28124):
    if i not in suma_de_abundantes:
       ans = ans + i
       print(ans)
