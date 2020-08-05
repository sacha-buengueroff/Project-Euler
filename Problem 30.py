total = 0
for i in range(2,355000):
    string = str(i)
    suma = 0
    for numero in string:
        suma += (int(numero))**5
    if suma == i:
        total += i
        print(suma)
print(total)