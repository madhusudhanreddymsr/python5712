s=input('enter any string:')
i=0

while i<len(s):
    if s[i] in"aeiouAEIOU":
        count+=1
        print(s[i])
    i+=1
print(count)