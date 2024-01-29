class grandparent():
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)

class parent(grandparent):
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
    def display(self):
        parent.display(self)
        print(self.e,self.f)
        
class child(parent):
    def __init__(self,g,h):
        self.g=g
        self.h=h
obj=child(1,2)
print(obj.a)
print(obj.b)






