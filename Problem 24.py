digitos = ["0","1","2","3","4","5","6","7","8","9"]

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

list = []
for p in permutation(digitos):
    list.append(p)
list.sort()
print(list[999999])

