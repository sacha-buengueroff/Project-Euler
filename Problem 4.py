"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse(s):
    return s[::-1]

def isPalindrome(n):
    n = str(n)
    N = reverse(n)
    if n == N:
        return True
    return False

palindromes = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if isPalindrome(i*j):
            palindromes.append(i*j)
num = max(palindromes)
print(num)





