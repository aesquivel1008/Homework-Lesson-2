number=int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number==0:
    print("the number is zero")
else:
    print("The number is negative")

one=int(input("Enter a number: "))
two=int(input("Enter a number: "))
three=int(input("Enter a number: "))
if one>two and one>three:
    print(f"{one} is the greates number")
elif two>one and two>three:
    print(f"{two} is the greates number")
else:
    print(f"{three} is the greates number")

if one<two and one<three:
    print(f"{one} is the lowest number")
elif two<one and two<three:
    print(f"{two} is the lowest number")
else:
    print(f"{three} is the lowest number")

year=int(input("PLease enter a year: "))
if year % 4==0:
    print("This is a leap year")
else:
    print("This is not a leap year")



