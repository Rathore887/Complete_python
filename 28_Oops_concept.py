class Dog():

    def __init__(self,bread,name,spot):

        self.breed_attri=bread
        self.name_attri=name
        self.spot_attri=spot


my_dog=Dog(bread='lab',name='Huskki',spot='USA')

print(my_dog.breed_attri)



class Dog():

    species='Mammal'

    def __init__(self,bread,name,spot):

        self.breed_attri=bread
        self.name_attri=name
        self.spot_attri=spot


my_dog=Dog(bread='lab',name='Huskki',spot='USA')

print(my_dog.breed_attri)
print(my_dog.species)