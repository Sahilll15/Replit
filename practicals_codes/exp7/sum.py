lst = input("Enter a list of numbers separated by space: ").split()

list = [int(num) for num in lst]

sum = 0
for i in list:
  sum += i

print(sum)
