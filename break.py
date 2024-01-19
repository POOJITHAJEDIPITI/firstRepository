str=input('enter a string:-')
out=''
res=''
n=0
for char in str:
    if  not char in out:
        out+=char
        
    else:
        res+=char
print(out)
print('res',res)