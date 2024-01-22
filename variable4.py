a=10
def fun():
    c=20
    def inner():
        global a
        a=90
        nonlocal c
        c=40
        print(c)
    print(c)
    inner()
    print(c)
fun()
print(a)