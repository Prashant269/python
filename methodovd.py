class cs(object):
    def sum(self):
        a=10
        b=20
        print a+b
class cs1(cs):
    def sum(self):
        a=30
        b=20
        print a+b
class cs2(cs1):
    def sum(self):
        a=20
        b=20
        print a+b


x=cs1()
x.sum()
        
