# Step 1: Take input as a list of integers
input_list = input("Enter a list of numbers (e.g., 4 2 7 1 3): ")
numbers = [int(num) for num in input_list.split()]


# Step 3: Sort using numpy
import numpy as np
sorted_list = np.sort(numbers)

# Step 4: Print the result
print("Sorted list:", sorted_list)