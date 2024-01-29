class A:
    c=print('a is called')
class B(A):
    d=print('b is called')
obj=B()
print(obj.d)