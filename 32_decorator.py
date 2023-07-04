def new_decorator(origial_function):
    def wrap_fun():

        print('some extra code ,before the orginal function')

        origial_function()

        print('smoe extra code after the original funcion')
    
    return wrap_fun


def fun_need_decorator():
    print('I wnat to be decorator')

# print(fun_need_decorator())

decorated_func=new_decorator(fun_need_decorator)

# decorated_func()

# @new_decorator 
def fun_need_decorator():
    print('I wnat to be decorator')

fun_need_decorator()