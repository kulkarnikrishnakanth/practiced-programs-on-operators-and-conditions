
num = int(input("enter a 4 digit number: "))
number = str(num)
if len(number) == 4:
    print(number[::-1])
else:
    print("you did not entered 4 digit number")
