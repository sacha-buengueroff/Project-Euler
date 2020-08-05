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
