#  Immutabilty 
name="sam"

# name[0]='p'   # error come

last_letter=(name[1:])

assign='p'+last_letter  # Adding letters

print(assign)

x=assign +" it is beutiful outside"
print(x)

letter='z'
print(letter*10)


#  These two are two different thing 
q=1+2
q1='1'+'2'


x='Hello world'
print(x.upper())


print(x.split())   # split the string with the white space or any specific world like here (i)

x='Hi this is a string '
print(x.split('i'))
