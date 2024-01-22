#program for toggle uppercase to lowercase and lowercase to upper case in string
def toggle():
    str=input('enter string:-')
    b=''
    for i in str:
            if 'a'<=i<='z':
                  b+=chr(ord(i)-32)
            else:
                  b+=chr(ord(i)+32)
    return b
x=toggle()
print(x)
    


    
    
 



