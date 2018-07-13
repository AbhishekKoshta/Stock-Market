import time
start_time=time.clock()
import urllib
from bs4 import BeautifulSoup
from itertools import islice
from pandas import DataFrame
import pandas as pd

Comps=[];   ccode=[];   Indus = []

categ = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#categ = ['Z']
for c in range(0,len(categ)):
    categoery='http://www.moneycontrol.com/india/stockpricequote/'+categ[c]    
#    html = urllib.urlopen(categoery).read()
    html = urllib.urlopen(categoery).read()
    
    print (categoery)
    
    TNC =2750 ;  qw=[]
    soup = BeautifulSoup(html)
    tags = soup('a')
    b = 0; 
    
    for tag in islice(tags,258,None):
        comp = tag.get('href', None)
        b = b + 1

        if b < TNC:
    #        print comp
            try:
                sp = comp.split('/')
                if len(sp[7]) > 1:
                    Indus.append(sp[5])
                    Comps.append(sp[6])
                    ccode.append(sp[7])
                    print (comp,b)

            except:
                pass
C_Codes = pd.DataFrame()
C_Codes["Industry"] = Indus
C_Codes["Company"] = Comps
C_Codes["Code"] = ccode
C_Codes.to_excel("Stock_Codes.xlsx")    
    
print (time.clock()-start_time, 'seconds')

URLs = ['http://www.moneycontrol.com/india/stockpricequote/plastics/primaplastics/PP21']
for i in range(1):
    html = urllib.urlopen(URLs[i]).read()
    a=0
    for line in html:
        print line
        a+=1
    print a