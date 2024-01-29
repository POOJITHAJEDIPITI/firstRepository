class mtca:
    chairman='MR.sunil'
    location='Palamaner'
    college='MOTHER THERESA INSTIUTIONS'
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class  mca(mtca):
    principal='MR.Prabhakar Naidu'
    strength=240
    staff=9
class degree(mtca):
    principal='MR.Madhusudhan Rao'
    strength=500
    staff=20
class btech(mtca):
    principal='MS.Sravani'
    strength=600
    staff=35

poojitha=mca('G.POOJITHA',987698765432)
varsha=btech('v.Varsha',3456789034)
print(poojitha.principal)
print(poojitha.chairman)
print(poojitha.college)
print(poojitha.location)
print(poojitha.name)