#program for print the first non repeatative character from given string
st=input('enter a string:-')
i=0
while i<len(st):
    if st[i] not in st[i+1:]:
        print(st[i])
        break
    i+=1

