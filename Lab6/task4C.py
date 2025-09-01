n = int(input("Enter a number: "))

# Method 1: Using for loop
total_for = 0
for i in range(1, n + 1):
    total_for = total_for + i

# Method 2: Using while loop
total_while = 0
i = 1
while i <= n:
    total_while = total_while + i
    i = i + 1

# Show results
print(f"Sum of first {n} numbers:")
print(f"For loop: {total_for}")
print(f"While loop: {total_while}")
