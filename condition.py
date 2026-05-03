age = int(input("Enter the age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("You can vote")
else:
    print("You can't vote")