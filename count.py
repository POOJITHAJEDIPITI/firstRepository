i1=input('enter a string:-')
i2=input('enter the character:-')
count=0
n=0
while n<len(i1):
    if i1[n] == i2:
        count+=1
    n+=1
print(count)