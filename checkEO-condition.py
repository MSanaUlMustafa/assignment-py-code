num = int(input("Enter a number like 5: "))

count_even = 0
count_odd = 0


for i in range(1, num+1):
    if i%2==0:
        print(f"{i} is even")
        count_even += 1
    else:
        print(f"{i} is odd")
        count_odd += 1

print("Number of odd values", count_odd)
print("Number of even values", count_even)