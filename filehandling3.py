file=open('name.txt','a')
data='\n sunil'
file.write(data)
file.close()










file=open('name.txt','r')
data=file.read()
print(data)
file.close()