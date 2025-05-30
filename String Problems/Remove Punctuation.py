punct=".?!-,"
str=input("Enter your sentence: ")
result=''
for i in str:
    if i not in punct:
        result+=i
print(result)
        
