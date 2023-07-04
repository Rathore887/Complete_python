# ......................... Append function or Push function ..............
my_list='hello'

mystring=[]

# for letter in my_list:
#     mystring.append(letter)

# print(mystring)


# mylist=[letter for letter in my_list]
# print(mylist)

# mylist=[uqu for uqu in 'wordlie']
# print(mylist)


# mylist=[num**2 for num in range(0,12)]
# print(mylist)

mylist=[uqu for uqu in range(0,12) if uqu%2==0]
print(mylist)



# ............... Nested for loop .............
mylist=[]

for a in [2,4,6]:
    for b in [5,6,7]:
        mylist.append(a+b)

print(mylist)