class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  #method of person class
  def intro(self):
    print(f"Mu name is {self.name} and my age is {self.age}")


#objeects
person1=Person("Sahil",30)

#call method
person1.intro()

