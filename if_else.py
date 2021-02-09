n = int(input("enter your no."))
if n%2!=0:
   print('Weird')
else:
    if n in range(3,6):
        if n%2==0:
            print('Not Weird')
    elif n in range(6,21):
        if n%2==0:
            print('Weird')
    else:
        if n%2==0:
            print('Not Weird')        
            
