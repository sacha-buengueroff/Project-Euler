def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def truncableDeIzquierda(n):
    string = str(n)
    esTruncable = True
    l = len(string)
    for i in range(0,l):
        if not isPrime(int(string[i:])):
            esTruncable = False
            break
    return esTruncable

def truncableDeDerecha(n):
    string = str(n)
    esTruncable = True
    l = len(string)
    for i in range(0,l):
        if not isPrime(int(string[0:l-i])):
            esTruncable = False
            break
    return esTruncable



lista =[]
for i in range(2,1000000):
    string = str(i)
    l = len(string)
    string2 = string[1:l]
    if len(string) > 2 and ("0" in string2 or "2" in string2 or "4" in string2 or "5" in string2 or "6" in string2 or "8" in string2):
        continue
    if truncableDeDerecha(i) and truncableDeIzquierda(i):
        lista.append(i)

print(lista)
Xs = [2,3,5,7]
x = sum(Xs)
y = sum(lista)
resultado = y - x
print(resultado)