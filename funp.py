# func to find prime
def prime(x):
    count=0
    for i in range(1,x+1):
     if x%i==0:
      count=count+1
    if count==2: 
      print 'primme'
      return x
    else:
      print 'not a prime'  
      return x
y=prime(99)
print y
