double =lambda x:x*2

print(double(2))

area= lambda x,y:x*y

x=int(input("Enter the length"))
y=int(input("Enter the bredth"))

print(area(x,y))


def app(fx,value1):
   return 6+fx(value1)

print(app(double,1))

