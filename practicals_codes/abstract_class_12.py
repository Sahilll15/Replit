import abc

class Shape(abc.ABC):

  @abc.abstractclassmethod
  def area(self):
    pass

  def perimeter(self):
    pass

class Square(Shape):
  def __init__(self,side):
    self.side=side

  def area(self):
    return self.side ** 2

  def perimeter(self):
    return self.side * 4


square=Square(5)
print(square.area())
print(square.perimeter())