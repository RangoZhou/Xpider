#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import numpy as np
import json


characterList = []
table = ''
with open('500.txt',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
        characterList.append(line.strip())

for character in characterList:
    # url = 'http://att.chaiwubi.com/wubi/86tj/'+character+'.gif'
    # r = requests.get(url, allow_redirects=True)
    # open(character+'.gif','wb').write(r.content)



    first = 'x'
    second = 'xx'
    third = 'xxx'
    whole = 'xxxx'
    table+=("'"+character+"': {'wubi86':{'code':{'first':'"+first+"','second':'"+second+"','third':'"+third+"','whole':'"+whole+"'},'base':true,'single':true,'decomposition':'/typing/res/decomposition/"+character+".gif'},},")


table="'use strict'\n"+"var table = {"+table[:-1]+"}"
f=open('table500.js','w')
f.write(table)