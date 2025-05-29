str="Hello I am a String"
vowels="aeiouAEIOU"
count=0
for i in str:
    if i in vowels:
        count+=1
print("Vowels in str:",count)
    