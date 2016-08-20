def add(x,y):
 return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  return x/y
print("enter any choice ")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
choice=input("enter any of above choice(1/2/3/4):")
num1=input("enter first number:")
num2=input("enter second number:")
if choice==1:
    print("choice 1 is selected so Addtion:\n")
    z=add(num1,num2)
    print ("sum of {}+{}={}".format(num1,num2,z))
elif choice==2:
      print("choice 2 is selected so Subtraction:\n")
      z=sub(num1,num2)
      print("Subtraction of {}-{}={}" .format(num1,num2,z))
elif choice==3:
     print("choice 3 is selected so Multiplication:\n")
     z=mul(num1,num2)
     print ("Multiplication of {}*{}={}".format(num1,num2,z))
elif choice==4:
     print("choice 4 is selected so Division:\n")
     z=div(num1,num2)
     print("Division  of {}/{}={}".format(num1,num2,z))
else:
       print("Wrong selection" )   
