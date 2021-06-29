import re

s="How are you"
x=re.search("^How.*you$",s)
if(x):
    print("Match Found")
else:
    print("Match not found")