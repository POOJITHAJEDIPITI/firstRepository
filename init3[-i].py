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
poojitha=mtca('poojitha','93987654','poojitha@gmail.com','1')





