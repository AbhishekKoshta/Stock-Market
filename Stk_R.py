from IPython import get_ipython
get_ipython().magic('reset -sf')
import time
sta = time.clock()
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
from itertools import islice
import xlsxwriter

workbook = xlsxwriter.Workbook('Stock_wise.xlsx')

Name  = input("Please enter name of the stock ")
base_url ='http://www.moneycontrol.com/india/stockpricequote/'+Name


page = requests.get(base_url)
print (base_url)
print (page.content)

'''
worksheet = workbook.add_worksheet(Name)
worksheet.set_column('A:A', 20)
worksheet.write('A1', 'Company Name')
worksheet.write('B1', 2016)
worksheet.write('C1', 2015)
worksheet.write('D1', 2014)
worksheet.write('E1', 2013)
worksheet.write('F1', 2012)

TNC =2750 ; Comps=[]; qw=[]
soup = BeautifulSoup(html)
tags = soup('a')
b = 0; ccode=[]
for tag in islice(tags,258,None):
    comp = tag.get('href', None)
    b = b + 1
    # print comp
    if b < TNC:
#        print comp
        try:
            sp = comp.split('/')
            Comps.append(sp[6])
            ccode.append(sp[7])
        except:
#            sp = comp.split('/')
            Comps.append('None')
            ccode.append('None')

for j in range(0,len(Comps)-2):
    try:
        url='http://www.moneycontrol.com/financials/'+str(Comps[j])+'/results/yearly/'+ str(ccode[j])+'#' + str(ccode[j])
    #    ul = 'http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01'
    except:
        print ("Broken link", j)
    try:
        k = urllib2.urlopen(url)
        nx=0
        for line in k:
            if "Net Profit/" in line:  # look for Eastern Time
                profit = (''.join(islice(k, 6)))
                sr = re.findall(r"[-+]?\d*\.*\d+", profit)
                print (len(Comps)-j), Comps[j]
                worksheet.write(j+1, 0, str(Comps[j]))
                try: 
                    worksheet.write(j+1, 1, float(sr[0]))
                except :
                    worksheet.write(j+1, 1, 'Not given')
                try:
                    worksheet.write(j+1, 2,  float(sr[1]))
                except:
                    worksheet.write(j+1, 2,  'Not given')
                try:
                    worksheet.write(j+1, 3,  float(sr[2]))
                except:    
                    worksheet.write(j+1, 3,  'Not given')
                try:
                    worksheet.write(j+1, 4,  float(sr[3]))
                except:
                    worksheet.write(j+1, 4,  'Not given')
                try:
                    worksheet.write(j+1, 5,  float(sr[4]))
                except:    
                    worksheet.write(j+1, 5,  'Not given')
    except:
        print ("URL NOT FOUND")
workbook.close()       

print (time.clock()-start_time, 'seconds')
'''   