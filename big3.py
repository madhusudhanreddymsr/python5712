a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
if a>b and a>c:
    print(a,'is biggest')
elif b>c:
    print(b,'is biggest')
else:
    print(c,'is biggest')