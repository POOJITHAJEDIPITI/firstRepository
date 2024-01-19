#program for removing duplicate characters in given string
a=input('enter the string \n')
out=""
for char in a:
    if char not in out:
        out=out+char
print(out)
