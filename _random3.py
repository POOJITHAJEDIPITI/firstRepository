#program for to generate 6 character captcha ,it should contain 2 digits,2 lower case,2 special symbols
import random
out=[]
while len(out)<6:
    out+=[str(random.randint(0,9))]
    out+=[random.randchoice(['#','$','*'])]
    out+=[chr(random.randint([65,91]))]
random.shuffle(out)
capcha=''
for i in out:
        capcha+=i
print(capcha)