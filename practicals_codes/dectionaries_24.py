 # Write a program to demonstrate working with dictionaries in python

my_dict={}

my_dict["banana"]=1
my_dict["cheery"]=2
my_dict["mango"]=3

print("The content of the dict is ",my_dict)

print("the key of the value is ",my_dict["banana"])

print("The keys in the dict are:")
for key in my_dict:
  print(key)

print("the values in the dict are")
for value in my_dict.values():
  print(value)

print("The key,value pair of the dict are")
for key,value in my_dict.items():
  print(key,":",value)