str="aaabbbbcccccccc"
counta=0
countb=0
countc=0
for i in str:
    if i == 'a':
        str.count(i)
        counta+=1    
    if i == 'b':
        str.count(i)
        countb+=1
    if i == 'c':
        str.count(i)
        countc+=1
print("a",counta,"b",countb,"c",countc)