#To find smallest number in list
large=0
small=[0]
i=[0]
list= [200,100,600,300,50]
for i in list:
    if large< i:
        large=i
    if small>i:
        small=i
print small ,large    
        
