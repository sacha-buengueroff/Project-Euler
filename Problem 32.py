productos = set()

chequeo = set('123456789')

for i in range(1,10):
    for j in range(1000,10000):
        s = str(i)+str(j)+str(i*j)
        if len(s) == 9 and set(s) == chequeo:
            productos.add(i*j)
        elif len(s) > 9:
            break

for i in range(10,100):
    for j in range(100,1000):
        s = str(i) + str(j) + str(i * j)
        if len(s) == 9 and set(s) == chequeo:
            productos.add(i * j)
        elif len(s) > 9:
            break


print(sum(productos))
