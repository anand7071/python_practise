a = [11,22,11,22,11,1,12,3,4,55,6]
a.sort()
#print(a)
m=[]
d = {}
for i in range(len(a)):
    m.append(a.count(a[i]))
#for i in range(len(a)):    
    #print(str(a[i])+":"+str(m[i]))
for i in range(len(a)):
    d.update({a[i]:m[i]})
print(d)