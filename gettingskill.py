import requests
import json
u=open("url.txt",'r')
f=open('skill.txt','w')
s=open('skilljson.json','w')
url=u.read()
u.close()
header={
      'authority': "www.naukri.com",
      'Connection': "keep-alive",
      'User-Agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'",
      'Referer': "https://www.naukri.com/information-technology-jobs-in-chennai?k=information%20technology&l=chennai",
      'appid': "109",
      
      'systemid': "109",
    }

for i in url.split('\n'):
    res=requests.get(i,headers=header)
    json.dump(res.json(),s)
    a=res.json()
    for i in range(0,len(a['jobDetails'])):
        f.write(a['jobDetails'][i]['tagsAndSkills'].upper()+',')
        if i!=len(a['jobDetails'])-1:
          f.write('\n')

f.close()
s.close()
