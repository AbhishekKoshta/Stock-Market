#from IPython import get_ipython
#get_ipython().magic('reset -sf')
import time
start_time = time.clock()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
data = pd.read_excel("ck.xlsx")
#data = pd.read_excel("Valid.xlsx")

data  = data.fillna(0)
data = data.replace('-',0)
data.to_csv("Final_PCR.csv")


newdata = pd.DataFrame(data['SP'])
newdata['CALL'] = data['CALL']
newdata['PUT'] = data['PUT']
newdata['Help'] = data['SP'] - data['SP'][0]

a=1
cumc = [0] ; cump= [0] 
nos = len(newdata['SP'])
while a < len(newdata['SP']):
    temp = 0
    temp1 = 0
    for i in range(a):
        for j in range(a,a+1):
#            print (i,j-i,newdata['CALL'][i] , newdata['Help'][j],a)
            temp = newdata['CALL'][i] * newdata['Help'][j-i] + temp
            
            temp1 = newdata['PUT'][nos-i-1] * newdata['Help'][j-i] + temp1
            
#            print temp
    cumc.append(temp)
    cump.append(temp1)
    a+=1
    
newdata["CUM_Call"] = cumc
newdata["CUM_Put"] = cump[::-1]
newdata['TV'] = newdata["CUM_Call"]  + newdata["CUM_Put"] 
Exp = newdata[newdata["TV"] == min(newdata['TV'])]["SP"]
PCR = sum(newdata['PUT'])/sum(newdata['CALL'])
gi = pd.Index(newdata['TV']).get_loc(min(newdata['TV']))
for i in range(gi-4,gi+5):
#    print  # newdata['TV'][i]
    print (newdata['SP'][i]), round((newdata['TV'][i]-newdata['TV'][gi])/newdata['TV'][gi]*100,3)

fig, max_pain = plt.subplots()
max_pain.bar(newdata['SP'],newdata['TV'])
plt.xticks(newdata['SP'],rotation=90)
title = "68 % chances of expiring at {}, with PCR of {}".format(Exp,PCR)
plt.title(title)
plt.savefig("PCR.png")

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
        
os.remove(fil)        