s=open('skill.txt','r')

eof=s.read()
punct='''()'''
for i in eof:
    if i in punct:
        eof=eof.replace(i,' ')
    elif i=='\n':
        eof=eof.replace(i,'')
skilllist={}
for j in eof.split(','):
    skilllist[j]=None
del skilllist['']
for i in skilllist:
    count=0
    for j in eof.split(','):
        if i ==j:
            count+=1
    skilllist[i]=count
print("the ranked skill list")
rankno=1
for i in sorted(skilllist,key=skilllist.get,reverse=True):
    print(f"{rankno} {i} : {skilllist[i]}")
    rankno+=1
