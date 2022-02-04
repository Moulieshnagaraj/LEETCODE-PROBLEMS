


li=["flower","flow","floight","flo"]
prefix=li[0]
demo=len(li[0])
for i in range(1,len(li)):
    if len(li[i]) <= demo:
           demo = len(li[i])
           prefix=li[i]
result=prefix
count = 0
while count < len(li):

    str1=li[count]
    res = ''
    for i in range(demo):
        if str1[i]== prefix[i]:
            res=res+str1[i]

    if len(res) <= len(result):
        result=res

    count+=1




'''
prefix=strs[0]
        demo=len(strs[0])
        for i in range(1,len(strs)):
            if len(strs[i]) <= demo:
                demo = len(strs[i])
                prefix=strs[i]
        
        
        result=prefix
            
        count = 0
        while count < len(strs):

            str1=strs[count]
            res = ''
            for i in range(demo):
                if str1[i]== prefix[i]:
                    res=res+str1[i]
                else:
                    break

            if len(res) <= len(result):
                result=res

            count+=1
        return str(result)

'''





