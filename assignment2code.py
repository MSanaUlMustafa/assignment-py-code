# Step 1: Accept list of integers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Step 2: Loop with break/continue
for num in numbers:
    if num == 20:
        print("Breaking at 20")
        break
    elif num > 10:
        print(f"Skipping {num}")
        continue
    print(num)
else:
    print("Loop ended naturally")  # Executes if loop completes without break