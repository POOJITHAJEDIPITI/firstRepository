#factorial of even numbers
def fact():
    fact=1
    n=0
    for i in range(0,n+1,2):
        fact*=i
    return fact
out=[fact(i)  for i in range(0,n+1,2)]
print(out)