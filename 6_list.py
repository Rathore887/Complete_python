mylist=[1,2,3,4]

mylist=['string',100,23.2]

print(len(mylist))

mylist=['one','two','three']
print(mylist[0])

print(mylist[0:2])

anotherlist=['four','five']

print(mylist+anotherlist)  # concatnating 

mylist[0]='One all cabs'

print(mylist)

mylist.append('six')  # adding method

print(mylist)

mylist.pop() # removing the elememnts 

popperiem=mylist.pop()
print(popperiem)

mylist.pop(0)
print(mylist)  #remove the specific elements 

mylist =['a','e','ex','b']
numlist=[4,1,2,5,8,9]

mylist.sort()  #it will change the main varibale as well 
print(mylist)

numlist.sort()


numlist.reverse()
print(numlist)