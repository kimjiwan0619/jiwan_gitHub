a=input('입력:')
b=list(a)
for i in b:
    if i=='y':
        d='a'
    elif i=='z':
        d='b'
    else:
        c=ord(i)+2
        d=chr(c)
    print(d,end='')