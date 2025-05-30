str=input("Enter you sentence: ")
words=str.split()
result=''
for i in words:
    if len(i)>0:
        result+=i[0].upper() + i[1:].lower() + ' '
print(result)
