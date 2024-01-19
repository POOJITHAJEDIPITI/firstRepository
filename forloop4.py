#program for removing duplicate values in list
a=input('enter the list values \n')
out=''
for char in a:
    if char not in out:
        out=out+char
print(out)