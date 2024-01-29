class A:
    __a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
    @classmethod
    def classdisplay(cls):
        print(cls.__a,cls.b)
obj=A(4,5)
# to execute this 
 #obj._A__a