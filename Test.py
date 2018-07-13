# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 04:51:40 2018

@author: iitb_student
"""

#'http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01'
from itertools import islice
k = urllib.request.urlopen('http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01')
for line in urllib.request.urlopen('http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01'):
#    print (line)
    if b'Net Profit/' in line:  # look for Eastern Time
        print ("Found net profit", line)
        profit = (''.join(islice(k, 6)))
        print (profit)

#for line in urllib.request.urlopen('http://www.moneycontrol.com/financials/afenterprises/results/yearly/AFE01#AFE01').read():
#    print (line)        