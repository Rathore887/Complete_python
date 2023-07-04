from collections import Counter

mylist=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,]
print(Counter(mylist))

print(Counter('aaaaaaaabbbbbbshfsfh'))

sentence="How mnay time does ech word would have been repeated"
print(Counter(sentence.lower().split()))

letter='aaaaaaaaaabbbbbbvvvvvvvvv'
c=Counter(letter)
print(c.most_common(2))


from collections import defaultdict
d={'a':10}
print(d)
print(d['a'])

# what if element is not present in the dictorory so that's why we are 
# placing some default value 

d=defaultdict(lambda:0)
d['correct']:10
print(d)

d['not present']
print(d)

mytuple=(10,20,30)
print(mytuple[0])

from collections import namedtuple

Dog=namedtuple('Dog',['age','breed','name'])
sammy=Dog(age=5,breed='Husky',name='sam')
print(type(sammy))
print(sammy)
print(sammy.breed)
print(sammy.name)
print(sammy[0])


