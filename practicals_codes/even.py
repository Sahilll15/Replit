numbers=input("Enter the comma seprated numbers")
num_list=[int(num) for num in numbers.split(',')]

even_list=lambda x:x%2==0

even=list(filter(even_list,num_list))

print(even)