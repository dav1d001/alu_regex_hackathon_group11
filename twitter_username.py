import re

usernamepttrn = re.compile(r'@[a-zA-Z0-9]+')
text = input(" Enter text >> ")
match = usernamepttrn.search(text)
print(match)
results = usernamepttrn.finditer(text)
for match in results:
    print(f" twitter username found: {match.group()}")
