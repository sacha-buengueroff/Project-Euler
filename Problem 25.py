fibonacci = [1, 1]
digits = 0
add = 0
currentIndex = 2
while digits < 1000:
    l = len(fibonacci)
    add = fibonacci[l-1] + fibonacci[l-2]
    fibonacci.append(add)
    digits = len(str(add))
    currentIndex += 1

print(currentIndex)
