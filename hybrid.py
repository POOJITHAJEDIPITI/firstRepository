class A:
    a=10
class B(A):
    b=20
class C(A):
    c=30
class D(C,B):
    d=40
obj=D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

