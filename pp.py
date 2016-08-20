#palindrome
num=input( "enter a number")
temp=num
result=0
while temp > 0:
    result=(temp%10)+(result*10)
    temp=temp/10
if result==num:
    print result,"is a palindrome number"
else:
    print result,"is not a palindrome number"
