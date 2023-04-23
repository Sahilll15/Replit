def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# example usage
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
