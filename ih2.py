class base1(object):
    def sum(self):
        a=10
        b=20
        print a+b,"is sum"
class base2(object):
        def sub(self):
         a=10
         b=5
         print a-b,"is sub"
class inheriting(base1,base2):
         pass
x=inheriting()
x.sum()
x.sub()
    
