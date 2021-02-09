n, x = map(int,input().split())
a=[]
for _ in range(x):
    a.append(map(float, input().split()))
for i in zip(*a):
    print(sum(i)/len(i))