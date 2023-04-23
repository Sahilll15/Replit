#1.handling zero error

try:
  num1=int(input("Enter the num1"))
  num2=int(input("Enter the num2"))
  result=num1/num2
  print(result)
except ZeroDivisionError:
  print("The number cannot be divided by zero")

#2.ValueError

try:
  age=int(input("Enter the age of the person"))
  print(age)
except ValueError:
  print("The input is not valid")

#3. file not found error
try:
  file=open("new.txt","r")
  print(file.read())
  file.close()
except FileNotFoundError:
  print("File not found")

#4.MyCustomException

class MyCustomException(Exception):

  pass

try:
  raise MyCustomException("This is a cusom exception")
except MyCustomException as e:
  print("Caught custom exception",str(e))