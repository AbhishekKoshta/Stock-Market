import re
import urllib
from bs4 import BeautifulSoup
from itertools import islice
import pandas as pd

data = pd.read_excel("Links.xlsx")
#URLs = ['http://www.moneycontrol.com/india/stockpricequote/plastics/primaplastics/PP21',
#        'http://www.moneycontrol.com/india/stockpricequote/breweries-distilleries/associatedalcoholbreweries/AAB']
#cash = 'http://www.moneycontrol.com/financials/primaplastics/balance-sheetVI/PP21#PP21'
#share = 'http://www.moneycontrol.com/company-facts/primaplastics/shareholding-pattern/PP21#PP21'

URLs = data["Links"]

Stk_Pick = pd.DataFrame()
Stock = []; market_cap = []; LTP = []
pe = [];  eps = [] ;  indpe = []
tdbt = [];  casheq = [];  shld = []
NSEp = [];  BSE_p = []; Sector = []


for i in range(len(URLs)):
#for i in range(1):
    html = urllib.urlopen(URLs[i])
    html1 = urllib.urlopen(URLs[i]).read()
    URLsp = URLs[i].split('/')
    cash = 'http://www.moneycontrol.com/financials/' + URLsp[-2] + '/balance-sheetVI/' + URLsp[-1] + '#' + URLsp[-1]
    cash_htm = urllib.urlopen(cash)
    share = 'http://www.moneycontrol.com/company-facts/' + URLsp[-2] + '/shareholding-pattern/'+URLsp[-1] + '#' + URLsp[-1]
    sh_htm = urllib.urlopen(share)
    gD_12 = 0   
    print ("====================================Stock {}===========================================".format(URLsp[-2]))
    Stock.append(URLsp[-2])
    Sector.append(URLsp[-3])
    
    print URLs[i]
    
    for line in html:
        if 'Nse_Prc_tick' in line:
            soup = BeautifulSoup(line,'html.parser')
            NSE_LTP = soup.find_all('strong')[0].text
            NSEp.append(NSE_LTP)
            print ("NSE",NSE_LTP)
            
        if 'Bse_Prc_tick' in line:
            soup = BeautifulSoup(line,'html.parser')
            BSE_LTP = soup.find_all('strong')[0].text
            BSE_p.append(BSE_LTP)
            print ("BSE",BSE_LTP)
#        try:
#            LTP.append(float(NSE_LTP))
#        except:
#            LTP.append(float(BSE_LTP))
            
        if 'FR gD_12' in line:
            gD_12+=1
            if gD_12==1:
                Market_cap = re.findall('[0-9.,]+',line)[1]
                try:
                    market_cap.append(float(Market_cap))
                except:
                    market_cap.append(float(''.join(Market_cap.split(','))))
                    
                print "Market cap",re.findall('[0-9.]+',line)[1]
            
            if gD_12==2:
                try:
                    PE = re.findall('[0-9.]+',line)[1]
                    pe.append(float(PE))
                    print "PE",re.findall('[0-9.]+',line)[1]
                except:
                    pe.append(0)
                    print ("---------------------Not able to find PE----------------------------")                        
                

            if gD_12==6:
                Ind_PE = re.findall('[0-9.]+',line)[1]
                indpe.append(float(Ind_PE))
                print "Industry PE",re.findall('[0-9.]+',line)[1]     

            if gD_12==7:
                EPS = re.findall('[0-9.]+',line)[1]
                eps.append(float(EPS))
                print "EPS",re.findall('[0-9.]+',line)[1]                
                
        if 'Total Debt' in line:
            next(html)
#            next(html,10)
            Total_Debt = re.findall('[0-9.]+',next(html))[-1]
            tdbt.append(float(Total_Debt))
            print "Total Debt", Total_Debt
            break
                

    for lin in cash_htm:
        if "Cash And Cash Equivalents" in lin:
            next(cash_htm)
            Cash = re.findall('[0-9.]+',next(cash_htm))[0]
            casheq.append(float(Cash))
            print ("Cash equivalent",Cash)
            

    for lin in sh_htm:
        if "Total shareholding of Promoter and Promoter Group (A)" in lin:
            next(sh_htm); next(sh_htm);next(sh_htm);next(sh_htm)
            Shr = re.findall('[0-9.]+',next(sh_htm))[1]
            shld.append(float(Shr))
            print ("Share Holding",Shr)            

    if len(casheq) < len(Stock):
        casheq.append(0)
        print ("")
    if len(shld) < len(Stock):
        shld.append("NA")
    try:
        LTP.append(float(NSE_LTP))
    except:
        LTP.append(BSE_LTP)
            
Stk_Pick['Sector'] = Sector
Stk_Pick['Stock'] = Stock
Stk_Pick['LTP'] = LTP
Stk_Pick['PE'] = pe
Stk_Pick['Industry PE'] = indpe
Stk_Pick['PE/Industry PE'] = Stk_Pick['PE']/Stk_Pick['Industry PE']
Stk_Pick['Market cap'] = market_cap
Stk_Pick['Debt'] = tdbt
Stk_Pick['Debt/Markt cap'] = Stk_Pick['Debt']/Stk_Pick['Market cap'] 
Stk_Pick['Cash Eq'] = casheq
Stk_Pick['Cash/Market cap'] = Stk_Pick['Cash Eq']/Stk_Pick['Market cap'] *100

Stk_Pick['Share Holding'] = shld
Stk_Pick['EPS'] = eps

Stk_Pick.to_excel("Best_Stock_Selection2.xlsx")            



