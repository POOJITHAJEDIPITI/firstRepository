#2.program for calculate the sum of even numbers in 6 digit number
def cal(num):
    if len(str(num))==6:
        sum=0
        for i in str(num):
            if int(i)%2==0:
                sum+=int(i)
        return sum
    else:
        print('enter 6 digit number')
print(cal(123456))