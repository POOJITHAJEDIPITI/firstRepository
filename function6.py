#program for count the occurance of character in string by using type2 function(with args & without return)
def occurance(string,char):
    i=0
    count=0
    while i<len(string):
        if string[i] in char:
            count+=1
        i+=1
    print(count)
occurance('poojitha','o')
    


           