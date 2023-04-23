a=float(input("Enter the lenght of a"))
b=float(input("Enter the lenght of b"))
c=float(input("Enter the lenght of c"))

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("It is a right-angled triangle.")
else:
    print("It is not a right-angled triangle.")