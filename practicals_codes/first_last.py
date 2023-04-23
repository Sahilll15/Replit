name_list=input("Enter the list of the names in the format First last")

name_list=name_list.split(',')

name_list.sort(key=lambda x:x.split()[-1])

print("the sorted name in the list are ",name_list)