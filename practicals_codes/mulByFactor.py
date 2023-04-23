# Write a Python program to multiply a list of numbers by a given factor using a lambda function. The program should prompt the user to enter a list of comma-separated numbers and a factor, and then use a lambda function to multiply each element of the list by the factor. The resulting list should then be displayed to the user.


list = input("Enter the comma sepeated numbers")
numbers=[int(num) for num in list.split(',')]

factor=int(input("Enter the factor"))

ans_list=[num*factor for num in numbers]

print(ans_list)