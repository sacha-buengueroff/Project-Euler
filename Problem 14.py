def collatzList(n):
    num = n
    list = [n]
    while n != 1:
        if n%2 == 0:
            n = n//2
            list.append(n)
        else:
            n = 3*n + 1
            list.append(n)
    l = len(list)
    return(num, l)

lista = []
for i in range(1,1000000):
    lista.append(collatzList(i))
    print(collatzList(i))

l = len(lista)
solucion = (0, 0)
for i in range(0,l):
    if solucion[1] <= lista[i][1]:
        solucion = lista[i]

print(solucion)