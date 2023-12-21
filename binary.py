s=eval(input('enter any string'))
i=0
out=''
while i<len(s):
    if s[i]=='1':
        out=out+'0'
    else:
        out=out+'1'
    i+=1
print(out)