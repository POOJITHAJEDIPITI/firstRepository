num=eval(input('enter a number \n'))
sum=0
for i in range(1,num):
   if num%i==0:
     sum+=i
if num==sum:
    print('given number is perfect number')
else:
    print('given number is not perfect number')
    