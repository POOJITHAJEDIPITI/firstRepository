#program for to find factorial of number
num=int(input('enter a number:-'))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(fact)