first=int(input("Enter your first number:"))
second=int(input("Enter your second number:"))
third=int(input("Enter your third number:"))


if first>second and first>third:
    print(first,"is the greatest number")

elif second>first and second>third:
    print(second,"is the greatest number")

else:
    print(third,"is the greatest number")    