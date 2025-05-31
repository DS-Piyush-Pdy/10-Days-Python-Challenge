str=input("Enter your sentence: ")
str2=""
words=[]
for i in str:
    if i == " ":
        words.append(str2)
        str2=""
    else:
        str2+=i
words.append(str2)
print(words)
