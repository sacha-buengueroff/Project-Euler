fibonacci = [1, 2]
add = 0
while add <= 4000000:
    l = len(fibonacci)
    add = fibonacci[l-1] + fibonacci[l-2]
    if add <= 4000000:
        fibonacci.append(add)
print(fibonacci)
resultado = 0
l = len(fibonacci)
for i in range(0,l):
    if fibonacci[i]%2 == 0:
        resultado = resultado + fibonacci[i]
print(resultado)