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