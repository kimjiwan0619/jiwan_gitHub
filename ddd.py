def ad_calc(text):

    index_sub = int(text.find("-"))
    index_add = int(text.find("+"))
    while(True):
        index_sub = int(text.find("-"))
        index_add = int(text.find("+"))

        if index_add>index_sub:
            num1=int(text[:index_sub])

            a =int(text.find('+',index_sub+1))
            b= int(text.find('-',index_sub+1))

            if a<b or b==-1:
                num2=num1-int(text[index_sub+1:a])
                num2 = str(num2)
                text.replace(text[:a],'num2')
            else:
                num2=num1-int(text[index_sub+1:b])
                num2 = str(num2)
                text.replace(text[:b], 'num2')
        elif index_add < index_sub:
            num1=int(text[:index_add])

            a = int(text.find('+', index_add +1))
            b = int(text.find('-', index_add + 1))

            if a<b or b==-1:
                num2=int(text[index_add+1:a])+num1
                num2=str(num2)
                text.replace(text[:a], 'num2')
            else:
                num2=int(text[index_add+1:b])+num1
                num2 = str(num2)
                text.replace(text[:b], 'num2')
        elif index_add==-1:
            num1=int(text[:index_sub])
            b= int(text.find('-', index_sub + 1))
            num2=num1-int(text[index_sub+1:b])
            num2=str(num2)
            text.replace(text[:b],'num2'])
        else:
            num1 = int(text[:index_add])
            a = int(text.find('+', index_add + 1))
            num2 = num1 + int(text[index_add + 1:a])
            num2 = str(num2)
            text.replace(text[:a], 'num2'])

        if index_add==-1 and index_sub==-1:
            break
    return num2

print(ad_calc("17+15-13-12"))