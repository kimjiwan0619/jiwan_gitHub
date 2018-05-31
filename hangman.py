a=input('단어를 입력 :')
c=list(a)
d=list("-"*len(a))
print(d)

num=0
while(True):
    b=input('문자를 입력 :')
    if b in c:
        for i in range(len(a)):
            if c[i]==b:
                d[i]=b
                print(d)       
    else:
        num=num+1
        
        if num == 5:
            print("기회소진!")
            break
