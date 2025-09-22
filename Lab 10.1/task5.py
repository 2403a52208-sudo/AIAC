import time

start_time = time.time()

# Optimized using list comprehension - combines range and squaring in one step
squares = [i**2 for i in range(1, 1000000)]

print(f"Number of squares: {len(squares)}")
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")


"""This script calculates the squares of numbers from 1 to 999,999 using a list 
comprehension,measures the execution time, and prints the number of squares 
computed along with the time taken."""
