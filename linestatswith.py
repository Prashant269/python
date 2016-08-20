foh=open('c:/test/c.txt','r')
for line in foh:
    if line.startswith('hai'):
        line=line.rstrip()
        print line 
