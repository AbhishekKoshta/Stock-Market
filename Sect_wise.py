import time
start_time=time.clock()
import urllib
import urllib2
from BeautifulSoup import *
from itertools import islice
from pandas import DataFrame
import pandas as pd
import xlsxwriter

workbook = xlsxwriter.Workbook('Profit_Review.xlsx')
worksheet = workbook.add_worksheet('All')
categ = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#categ = ['X','Z']
alphabets=-1; Total_comp=[0]
for c in range(0,len(categ)):
    categoery='http://www.moneycontrol.com/india/stockpricequote/'+categ[c]
    html = urllib.urlopen(categoery).read()
    worksheet.set_column('B:B', 20)
    worksheet.write('A1', 'Sector')
    worksheet.write('B1','Company name')
    worksheet.write('C1', 2016)
    worksheet.write('D1', 2015)
    worksheet.write('E1', 2014)
    worksheet.write('F1', 2013)
    worksheet.write('G1', 2012)
    alphabets=alphabets+1    
    C_starts = 1350; TNC =4000-1350; Comps=[]; qw=[]
    soup = BeautifulSoup(html)
    tags = soup('a')
    b = 0; ccode=[];sector=[]
    print categoery
    for tag in islice(tags,200,None):   # 200 is used to avoid initial 200 link which is not of  a company
        comp = tag.get('href', None)
        b = b + 1
        # print comp
        if b < TNC:
            try:
                sp = comp.split('/')
                sector.append(sp[5])
                Comps.append(sp[6])
                ccode.append(sp[7])
                print sp[6]
            except:
                print "Not Valid address"
    #                sp = comp.split('/')
    #                Comps.append('None')
    #                ccode.append('None')
            
    for j in range(0,len(Comps)-2):
#    for j in range(0,4):
        try:
            url='http://www.moneycontrol.com/financials/'+str(Comps[j])+'/results/yearly/'+ str(ccode[j])+'#' + str(ccode[j])
        #    ul = 'http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01'
        except:
            print "Not a company's link", j
        try:
            k = urllib2.urlopen(url)
            nx=0
            for line in k:
                if "Net Profit/" in line:  # look for Eastern Time
                    profit = (''.join(islice(k, 6)))
                    sr = re.findall(r"[-+]?\d*\.*\d+", profit)
#                    print (len(Comps)-j), Comps[j]
                    
                    worksheet.write(j+1+Total_comp[len(Total_comp)-1], 0, str(sector[j]))
                    worksheet.write(j+1+Total_comp[len(Total_comp)-1], 1, str(Comps[j]))
                    try: 
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 2, float(sr[0]))
                    except :
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 2, 'Not given')
                    try:
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 3,  float(sr[1]))
                    except:
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 3,  'Not given')
                    try:
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 4,  float(sr[2]))
                    except:    
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 4,  'Not given')
                    try:
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 5,  float(sr[3]))
                    except:
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 5,  'Not given')
                    try:
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 6,  float(sr[4]))
                    except:    
                        worksheet.write(j+1+Total_comp[len(Total_comp)-1], 6,  'Not given')
        except:
            print "URL NOT FOUND"

    Total_comp.append(len(Comps))   
    print Total_comp     
workbook.close()       

print time.clock()-start_time, 'seconds'
#print sector