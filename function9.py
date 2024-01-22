#program for sum of all even number in 6 digit number
def add(num):
    sum=0
    temp=str(num)
    if len(temp)==6:
        for i in temp:
            if int(i)%2==0:
               sum+=int(i)
        return sum
y=add(123456)
print(y)
a=add(222222)
print(a)
            
    

    
        

        





    