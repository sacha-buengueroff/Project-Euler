for x in range(1,1000):
    for y in range((x+1),1000):
        if ((x*x)+(y*y))==((1000-x-y)**2):
            a=x
            b=y
            c=1000-x-y
            break
print(a,b,c)
print(a*b*c)