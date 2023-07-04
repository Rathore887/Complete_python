def my_func(a,b,c=0):
    return sum((a,b,c))**0.05

print(my_func(10,25))




# What if i want to pass more number so we use arg funciton

# .......Tupple return ......

def myfnc(*args):     # * give the indecation that this is args 
    print(args)

print(myfnc(10,4,5,0,12,85))


# .......Dictonary return 

def func(**kargs):    # ** shows the dictonary  return
    print(kargs)
    if 'fruit' in kargs:
        print('My fruit of chioce is here {}'.format(kargs['fruit']))
    else:
        print("Not avaialable here")

func(fruit='apple',veggie='lettuce')



def comb(*args,**kargs):
    print(args)
    print(kargs)
    print('I would like {} {} '.format(args[0],kargs['food']))

comb(10,1,2,0,5,fruit='egg',food='apple')