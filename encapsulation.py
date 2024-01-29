#access specifiers
#public access specifier
class A:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
obj=A(5,6)
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

