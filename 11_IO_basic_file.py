myfile=open('12...test.txt')
print(myfile.read())

myfile.seek(0)   # reset the file to remove the cursor 
print(myfile.read())


myfile.seek(0)   # reset the file to remove the cursor 
print(myfile.readlines())

# myfile.close()

filr2= open('12...test.txt',mode='w')