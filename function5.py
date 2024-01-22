#program for generate sequence of numbers similar to range function by using type2(with args and without return)
def sequence(num1,num2,num3):#num1=starting value,num2=ending value,num3=updation
    out=[]
    while num1<num2:
        out+=[num1]
        num1+=num3
    print(out)
sequence(1,10,2)

    