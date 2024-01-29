#to display the parent class variable by using super().
class parent:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)


class child(parent):
    a=40 
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f
    def display(self): #by method chaining method

         #parent.display(self) 
         super().display() #we can also use
         print(self.e,self.f)

     

    
obj=child(4,5,6,7)
print(obj.a)
print(obj.c)
print(obj.d)
print(obj.e)
print(obj.f)
print(vars(obj))
print(obj.display())