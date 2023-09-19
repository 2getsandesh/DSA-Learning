#Accept two floating-point values from the user and multiply it. Answer should be in 3 decimal point

a=float(input("Enter first number : "))
b=float(input("Enter second number : "))

res=a*b
print(f"The product of {a}*{b} is : {res:.3f}")