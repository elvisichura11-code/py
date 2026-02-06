#a python program that prompts a user to rnter a number and checks whether it is even or odd

number=int(input("Enter number:"))

if number == 0:
     print("number is neutral")

elif number%2==0:
    print(number,"is an even number")
else:
     print(number,"is an odd number")