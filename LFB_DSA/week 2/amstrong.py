n = int(input("Enter the number"))
x = 0
numstr = str(n)
x = sum(int(i)**3 for i in numstr)
if x == n: print("Yes")
else: print("No")

'''while temp>0:
    rem = temp%10
    x += rem**3
    temp=temp//10'''