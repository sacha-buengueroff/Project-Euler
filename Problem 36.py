def toBin(n):
    x = bin(n)
    x = str(x)
    x = x[2:]
    x = int(x)
    return x

def reverse(n):
    string = str(n)
    dadoVuelta = string[::-1]
    resultado = int(dadoVuelta)
    return resultado

tuplas = []
tuplasReversa = []
for i in range(1,1000000):
    binario = toBin(i)
    tuplas.append([i, binario])

for tupla in tuplas:
    tuplasReversa.append([reverse(tupla[0]), reverse(tupla[1])])

resultado = 0
l = len(tuplas)
for i in range(0,l):
    if tuplas[i] == tuplasReversa[i]:
        resultado += tuplas[i][0]

print(resultado)