list = input("Enter the number of the list by comma sepreted by comma ").split(
  ',')

list = [int(x) for x in list]

print(list)
tuple_list = tuple(list)

print(tuple_list)
