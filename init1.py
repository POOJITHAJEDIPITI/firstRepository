class mtca:
    principal='MR.Prabhakar naidu'
    college='MOTHER THERESA INSTITUTE OF COMPUTER APPLICATIONS'
    location='palamaner'
    def __init__(self,sname,mobile,email,semester):
           self.studentname=sname
           self.mobilenumber=mobile
           self.emailaddress=email
           self.sem=semester
student1=mtca('poojitha','93987654','poojitha@gmail.com','1')
print(student1.studentname)

print(student1.mobilenumber)
print(student1.principal)
print(student1.college)
print(student1.location)

