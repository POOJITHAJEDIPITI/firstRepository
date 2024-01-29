class increment:
    def __init__(self,a):
        self.a=a
    def increment1(self,step=1):
        self.a=self.a+step
        #return self.a
        return str(self.a) # str is used to convert the int to str
    def increment(self,step=1):
        self.a=self.a-step
        return self.a
num=increment(5)
#print(num.increment1())
print(repr(num.increment1)) #repr is magic method used to get the value of object
#print(str(num.increment1))  # str is magic method used to get the value of object


