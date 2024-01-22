#program for printing vowels which are  not present  in given string-second method
def filter(string):
    vowel='aeiouAEIOU'
    out=''
    for i in string:
        if i in vowel:
            out+=i
    return out
def extract(st):
    res=''
    for j in 'aeiouAEIOU':
        if j not in st:
            res+=j
    return res
print(extract(filter('hello')))
