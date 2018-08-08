#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import numpy as np
import json
# from bs4 import BeautifulSoup
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

characterList = []
table = ''
with open('./98WuBi/常用字-全码-三码.txt',encoding='utf-8') as f:
    for line in f.readlines():
        # print(line.strip())
        characterList.append(line.strip())


# root_url = "http://www.chaiwubi.com/bmcx/"
# driver = webdriver.Firefox()
# driver.get(root_url)

for character in characterList:
    url = 'http://att.chaiwubi.com/wubi/98tj/'+character+'.gif'
    # url = 'http://att.chaiwubi.com/wubi/86tj/'+character+'.gif'
    r = requests.get(url, allow_redirects=True)
    open('./98/'+character+'.gif','wb').write(r.content)
    
    # inputCharacter = driver.find_element_by_id('kw')
    # inputCharacter.send_keys(character)
    # inputCharacter.send_keys(Keys.ENTER)

    # driver.implicitly_wait(10)

    # heading = driver.find_element_by_class_name('dw-bmcx')
    # # chart = driver.find_element_by_id('zid1')
    # print(heading.get_attribute('innerHTML'))
    
    # # click submit button
    # # submit_button = driver.find_element_by_id('cwb_cx')[0]
    # # submit_button.click()

    # # page = urllib.request.urlopen(root_url)
    # # html = page.read().decode('utf-8')

    # # soup = BeautifulSoup(html)

    # # <input id="kw" name="wz" type="text" value="的" maxlength="30" onfocus="if(this.value=='的'){this.value='';}" onblur="if(this.value==''){this.value='的';}" />
    


    # # <button id="cwb_cx" type="submit">点此查询</button>


    # # chart = soup.find("table",attrs={"class":"details"})

    # # # The first tr contains the field names.
    # # headings = [th.get_text() for th in table.find("tr").find_all("td")]

    # # datasets = []
    # # for row in table.find_all("tr")[1:]:
    # #     dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    # #     datasets.append(dataset)
    # # print datasets

    

    # break

    # first = 'x'
    # second = 'xx'
    # third = 'xxx'
    # whole = 'xxxx'
    # table+=("'"+character+"': {'wubi86':{'code':{'first':'"+first+"','second':'"+second+"','third':'"+third+"','whole':'"+whole+"'},'base':true,'single':true,'decomposition':'/typing/res/decomposition/"+character+".gif'},},")

# driver.close()


# table="'use strict'\n"+"var table = {"+table[:-1]+"}"
# f=open('table500.js','w')
# f.write(table)