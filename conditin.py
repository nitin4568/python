# Take input from user
marks = int(input("Enter the marks: "))

# Check grade
if marks >= 90:
    grade = "A"
elif marks > 50:
    grade = "B"
else:
    grade = "C"

# Print result
print("Your grade is:", grade)