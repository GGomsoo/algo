str = input()
res = ""

for i in range(len(str)):
    word = str[i]
    
    if word.isupper():
        res += word.lower()
    else:
        res += word.upper()

print(res)
