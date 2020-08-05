"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for x in range(1,1000):
    for y in range((x+1),1000):
        if ((x*x)+(y*y))==((1000-x-y)**2):
            a=x
            b=y
            c=1000-x-y
            break
print(a,b,c)
print(a*b*c)
