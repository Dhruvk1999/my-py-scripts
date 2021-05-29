# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:28:27 2021

@author: Dhruv
"""
import bs4,requests
import re

res=requests.get('http://knowledgeplatform.in/em-ea/question-bank/')
res.raise_for_status()
text=bs4.BeautifulSoup(res.text)
links=text.find_all('a')
pdfs=[]
lists=list(links)
for i in range(len(lists)):
    if 'pdf' in str(lists[i]):
        pdfs.append(lists[i])
    else:
        pass


file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
  
for i in range(len(pdfs)):
    r = requests.get(pdfs[i].get('href'), stream = True)
      
    with open(str(i)+".pdf","wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
      
             # writing one chunk at a time to pdf file
             if chunk:
                 pdf.write(chunk)