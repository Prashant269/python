#amstrong number
num=input("enter any number")
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//=10
print temp 
