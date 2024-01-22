class circle:

    def __init__(self,r):
        self.r=r
    def area_circle(self):
        return self.r**2*3.14
    def circum_circle(self):
        return  self.r*2*3.14
    def diameter_circle(self):
        return self.r*2
obj=circle(3)
print(obj.area_circle())
print(obj.circum_circle())
print(obj.diameter_circle())