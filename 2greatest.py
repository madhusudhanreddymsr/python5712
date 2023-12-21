a=int(input('enter num1:'))
b=int(input('enter num2:'))
c=int(input('enter num3:'))
if a>b and a>c:
    if b>c:
        print(b,'is 2nd greatest')
    else:
        print(c,'is 2nd greatest')
elif b>c:
    if a>c:
        print(a,'is 2nd greatest')
    else:
        print(c,'is 2nd greatest')

else:
    if a>b:
        print(a,'is 2nd greatest')
    else:
        print(b,'is second greatest')