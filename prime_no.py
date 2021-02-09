num = int(input("enter the no you want to check :: "))
prime = True
for i in range(2, num):
    if (num%i==0):
        prime= False
    break
if prime:
    print("the no is prime")
else : 
    print("the no is not prime")