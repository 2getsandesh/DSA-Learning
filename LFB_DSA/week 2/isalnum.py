s = str(input("Enter a string"))
new = ''.join(i.lower() for i in s if i.isalnum())
print(new)