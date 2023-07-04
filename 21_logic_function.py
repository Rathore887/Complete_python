def check(number):
    return number%2==0

result=check(20)
print(result)


# ....... checking the result...........

# def checknum(list):
#     for num in list:
#         if num%2==0:
#             return True
#         else :
#             pass
#     return False

# mylist=[15,23,55]
# result=checknum(mylist)
# print(result)




my_new_list=[]

def check(list):
    for num in list:    
        if(num%2==0):
            my_new_list.append(num)
        else :
            pass
    return my_new_list

listt=[12,15,265,45,32,3,0,5,45,75]
result= check(listt)
print(result)
