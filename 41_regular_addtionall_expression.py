import re

print(re.search(r'cat|dog','he cat is here'))

print(re.findall(r'.at','The cat in the hat went splat'))

print(re.findall(r'...at','The cat in the hat went splat'))

print(re.findall(r'^\d','2 is a number')) # start with number

print(re.findall(r'\d$','The number is 2'))   # End with number

phrase='there are 3 number 34 inside 5 this sentence'

# Exculde number
pattern=r'[^\d]'
print(re.findall(pattern,phrase))

# Merge them are splited word
pattern=r'[^\d]+'
print(re.findall(pattern,phrase))

# Exclude any perticular word
test_pharse="This is a string! But it has punctunation.How an we remove it?"
pattern=re.findall(r'[^!.?]+',test_pharse)
print(pattern)

# Join the previous split word
clean=re.findall(r'[^!.?]+',test_pharse)
' '.join(clean)
print(clean)

text='Only find the hypen-words in this sentence. But you do nt know  how long-go'
pattern=r'[\w]+-[\w]+'
print(re.findall(pattern,text))

text='Hello would you like some catfish?'
textwo='hello  would you like to take a catnap'
textthree='Hello have you seen this caterpiller'

print(re.search(r'cat(fish|nap|erpiller)',textthree))


