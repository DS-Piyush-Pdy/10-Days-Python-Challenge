str="AAAEDDDFHRVJJJJRTRTTTW"
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in str:
    if count[i]==1:
        print("First non repeating character is: ",i)
        break
else:
    print("No non repeating characters")