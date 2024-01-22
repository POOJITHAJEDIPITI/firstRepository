#program for remove the numbers in given string
a='user@123#aqdmin'
out=''
for char in a:
    if not '0'<=char<='9':
        out+=char
print(out)

    



