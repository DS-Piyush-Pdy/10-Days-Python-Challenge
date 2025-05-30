str=input("Enter your sentence: ")
inp=input("Enter the character you want to count: ")
count=0
for i in str:
    if i==inp:
        count+=1
print(inp,"occured",count,"times")
