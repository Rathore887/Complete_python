# stockprice=[('Apple',455),("google",600)]

# for item in stockprice:
#     print(item)


work_hours=[('Abby',100),('Biilyy',400),('Ayush',5000)]

def emplyee(work_hour):
    max_work=0
    empolyee_name=''

    for name,hour in work_hour:
        if hour>max_work:
            max_work=hour
            empolyee_name=name
        else:
            pass
    
    return max_work,empolyee_name

print(emplyee(work_hours))