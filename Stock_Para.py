#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:34:36 2018

@author: kvv
"""
import re
import urllib
from bs4 import BeautifulSoup
from itertools import islice

URLs = [
        "http://www.moneycontrol.com/india/stockpricequote/electric-equipment/websolenergysystem/WSL"
        ]

#cash = 'http://www.moneycontrol.com/financials/primaplastics/balance-sheetVI/PP21#PP21'
#share = 'http://www.moneycontrol.com/company-facts/primaplastics/shareholding-pattern/PP21#PP21'

for i in range(1):
    html = urllib.urlopen(URLs[i])
    html1 = urllib.urlopen(URLs[i]).read()
    URLsp = URLs[i].split('/')
    cash = 'http://www.moneycontrol.com/financials/' + URLsp[-2] + '/balance-sheetVI/' + URLsp[-1] + '#' + URLsp[-1]
    cash_htm = urllib.urlopen(cash)
    share = 'http://www.moneycontrol.com/company-facts/' + URLsp[-2] + '/shareholding-pattern/'+URLsp[-1] + '#' + URLsp[-1]
    sh_htm = urllib.urlopen(share)
    gD_12 = 0   
    print ("{}".format(URLsp[-2]))
    for line in html:
        if 'Nse_Prc_tick' in line:
            soup = BeautifulSoup(line,'html.parser')
            NSE_LTP = soup.find_all('strong')[0].text
            print ("NSE",NSE_LTP)
        if 'Bse_Prc_tick' in line:
            soup = BeautifulSoup(line,'html.parser')
            BSE_LTP = soup.find_all('strong')[0].text
            print ("BSE",BSE_LTP)
        

        if 'FR gD_12' in line:
            gD_12+=1
            if gD_12==1:
                Market_cap = re.findall('[0-9.]+',line)[1]
                print "Market cap",re.findall('[0-9.]+',line)[1]
            
            if gD_12==2:
                PE = re.findall('[0-9.]+',line)[1]
                print "PE",re.findall('[0-9.]+',line)[1]
                

            if gD_12==6:
                Ind_PE = re.findall('[0-9.]+',line)[1]
                print "Industry PE",re.findall('[0-9.]+',line)[1]     

            if gD_12==7:
                EPS = re.findall('[0-9.]+',line)[1]
                print "EPS",re.findall('[0-9.]+',line)[1]                
                
        if 'Total Debt' in line:
            next(html)
#            next(html,10)
            Total_Debt = re.findall('[0-9.]+',next(html))[-1]
            print "Total Debt", Total_Debt
            break
                

    for lin in cash_htm:
        if "Cash And Cash Equivalents" in lin:
            next(cash_htm)
            Cash = re.findall('[0-9.]+',next(cash_htm))[0]
            print ("Cash equivalent",Cash)

    for lin in sh_htm:
        if "Total shareholding of Promoter and Promoter Group (A)" in lin:
            next(sh_htm); next(sh_htm);next(sh_htm);next(sh_htm)
            Shr = re.findall('[0-9.]+',next(sh_htm))[1]
            print ("Share Holding",Shr)            