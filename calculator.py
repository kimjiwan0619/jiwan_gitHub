def ad_calc(text):

    while(True):
        index_sub = text.find("-")
        index_add = text.find("+")
        if index_add==-1 and index_sub==-1:            
            break
        elif index_add==-1:
            num1=int(text[:index_sub])
            b= text.find('-', index_sub + 1)
            if b==-1:
                num2=num1-int(text[index_sub+1:])
                num2=str(num2)
                text=text.replace(text[0:],num2)
            else:
                num2=num1-int(text[index_sub+1:b])
                num2=str(num2)
                text=text.replace(text[:b],num2)
        elif index_sub==-1:
            num1 = int(text[:index_add])
            a = text.find('+', index_add + 1)
            if a==-1:
                num2=num1+int(text[index_add+1:])
                num2=str(num2)
                text=text.replace(text[0:],num2)
            else:
                num2 = num1 + int(text[index_add+ 1:a])
                num2 = str(num2)
                text=text.replace(text[:a], num2)
        elif index_add < index_sub :
            num1=int(text[:index_add])

            a = text.find('+', index_add +1)
            b = text.find('-', index_add + 1)
            if (a<b and a!=-1 )or b==-1:
                num2=int(text[index_add+1:a])+num1
                num2=str(num2)
                text=text.replace(text[:a], num2)
        
            else:
                num2=int(text[index_add+1:b])+num1
                num2 = str(num2)
                text=text.replace(text[:b],num2)
        elif index_add>index_sub:
            num1=int(text[:index_sub])

            a =text.find('+',index_sub+1)
            b= text.find('-',index_sub+1)

            if a<b or b==-1:
                num2=num1-int(text[index_sub+1:a])
                num2 = str(num2)
                text=text.replace(text[:a],num2)
                
            else:
                num2=num1-int(text[index_sub+1:b])
                num2 = str(num2)
                text=text.replace(text[:b], num2)
        
    return num2

print(ad_calc("1+1"))
