#!/usr/bin/env python
# coding: utf-8

# In[105]:


import requests
import pandas

from bs4 import BeautifulSoup

r= requests.get("https://www.hindustantimes.com/tech/")
c= r.content


soup = BeautifulSoup(c,"html.parser")


mediabody = soup.find_all("div",{"class" : "media-body"})
l=[]
for media in mediabody :
    d={}
    try : 
        d["headline"] = media.a.text
    except:
        d["headline"] = None
    try:
        d['shortInformation'] = media.p.text
    except :
        d['shortInformation'] = None
    try :
        r= requests.get(media.a['href'])
        c= r.content
        soup = BeautifulSoup(c,'html.parser')
        story= ''
        para = soup.find('div',{'class': 'story-details'}).find_all('p')
        for p in para:
            story = story + p.text
        print(story)
        
        d['story'] = story
        
    except :
        print("except")
        
    l.append(d)
    
df = pandas.DataFrame(l)
df.to_csv('output.csv')


# In[ ]:




