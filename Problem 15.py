"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def lattice_paths_of_n(n):
    list2 = []
    my_list = []
    for i in range(1, n+2):
        list2.append(i)
    for i in range(1, n+2):
        my_list.append(list2)
    for i in range(0,n+1):
        for f in range(0,n+1):
            if f == 0 or i == 0:
                my_list[i][f] = 1
            else:
                my_list[i][f] = my_list[i-1][f]+my_list[i][f-1]

    return my_list[n][n]

print(lattice_paths_of_n(4))

#sino es (2*n)!/(n!*n!)
