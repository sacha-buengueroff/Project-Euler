def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def listaDePrimos(n):
    lista = [2]
    for i in range(3,n,2):
        if isPrime(i):
            lista.append(i)
    return lista

def sumaLista(lista):
    l = len(lista)
    resultado = 0
    for i in range(0,l):
        resultado = resultado + lista[i]
    return resultado

print(sumaLista(listaDePrimos(2000000)))