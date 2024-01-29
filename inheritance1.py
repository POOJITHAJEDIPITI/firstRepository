class parent:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
class child(parent):
    a=40 #overrides parent class a prints 40
    def __init__(self,e,f):#overrides the parent method
        self.e=e
        self.f=f

    
obj=child(4,5)
print(obj.a)
print(obj.e)
print(obj.f)