#program for find the factorial of number using type 1 function(without args and return)
def fact1():
    a=int(input('enter a number:-'))
    fact=1
    for i in range(1,a+1):
        fact*=i
    print(fact)
fact1()