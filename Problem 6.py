"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumOfSquares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2
    return sum

def squareOfSum(n):
    suma = 0
    for i in range(1,n+1):
        suma = suma + i
    suma = suma**2
    return suma

print(abs(squareOfSum(100)-sumOfSquares(100)))
