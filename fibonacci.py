#program for printing fibonacci series
a,b=0,1
n=int(input('enter a number'))
print(a,end=',')
while b<n:
    print(b,end=',')
    a,b=b,a+b