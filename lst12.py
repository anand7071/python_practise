
import itertools
s,m=input().split()

b,l=input().split()
s=int(s)
m=int(m)
b=int(b)
l=int(l)

s=[s,m]
b=[b,l]
for i in itertools.product(s,b):
    print(i,end=" ")
    