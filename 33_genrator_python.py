# we are using genertor because suopse if you want to some number between 
# 1 million then you need to store all number in memory which is not good
# SO that's why we are using genrator 

def create_cubes(n):

    for x in range(n):
        yield x**3

# 1 method 
ans=list(create_cubes(10))
print(ans)

# 2 method 
for x in create_cubes(10):
    print(x)


def gen_fibon(n):
    a=1
    b=1
#  Here if we are not using yeild then we need to store all value in some list
    for i in range(n):
        yield a
        a,b=b,a+b

for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x

# 1 mehod to access
# for number in simple_gen():
#     print(number)

# 2 method to acces 
g=simple_gen()
g
print(next(g))
print(next(g))
print(next(g))




s='hello'

# for letter in s:
#     print(letter)


s_itern=iter(s)
print(next(s_itern))
