#    ..............First ..........

# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1=[' ',' ',' ']
# row2=[' ',' ',' ']
# row3=[' ',' ',' ']

# row2[1]='x'

# display(row1,row2,row3)


# result=int(input("Please enter your number"))

# print(type(result))


# def validate_check():

#     choice='WRONG'
#     acceptable_range=range(0,10)
#     within_range=False

#     while choice.isdigit()==False or within_range==False:
#         choice=input("please enter a number between 0-10")

#         if(choice.isdigit==False):
#             print("Sorry that is not a digit")
        
#         if(choice.isdigit()==True):
#             if(int(choice) in acceptable_range):
#                 within_range=True
#             else:
#                 print("Out of range")
#                 within_range=False
    
#     return int(choice)

# validate_check()



#  ............Second ...........
class Dog():
    species='mammal'

    def __init__(self,name,bread):
        self.name_atri=name
        self.bread_attri=bread

    
    def bark(self):
        print('wook my name is {} '.format(self.name_atri,Dog.species))

    
mydog=Dog('Husskie','lab')
print(mydog.bark())




# ...............Third...............

class Animal():

    def __init__(self):
        print("Animal created")
    
    def who_am_i(selfl):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def who_am_i(self):    #Modify new instance
        print("I am an animal")

    def bark(self):        # creating new intence
        print("i am eating and dog")


# ............Fourth.............

# If we want to access the len,str function inside the class they are not get access or giving some error 
# so for that we need to create a function for all like len,str and so on 

class Book():

    def __init__(self,title,authohr,page):

        self.title=title
        self.authoodr=authohr
        self.page=page

    def __str__(self):
        return f"{self.title} by {self.authoodr}"

    def __len__(self):
            return self.page
    
myb=Book("Ayush","singh",754)
print(myb.__len__())

