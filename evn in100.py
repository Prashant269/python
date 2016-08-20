#progrm to print even and odd numbers between 1 to 100
i=1
print("even numbers are:") 
for i in range(100):
    if i%2==0:
        print("{} is even ".format(i))
    else:
        print("{} is odd".format(i))
