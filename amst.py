num=input("enter any number")
temp=num
sum-=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp/10
if  sum==num:
    print num,'is a amstrong number'
else:
    print num,'is not a amstrong number '
