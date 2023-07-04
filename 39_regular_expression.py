text="The agnet phone number is 408-555-1234. Call soon"

print('phone' in text)

import re
pattern='phone'

print(re.search(pattern,text))

pattern="NOT IN TEXT"

print(re.search(pattern,text))   # return null beacuse it's not avaible

pattern='phone'

match=re.search(pattern,text)

print(match)
print(match.span())
print(match.start())

text='my phone once my phone twice'
match=re.search('phone',text)
print(match)

matches=re.findall('phone',text)
print(matches)

print(len(matches))

for match in re.finditer('phone',text):
    print(match.group())
