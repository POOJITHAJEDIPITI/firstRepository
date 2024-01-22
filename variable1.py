#global variable accessing
a=10
def fun():
   # print(a) error:local variable 'a' referenced before assignment
    a=20
    print(a)
print(a)
fun()