"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

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
