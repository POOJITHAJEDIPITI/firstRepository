s='hello world'
i=0
n=' '
while i<len(s):
    if s[i]==' ':
        i+=1
        n+=chr(ord(s[i])-32)
    else:
        n+=s[i]
    i+=1
print(n)
