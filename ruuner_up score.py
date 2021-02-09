arr=[]
for _ in range(int(input('enter the size of array \t'))):
    name = input("enter the name \t")
    score = float(input("enter the no. \t" ))
    arr.append([name,score])
arr.sort()
print(arr)
print(arr[1][1])