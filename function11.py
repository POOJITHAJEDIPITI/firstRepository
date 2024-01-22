def vowel(str):
    out=[]
    n=0
    for v in range(len(str)):
        if str[v] in 'AEIOUaeiou':
            out+=[v]
    return out
y=vowel('hello')
print(y)
x=vowel('aeiou')
print(x)
