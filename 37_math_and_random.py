import math

value=4.354
print(math.floor(value))
print(math.ceil(value))

print(round(4.5))
print(round(5.5))

print(math.pi)

from math import pi
print(pi)

print(math.e)
print(math.inf)
print(math.nan)

print(math.e)
print(math.log(math.e))

print(math.log(100,10))

print(math.sin(10))

print(math.radians(180))

print(math.radians(180))


import random
print(random.randint(0,100))


print(random.seed(101))
print(random.randint(0,100))


mylist=list(range(0,20))
print(mylist)

print(random.choice(mylist))

print(mylist)


mylist=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# sample with replacement or repeation 
print(random.choice(population=mylist,k=10))

# sample without replacement or repeation 
print(random.sample(population=mylist,k=10))

random.shuffle(mylist)

print(mylist)

print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))


