def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

listaDePrimos = [2]
num = 3
while len(listaDePrimos) <= 10000:
    if isPrime(num):
        listaDePrimos.append(num)
        num = num + 2
    else:
        num = num + 2
print(listaDePrimos[10000])