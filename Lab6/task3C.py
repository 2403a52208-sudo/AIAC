age = int(input("Enter your age: "))

# Nested if-elif-else conditionals to classify age groups
if age >= 0:
    if age <= 12:
        print(f"Age {age}: Child")
    elif age <= 19:
        print(f"Age {age}: Teen")
    elif age <= 59:
        print(f"Age {age}: Adult")
    else:
        print(f"Age {age}: Senior")
else:
    print(f"Age {age}: Invalid age (must be 0 or positive)")