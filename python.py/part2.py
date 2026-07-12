x=int(input("enter any number"))
y=int(input("enter other number"))

print("current x value is",x)
print("current y value is",y)

"""z=x
x=y
y=z"""
x,y=y,x
print("now x value is",x)
print("now y value is",y)