list = []
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        list.append(i)
l = len(list)
print(list)
resultado = 0
for i in range(0,l):
    resultado = resultado + list[i]
print(resultado)