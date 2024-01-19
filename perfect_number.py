num=eval(input('enter a number \n'))
sum=0
i=1
while i<num:
   if num%i==0:
     sum+=i
   i+=1
if num==sum:
    print('given number is perfect number')
else:
    print('given number is not perfect number')