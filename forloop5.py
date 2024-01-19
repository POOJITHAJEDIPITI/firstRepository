#program for add even numbers and substract odd numbers in a given heterogenous list collection
input=[1,'1',2,2.4,[4,5,6],9,16,'abcd']
sum=0
for char in input:
    if type(char)==int:
        if char%2==0:
            sum=sum+char
        else:

            sum=sum-char
print(sum)