"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primeFactors(n):
    prime_factors = []
    while n%2 == 0:
        prime_factors.append(2)
        n = n/2
    for i in range(3, int(n**0.5)+1, 2):
        while n%i == 0 and isPrime(i):
            prime_factors.append(i)
            n = n/i
    return prime_factors

print(primeFactors(600851475143))
print(primeFactors(20))
