# Write a Python program to find the largest number in a list using a lambda function.
# The program should prompt the user to enter a list of comma-separated numbers and then use a lambda function to find the largest number in the list. The largest number should then be displayed to the user.

list = input("Enter the comma sepeated numbers")
numbers = [int(num) for num in list.split(',')]

max_numbers = max(numbers, key=lambda x: x)

print(f"The largest number is {max_numbers}")
