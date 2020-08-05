lista = []
for a in range(2,101):
    for b in range(2,101):
        power = a**b
        lista.append(power)
lista = set(lista)
print(len(lista))