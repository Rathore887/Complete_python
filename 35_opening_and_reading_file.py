f=open('practice.txt','w+')
f.write('this is a test string')
f.close()


import os
print(os.getcwd())    # current working directory 

print(os.listdir('C:\\Users'))


# import shutil
# shutil.move('practice.txt',)   #move your file )

import send2trash
print(os.listdir())

send2trash.send2trash('practice.txt')
print(os.listdir())


# for folder,sub_folders,files in os.walk