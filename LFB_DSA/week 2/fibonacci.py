a,b = 0,1
n = int(input('Enter the no of terms:'))
print(a,b,end=' ')

for i in range(n-2):
    res = a + b
    print(res, end=' ')
    a=b
    b=res

