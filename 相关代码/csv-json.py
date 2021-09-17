# -*- coding: utf-8 -*-
import json

f=open("concept.csv","r",encoding='utf-8')
ls=[]
for line in f:
        line = line.replace("\n", "")
        ls.append(line.split(","))
f.close()
print(ls[1:])
fw=open("concept.json","w",encoding='utf-8')
for i in range(1,len(ls)):
    ls[i]=dict(zip(ls[0],ls[i]))
a = json.dumps(ls[1:],sort_keys=True,indent=4,ensure_ascii=False)
print(a)
fw.write(a)
fw.close()
