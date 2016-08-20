class calc:
    info="calculation operations are as fallows:"
  
    def add(self):
       x=5
       y=5
       print x+y,"is sum"
    def sub(self):
         x=5
         y=5
         print x-y,"is subtraction"
    def mul(self):
         x=5
         y=5
         print x*y,"is multiplication"
    def div(self):
        x=5
        y=5
        print x/y,"is division"
    def mod(self):
        x=5
        y=5
        print x%y,"is modulus"
myobject=calc()
print myobject.info
myobject.add()
myobject.sub()
myobject.mul()
myobject.div()
myobject.mod()
