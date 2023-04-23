#using overriding

class Animal:
  def __init__(self,name):
    self.name=name

  def sound_made(self):
    pass

class Dog(Animal):

  def sound_made(self):
    print(f"{self.name} Barks")

class Cat(Animal):

  def sound_made(self):
    print(f"{self.name} meows")

dog=Dog("Rufus")
cat=Cat("Whiskers")

for animal in (dog,cat):
  animal.sound_made()


#using overloading

class Math:
  def add(self,*args):
    if len(args)==2:
      return args[0]+args[1]
    elif len(args)==3:
      return args[0]+args[1]+args[2]
    else:
      return sum(args)

math=Math()



print(math.add(1, 2))      
print(math.add(1, 2, 3))  
print(math.add(1, 2, 3, 4, 5))

#using normal arguments
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius ** 2

# Create objects of different classes
rect = Rectangle()
circle = Circle()


print(rect.area(4, 5))  
print(circle.area(3))     
