num=int(input('enter a number:-'))
sum=num
while num>0:
    out=num%10
    sum=sum*10+out
    num=num//10
if num==sum:
    print('given number is palindrome')
else:
    print('given number is not palindrome')