# Swapping with the help of third variable 
print("With the help of third Variable")

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))
temp = 0

tmep = var1
var1 = var2
var2 = tmep

print("After swapping First number:", var1)
print("After swapping second number:", var2)

print()

# Swapping without third variable
# With the help of addition and subtraction
print("Without third Variable")

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a - b
b = a + b
a = b - a

print("a: ", a)
print("b: ", b)
