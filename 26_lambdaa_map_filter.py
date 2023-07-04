def square(num):
    return num**2

my_num=[1,2,3,4,5]

# 1 Method to use to call he fuction
for item in map(square,my_num):
    print(item)

# 2 method too call the functioon using map function 

list(map(square,my_num))


# 2 example 

def checknum(num):
    return num%2==0


mynum=[1,2,3,4,5,6,7]

list(filter(checknum,mynum))

for n in filter(checknum(mynum)):
    print(n)




# Lambda function 
# previously we are writting the function it should be bit lengthy 
# so we introduce the lambda function

def square(num):
    result=num**2
    return result

square(3)

#  Both are doing the same thing
lambda num:num**2

square(3)    


# converting first function into lambda 

list(map(lambda num:num**2,mynum))

list(filter(lambda num:num%2==0,my_num))
