import numpy as np

v1=np.array([1,2,3])
v2=np.array([4,5,6])

v3=v1+v2
v3_sub=v1-v2

print("The vector 1",v1)
print("The vector 2",v2)
print("The Solution is",v1+v2)
print("The Solution is",v1-v2)


#parrt2

s=2
v4=s*v1
print("the scalar multiplication is",v4)

#part3-Dot product

n5=np.dot(v1,v2)

print("The Dot prodct is",n5)
#part 4-multiplication


v6=np.matmul(v1,v2)
print("The matrix multi is",v6)