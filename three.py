#swap 4 variables
# swap variable
w=input("enter any nymber")
x=input("enter any nymber")
y=input("enter any number")
z=input("enter any number")
print("w before swap :{}".format(w))
print("x  before swap:{}".format(x))
print("y before swap :{}".format(y))
print("z before swap :{}".format(z))

w=w+x+y+z
x=w-x-y-z
print("x after swap is {}".format(x))
y=w-x-y-z
print("y after swap is {}".format(y))
z=w-x-y-z
print("z after swap is {}".format(z))
w=w-x-y-z
print("w after swap is {}".format(w))
