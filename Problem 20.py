def factorial(n):
    fact = 1
    if n > 2:
        for i in range(1,n+1):
            fact = fact * i
    return fact

def sumaDigitos(n):
    num = str(n)
    resultado = 0
    for digit in num:
        resultado = resultado + int(digit)
    return resultado

print(sumaDigitos(factorial(100)))