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





