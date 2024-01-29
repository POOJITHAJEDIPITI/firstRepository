class mtca:
    principal='MR.Prabhakar naidu'
    college='MOTHER THERESA INSTITUTE OF COMPUTER APPLICATIONS'
    location='palamaner'
    def __init__(self,sname,mobile,email,semester):
           self.studentname=sname
           self.mobilenumber=mobile
           self.emailaddress=email
           self.sem=semester
    def upd_mob(self,new):
          self.mobilenumber=new
          print('mobile number updated')

    def  upd_sem(self,next):
          self.sem=next
          print('semester is updated')
    def  upd_email(self,email2):
          self.emailaddress=email2
          print('email address is updated')
    @classmethod #used to pass the address if we take cls or object it will pass address to class only so it reflects to all taken objects
    def change_principal(cls,new):
          cls.principal=new
poojitha=mtca('poojitha','93987654','poojitha@gmail.com','1')






