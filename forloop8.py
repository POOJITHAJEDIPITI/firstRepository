#program for storing the index values of vowels in given string
a=input('enter a string \n')
out=[]
for i in range(len(a)):
    if a[i] in 'aeiouAEIOU':
         out+=[i]
    
print(out)