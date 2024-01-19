a='hello my name is poojitha'
i=0
out=" "
while i<len(a):
    if a[i]==" ":
        out+="___"
    else:
        out+=a[i]
    i+=1
print(out)