import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
'''
try:
    Name = raw_input("Name of the stock ")
    Base_url =("https://www.nseindia.com/live_market/dynaContent/"+
           "live_watch/option_chain/optionKeys.jsp?symbolCode=2772&symbol=" + Name+"&"+
           "symbol="+Name+"&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17")
except:
    Base_url =("https://www.nseindia.com/live_market/dynaContent/"+
           "live_watch/option_chain/optionKeys.jsp?symbolCode=2772&symbol=UBL&"+
           "symbol=UBL&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17")

Name = "ubl"
Base_url =("https://www.nseindia.com/live_market/dynaContent/"+
           "live_watch/option_chain/optionKeys.jsp?symbolCode=2772&symbol=UBL&"+
           "symbol=UBL&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17")
'''    

#Name = raw_input("Name of the stock ")    
Name = input("Name of the stock ")    
Base_url = "https://nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=797&symbol="+Name+"&symbol="+Name+"&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17"

if Name is '':
    Base_url = "https://nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=797&symbol=pnb&symbol=pnb&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17"
    Name = 'pnb'
 
page = requests.get(Base_url)
page.status_code
page.content

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

table_it = soup.find_all(class_="opttbldata")
table_cls_1 = soup.find_all(id="octable")

col_list = []

# The code given below will pull the headers of the Option Chain table
for mytable in table_cls_1:
    table_head = mytable.find('thead')
    
    try:
        rows = table_head.find_all('tr')
        for tr in rows: 
            cols = tr.find_all('th')
            for th in cols:
                er = th.text
                ee = er.encode('utf8')       
                col_list.append(ee)
                
    except:
        print ("no thead")
    

col_list_fnl = [e for e in col_list if e not in ('CALLS','PUTS','Chart','\xc2\xa0')]
                
print (col_list_fnl)

table_cls_2 = soup.find(id="octable")
all_trs = table_cls_2.find_all('tr')
req_row = table_cls_2.find_all('tr')

new_table = pd.DataFrame(index=range(0,len(req_row)-3) , columns=col_list_fnl)

row_marker = 0 

for row_number, tr_nos in enumerate(req_row):
     
     # This ensures that we use only the rows with values    
     if row_number <=1 or row_number == len(req_row)-1:   
         continue
          
     td_columns = tr_nos.find_all('td')
     
     # This removes the graphs columns
     select_cols = td_columns[1:22]                  
     cols_horizontal = range(0,len(select_cols))
      
     for nu, column in enumerate(select_cols):
         
         utf_string = column.get_text()
         utf_string = utf_string.strip('\n\r\t": ')
         tr = utf_string.encode('utf8')
         tr = tr.replace(',' , '')
         new_table.ix[row_marker,[nu]]= tr
         
     row_marker += 1   
          
print (new_table)
fil = Name + 'Option_Chain_Table.xlsx'
new_table.to_excel(fil)
newdata = pd.read_excel(fil)
newdata = newdata.fillna(0)
newdata = newdata.replace('-',0)
newdata['Help'] = newdata['Strike Price'] - newdata['Strike Price'][0]
newdata['CALL'] = pd.to_numeric(newdata['OI'])
newdata['PUT'] = pd.to_numeric(newdata['OI.1'])


a=1
cumc = [0] ; cump= [0] 
nos = len(newdata['Strike Price'])
while a < len(newdata['Strike Price']):
    temp = 0
    temp1 = 0
    for i in range(a):
        for j in range(a,a+1):
#            print (i,j-i,newdata['CALL'][i] , newdata['Help'][j],a)
            temp = float(newdata['CALL'][i]) * newdata['Help'][j-i] + temp
            
            temp1 = float(newdata['PUT'][nos-i-1]) * newdata['Help'][j-i] + temp1
            
#            print temp
    cumc.append(temp)
    cump.append(temp1)
    a+=1
    
newdata["CUM_Call"] = cumc
newdata["CUM_Put"] = cump[::-1]
newdata['TV'] = newdata["CUM_Call"]  + newdata["CUM_Put"] 
Exp = newdata[newdata["TV"] == min(newdata['TV'])]["Strike Price"]
PCR = sum(newdata['PUT'])/float(sum(newdata['CALL']))
gi = pd.Index(newdata['TV']).get_loc(min(newdata['TV']))
for i in range(gi-2,gi+3):
#    print  # newdata['TV'][i]
    print (int(newdata['Strike Price'][i]), round((newdata['TV'][i]-newdata['TV'][gi])/newdata['TV'][gi]*100,3))

fig, max_pain = plt.subplots()
max_pain.bar(newdata['Strike Price'],newdata['TV'])
plt.xticks(newdata['Strike Price'],rotation=90)
title = "{}, 68 % chances of expiring at {}, with PCR of {}".format(Name.upper(),Exp,PCR)
plt.title(title)
plt.savefig("{}.png".format(Name))

print ("====================================================\n")
print ("There is 68 % chances that the stocks will expire at ",Exp)
print ("====================================================\n")

print ("PCR value",PCR)

if PCR>1.3:
    print ("Bullish reversal might come in place",PCR)
elif PCR < 0.5:
        print ("Bearish reversal might kick off",PCR)
        print ("Stock might go down")
newdata['TV'][20]            
        

check = pd.DataFrame()
check['Strike Price'] = newdata['Strike Price']
check['Call'] = newdata['CALL']
check['Put'] = newdata['PUT']
check['CUM_Call'] = newdata['CUM_Call']
check['CUM_Put'] = newdata['CUM_Put']
check['TV'] = newdata['TV']
#print check
