# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:23:26 2022

@author: Vincent Medrano
"""

"""
The formula for how much your payment would be were you to borrow PV dollars
at APR of r% for n months:
    
Pmt =  r/1200*PV/(1-(1+(r/1200))**(-n))

r/1200 because we have annual percentage rate and we need rate/time period,
i.e. rate/month and we need it as a decimal, not a percent...
For example APR = 5.5, expressed as a decimal is 5.5/100, and then express this
as a monthly amount 5.5/(100*12)

Assignment: write a Python program that takes

1. how much you borrow (PV),

2. the annual percentage rate, r, and

3. how many months you pay on the loan

compute and print the monthly payment    
"""


#Amount borrowed
PV = int(input("How much are you borrowing?:"))

#APR
r = int(input("APR?:"))

#Number of months
n = int(input("How many months?:"))


#Calculation
pmt = r/1200*PV/(1-(1+(r/1200))**(-n))

print("That is $" + "%.2f" % pmt + " a month.")