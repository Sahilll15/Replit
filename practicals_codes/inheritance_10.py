#superclass
class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def say_hello(self):
    print(f"Hello {self.name}")

#subclass
class student(person):
  #inheritance
  def __init__(self,name,age,Branch):
    #calling of superclass
    super().__init__(name,age)
    self.Branch=Branch

  def Branchh(self):
    print(f"My branch is {self.Branch} and age is{self.age}")

#object from person class
person1=person("sahil",19)
#object from student class
student1=student("chikitsa",19,"CSE")

#METHOD FROM PERSON CLASS CALLED
person1.say_hello()
#Mehtod from student class called
student1.Branchh()