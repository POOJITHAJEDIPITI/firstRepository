a=10
def funn():
    c=20
    def inner():
        print(a)
        print(c)
       # inner()
    print(c)
    inner()
funn()