#program for printing ['abcd',[1,2,3]] in ['a','b','c',d',1,2,3]
def fname(arr):
    out=[]
    for i in arr:
        if type(i) in [str,list,tuple,set,dict]:
            for j in i:
                out+=[j]
    return out
print(fname(['abcd',[1,2,3]]))
 
        
