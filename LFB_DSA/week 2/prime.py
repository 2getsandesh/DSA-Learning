n = int(input("enter a num"))
flag = 0
for i in range(2,n//2+1):
    if n%i==0: flag = 1
if flag==0: print("PRIME")
else: print("NoT PRIME")
