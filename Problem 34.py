"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(n):
    res = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    for i in range(1,n+1):
        res *= i
    return res


total = 0
for i in range(3,2550000):
    string = str(i)
    suma = 0
    for numero in string:
        suma += factorial(int(numero))
    if suma == i:
        total += i
print(total)
