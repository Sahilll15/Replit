class person:
  print("Sahil Chalke")



person1=person()

class cricketer():

  def __init__(self,name,role):
    self.name=name
    self.role=role

  def say_role(self):
    print(f"my name is {self.name} and my Role in the teams is {self.role}")


# cricketer1=cricketer("Kohli","Batsmen")
# cricketer1.say_role()


class batsmen(cricketer):
   def __init__(self,name,role,runs):
     super().__init__(name,role)
     self.runs=runs

   def say_runs(self):
     print(f"i have scored {self.runs} runs")



batsmen1=batsmen('sahil',"batting",100)
batsmen1.say_role()
batsmen1.say_runs()


#polymorpish
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.speak()


#constructor

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def __str__(self):
    return f"my name is {self.name} and age is {self.age}"


person1=person("sahil",30)
print(person1)

# person1.person_desc()
# print(f"The age of the person is {person1.age}")
# print(f"The name of the person is {person1.name}")