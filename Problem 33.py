"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

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
