import math
l=int(input("enter length"))
print("length is",l)
b=int(input("enter breadth"))
print("breadth is",b)
h=int(input("enter height"))
print("height is",h)
print(l,h,b)
s=(l+b+h)/2
print(s)
area=math.sqrt(s*(s-l)*(s-b)*(s-h))
print("Area of triangle",area)