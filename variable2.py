a=10
def fun():
    global a #used to modify the variable value
    a=20
    print(a)
#print(a)  10
fun()
print(a) #20
print(a)#20 here the a value modified by global keyword by that only we get 20