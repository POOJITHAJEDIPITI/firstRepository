num=int(input('enter the number'))
count=0
i=1
while num>=i:
    if num%i==0:
        count+=1
    i+=1
if(count==2):
    print('prime')
else:
    print('not prime')
    