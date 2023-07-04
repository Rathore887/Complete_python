# ................Range...........

# for num in range(10):
#     print(num)

# for num in range(3,10):
#     print(num)

# for num in range(0,11,2):
#     print(num)


# index_count=0

# for letter in 'abcde':
#     print('At index {} the letter is {}'.format(index_count,letter))
#     index_count+=1


# ...............enumerate...........

# word='abcsedf'

# for item in enumerate(word):
#     print(item)


# for index,letter in enumerate(word):
#     print(index)
#     print(letter)



# .....................Zip...........
# mylist1=[1,2,3]

# mylist2=['a','b','c']

# mylist3=[100,200,300]

# for item in zip(mylist1,mylist2,mylist3):
#     print(item)


# .....................Zip list...........
# list_file=list[zip(mylist1,mylist2,mylist3)]
# print(list_file)


# print(2 in [1,2,3])

# d={'mykey':345}
# print(345 in d.keys())

# ..........................Min and max funtion.............

# mylist=[100,200,300]

# print(min(mylist))
# print(max(mylist))

# ..............................Random functions.....................
from random import shuffle
mylist=[1,2,3,4,5,6,7,8,9]
random_list=shuffle(mylist)

print(mylist)


# ...............................randint function....................
from random import randint

print(randint(0,100))


# ..................................User input funtion .................
result=input("Enter a number here :")
print(result)
print(type(result))
