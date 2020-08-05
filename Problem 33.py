divisiones = []
for i in range(10,100):
    for j in range(i+1,100):
        r = i/j
        iEnString = str(i)
        jEnString = str(j)
        if jEnString[1] != "0":
            if iEnString[0] == jEnString[0] and (int(iEnString[1])/int(jEnString[1])) == r:
                divisiones.append([i,j])
            elif iEnString[1] == jEnString[0] and (int(iEnString[0])/int(jEnString[1])) == r:
                divisiones.append([i,j])
        elif jEnString[0] != "0":
            if iEnString[1] == jEnString[1] != "0" and (int(iEnString[0])/int(jEnString[0])) == r:
                divisiones.append([i,j])
            elif iEnString[0] == jEnString[1] and (int(iEnString[1])/int(jEnString[0])) == r:
                divisiones.append([i,j])

numerador = 1
denominador = 1
for numeros in divisiones:
    numerador *= numeros[0]
    denominador *= numeros[1]
print(numerador/denominador)
