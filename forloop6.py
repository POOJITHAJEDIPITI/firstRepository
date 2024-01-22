#program for add the integers in heterogenous collection
a=[1,'2',2,2.4,[4,5,6],9,16,'abcd']
sum=0
for i in a:
    if isinstance(i,int):
        if i%2==0:
            sum=sum+i
        else:
            sum=sum-i
print(sum)