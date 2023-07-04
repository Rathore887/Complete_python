# try:
#     result=10+10
# except:
#     print("Heyy it look like you are not adding correctly")
# else:
#     print("add went well")
#     print(result)



# try:
#     f=open('testfile','r')
#     f.write("write a test line")

# except TypeError:
#     print("There was a typ error")

# except OSError:
#     print("Hey you have a os error")

# except:
#     print("all other exceptions")

# finally:
#     print("I always run")


# Try and catch block in function 

def ask_for_int():
    try:
        result=int(input("Please provide number "))
    except:
        print("Whhops that is not a number")
    finally:
        print("End of try/except/finally")
    
ask_for_int()



# try and except inside the while loop 
def ask_for_int():

    while True:
        try:
            result=int(input("Please provide number "))
        except:
            print("Whhops that is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")

ask_for_int()