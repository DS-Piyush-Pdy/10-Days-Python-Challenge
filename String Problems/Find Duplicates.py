str="gcbxjbcjskajcjsbvjkajxlhctttygkmpoi"
result=""
for i in str:
    if str.count(i) > 1 and i not in result:
        result+=i
print(result)
        
