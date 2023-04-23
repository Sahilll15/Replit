import math

# Ask user to input the shape
shape = input("Enter the shape you want to calculate the area of (triangle/circle/rectangle): ")

# Calculate area of triangle
if shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

# Calculate area of circle
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is:", area)

# Calculate area of rectangle
elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)

# If the input is not valid
else:
    print("Invalid input. Please enter triangle, circle, or rectangle.")
