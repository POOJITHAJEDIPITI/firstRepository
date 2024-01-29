class static:
    def __init__(self,a):
        self.a=a
@staticmethod #which is independent of both class and object
def add(a,b):
    return a+b
print(add(2,3))