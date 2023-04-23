def arithmetic_operations(a, b):
  return a + b, a - b, a * b, a / b


# example usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
add, sub, mul, div = arithmetic_operations(x, y)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
