#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


wubi = "98"
firstDict = {}
secondDict = {}
thirdDict = {}
wholeDict = {}
table = ''

#tableName = '98五笔-全码-单字-码表'
#tableName = '一简二重字(可选)'
#tableName = '常用字-一级简码'
#tableName = '常用字-三级简码'
#tableName = '常用字-二级简码'
#tableName = '常用字-全码-三码'
#tableName = '常用字-全码-四码'
#tableName = '生僻字'

tableName = 'table'


with open('./'+wubi+'WuBi/'+'98五笔-全码-单字-码表'+'.txt',encoding='utf-8') as f:
    for line in f.readlines():
        wholeDict[line.strip().split(" ")[0]]=line.strip().split(" ")[1]

with open('./'+wubi+'WuBi/'+'常用字-三级简码'+'.txt',encoding='utf-8') as f:
    for line in f.readlines():
        thirdDict[line.strip().split(" ")[0]]=line.strip().split(" ")[1]

with open('./'+wubi+'WuBi/'+'常用字-二级简码'+'.txt',encoding='utf-8') as f:
    for line in f.readlines():
        secondDict[line.strip().split(" ")[0]]=line.strip().split(" ")[1]

with open('./'+wubi+'WuBi/'+'常用字-一级简码'+'.txt',encoding='utf-8') as f:
    for line in f.readlines():
        firstDict[line.strip().split(" ")[0]]=line.strip().split(" ")[1]

for key in wholeDict:
    # url = 'http://att.chaiwubi.com/wubi/'+wubi+'tj/'+character+'.gif'
    # r = requests.get(url, allow_redirects=True)
    # open('./'+wubi+'/'+tableName+'/'+character+'.gif','wb').write(r.content)
    first = firstDict.get(key,'')
    second = secondDict.get(key,'')
    third = thirdDict.get(key,'')
    whole = wholeDict.get(key,'')
    table+=("'"+key+"': {'wubi"+wubi+"':{'code':{'first':'"+first+"','second':'"+second+"','third':'"+third+"','whole':'"+whole+"'},'base':true,'single':true,'decomposition':'/typing/res/decomposition/"+key+".gif'},},")


table="'use strict'\n"+"var table = {"+table[:-1]+"}"
f=open('./'+wubi+'/'+tableName+'.js','w')
f.write(table)
