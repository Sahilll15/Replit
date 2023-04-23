# . Write a Python program to add two lists using a lambda function. The program should prompt the user to enter two lists of comma-separated numbers and then use a lambda function to add the corresponding elements of the two lists. The resulting list should
# then be displayed to the user.

list1=input("Enter the comma seprated numbers for list 1")
numbers1=[int(num) for num in list1.split(',')]

list2=input("Enter the comma seprated numbers for list 2")
numbers2=[int(num) for num in list2.split(',')]


print(numbers1)
print(numbers2)

add_list=lambda x,y:[a+b for a,b in zip(x,y)]

result=add_list(numbers1,numbers2)

print(f"the results of the numbers is{result}") 

# list(zip(list1, list2))
# # Output: [(1, 4), (2, 5), (3, 6)]