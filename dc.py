import random
min=1
max=6
throw_dice="yes"
while throw_dice=="yes" or "y":
 print "after throwing dice"
 print random.randint(min,max)
 print random.randint(min,max)

 throw_dice=raw_input("Throw dice again")
