n=1
while(n!=0):
    n = int(input("Enter 1,2,3,4,0"))
    if n==0: break
    a = int(input("First num"))
    b = int(input("sec num"))

    if n==1: print(a+b)
    elif n==2: print(a-b)
    
print("Terminated")