a=input('enter the string:-')
count=0
n=0
while n<len(a)-1:
    if a[n] in 'aeiouAEIOU':
        count+=1
    n+=1
print(count)