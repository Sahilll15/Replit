# Write a Python program to filter a list of numbers using a lambda function. The
# program should prompt the user to enter a list of comma-separated numbers and then use a lambda function to filter the list so that only even numbers are included. The filtered list should then be displayed to the user.

numbers=input("Enter the comma seprated numbers")
num_list=[ int(num) for num in numbers.split(',') ]

even_list=lambda x :x%2==0
filter_numbers=list(filter(even_list,num_list))

print(f"The filtered numbers are {filter_numbers}")
