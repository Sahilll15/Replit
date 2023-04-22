double =lambda x:x*2

print(double(2))

area= lambda x,y:x*y

x=int(input("Enter the length"))
y=int(input("Enter the bredth"))

print(area(x,y))


def app(fx,value1):
   return 6+fx(value1)

print(app(double,1))

lambda arguments: expression

square= lambda x: x*x 

print(square(2))

#que1

str_len=lambda str:len(str)

print(str_len("sahil"))

# qu2-Write a lambda function that takes a list of numbers and returns the sum of the even numbers.

num=[1,2,3,4,5,6,7]

even_numbers=filter(lambda x:x%2==0 ,num)
num_sum=sum(even_numbers)
print(num_sum)

strings = ["apple", "banana", "cherry", "date"]

str_a=lambda s:"a"  in  s
strings_a=filter(str_a,strings)

print(strings_a)
print(list(strings_a))


#que3-Write a lambda function that takes a list of strings and returns a list of all strings that start with the letter "a".

strings = ["apple", "aanana", "cherry", "date"]

str_a=lambda s:"p" in s[1]
strings_starts_a=filter(str_a,strings)

print(list(strings_starts_a))

people = [("Alice", 25), ("Bob", 35), ("Charlie", 40), ("Dave", 30)]

older_people=lambda person:person[1]>30

old_age=filter(older_people,people)

print(list(old_age))

#que5-my_dict = {"key1": True, "key2": False, "key3": True, "key4": True}

my_dict = {"key1": True, "key2": False, "key3": True, "key4": True}
true_keys=lambda d:[k for k,v in d.items() if v== True]

true_key_list=true_keys(my_dict)
print(true_key_list)


 