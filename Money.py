import time
start_time=time.clock()
import urllib
#import urllib2
from bs4 import BeautifulSoup
#from BeautifulSoup import *
from itertools import islice
from pandas import DataFrame
import pandas as pd
import xlsxwriter
import urllib.request
workbook = xlsxwriter.Workbook('Name_wise1.xlsx')

#categ = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
categ = ['Z']
for c in range(0,len(categ)):
    categoery='http://www.moneycontrol.com/india/stockpricequote/'+categ[c]
    
#    html = urllib.urlopen(categoery).read()
    html = urllib.request.urlopen(categoery).read()
    
    
    worksheet = workbook.add_worksheet(categ[c])
    worksheet.set_column('A:A', 20)
    worksheet.write('A1', 'Company Name')
    worksheet.write('B1', 2016)
    worksheet.write('C1', 2015)
    worksheet.write('D1', 2014)
    worksheet.write('E1', 2013)
    worksheet.write('F1', 2012)
    print ('\n',categoery)
    
    TNC =2750 ; Comps=[]; qw=[]
    soup = BeautifulSoup(html)
    tags = soup('a')
    b = 0; ccode=[]
    
    for tag in islice(tags,258,None):
        comp = tag.get('href', None)
        b = b + 1
#        print (comp,b)

        if b < TNC:
    #        print comp
            try:
                sp = comp.split('/')
                Comps.append(sp[6])
                ccode.append(sp[7])
            except:
                pass
    #            sp = comp.split('/')
#                Comps.append('None')
#                ccode.append('None')
    
    for j in range(0,len(Comps)-40):
        try:
            url='http://www.moneycontrol.com/financials/'+str(Comps[j])+'/results/yearly/'+ str(ccode[j])+'#' + str(ccode[j])
#            print (url)
        #    ul = 'http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01'
#'http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01'
        except:
            print ("Broken link", j)
        try:
#            k = urllib2.urlopen(url)
#            print ("Trying")
            k = urllib.request.urlopen(url).read()
#            k = urllib.request.urlopen(url).read()
#            print (urllib.request.urlopen(url))
            nx=0
#            for line in urllib.request.urlopen('http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01').read():
            for line in urllib.request.urlopen(url):
#                if "Net Profit/" in line:  # look for Eastern Time  Python2
                if b"Net Profit/" in line:  # look for Eastern Time  Python 3
                    print ("Found net profit", line)
#                    profit = (''.join(islice(k, 6)))
                    profit = (''.join(str(islice(k, 6))))
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
            pass
workbook.close()       

print (time.clock()-start_time, 'seconds')
   
'''
http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01

import urllib
import urllib2
from BeautifulSoup import *
# food_item = raw_input('Enter food item ')
url = 'http://www.moneycontrol.com/stocks/marketinfo/marketcap/nse/index.html' #+ food_item
html =urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
tags = soup ('a')
y=[]; k=[]
for tag in tags :
    z = tag.get('href', None)
    # var1, var2 = z.split(" ");
    # if z.startswith( '/calories-nutrition/generic/' ):
    # prfloat 'Similar match ',  z[z.find('c/')+2:],'have following amount of carbs in 100 gram'
    y.append(z)
prfloat len(y) 

for i in range(0,len(y)):
    if 'india/stockprice' in str(y[i]):
        print str(y[i])
        

'''
'''
ex = DataFrame({str(Comps[j]): sr})
#            ex = DataFrame({str(Comps[j]): sr}, index=['2016','2015','2014','2013','2012'])
#            # import pdb
#            # pdb.set_trace()
##            nx=nx+2
##            qw.append(ex.T)
#            qwa=ex
#            print ex.T
#            ex.append(DataFrame({str(Comps[j]): sr}, index=['2016','2015','2014','2013','2012']))
#            ex.to_excel(writer,sheet_name='Company starting with A',startrow=j+nx)
#            df = DataFrame(columns=('Company Name', '2016','2015','2014','2013','2012',))
#            df.loc[j] = [str(Comps[j]),sr[0],sr[1],sr[2],sr[3],sr[4]]
#            df.to_excel(writer,sheet_name='Company with A')
            
            '''