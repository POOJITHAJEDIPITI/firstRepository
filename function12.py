#program for printing vowels which are  not present  in given string
def filter(string):
    vowel='aeiouAEIOU'
    out=''
    for i in vowel:
        if i not in string:
            out+=i
        
    return out
print(filter('hello'))
print(filter('aeiou'))
print(filter('AEIOU'))
print(filter('aeiouAEIOU'))


    


