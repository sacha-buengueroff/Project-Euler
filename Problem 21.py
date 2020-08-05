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

