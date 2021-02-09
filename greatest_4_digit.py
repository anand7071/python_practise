a=[]
for i in range(5):
    a.append(int(input("enter the "+str(i)+" number")))
a.sort()
print(a[-1])